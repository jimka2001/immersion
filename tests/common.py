import unittest
import os
import signal
import functools

test_directory = os.path.dirname(__file__)


# Custom exception for test timeout
class TestTimeoutError(Exception):
    pass


# Decorator for adding timeout functionality to functions/methods
def timeout(TIMEOUT_SECONDS):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            def handler(signum, frame):
                raise TimeoutError(f"{signum=} {frame=} Function '{func.__name__}' timed out after {TIMEOUT_SECONDS} seconds.")

            old_handler = None

            try:
                # signal.SIGALRM fails on windows, so I hope this will trigger the
                #    except clause, and set old_handler to None
                old_handler = signal.signal(signal.SIGALRM, handler)
                signal.alarm(TIMEOUT_SECONDS)
            except Exception:
                old_handler = None
            try:
                result = func(*args, **kwargs)
            finally:
                # old_handler is None if the above try failed on windows.
                if old_handler is not None:
                    signal.alarm(0)  # Reset the alarm
                    signal.signal(signal.SIGALRM, old_handler)
            return result

        return wrapper

    return decorator


def locate_src_file(pyfile:str) -> str:
    """Return full path name to the named python file in the src directory."""
    return os.path.join(test_directory, os.pardir, 'src', pyfile)


def call_with_remapped(old_function,
                       remap,
                       test):
    """Call the given test function with some function remapped to
    a function which counts the number of times it is called.
    old_function is the function object which will be called.
    remap is a function which globally sets the function to the given value.
    test is a function which is run while the function has been
        safely rebound.

    call_with_remapped returns the integer number of times the remapped
       function is called.
    e.g., the following call to call_with_remapped, will call foo,
    and return a tuple (c,v) where c is the number of
    times algebra.recursion.power is called and v is the return value
    of foo.

      def remap(f):
        algebra.recursion.power = f

      call_with_remapped(algebra.recursion.power,
                        remap,
                        foo)
    """
    c = 0

    def new_function(*args):
        nonlocal c
        c += 1
        return old_function(*args)

    try:
        remap(new_function)
        v = test()
    finally:
        remap(old_function)

    return c, v


def captured(thunk):
    # code taken from
    # https://stackoverflow.com/questions/14422797/access-the-printed-output-of-a-function-call
    import io
    import sys
    capture = io.StringIO()
    save, sys.stdout = sys.stdout, capture
    v = thunk()
    sys.stdout = save
    return v, capture.getvalue().splitlines()


# code taken from
# https://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
def which(program):
    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(program)
    if fpath:
        if is_exe(program):
            return program
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            exe_file = os.path.join(path, program)
            if is_exe(exe_file):
                return exe_file

    return None

def count_lines_file(fname: str) -> int:
    in_fp = open(fname, 'r')
    assert in_fp, f"could not open {fname}"
    lines = list(in_fp.readlines())
    num_lines = len(lines)
    comment_lines = [line for line in lines
                     for sline in [line.lstrip()]
                     if sline and sline[0] == '#']
    blank_lines = [line for line in lines
                    if line.isspace()]
    in_fp.close()
    return num_lines - len(comment_lines) - len(blank_lines)

def copy_data(a):
    if isinstance(a, list):
        return [copy_data(x) for x in a]
    else:
        return a

class ImmTestCase(unittest.TestCase):

    @timeout(60)  # no test method should take longer than 60 seconds to run
    def run(self, result=None):
        return super().run(result)
    def assertImmutable3(self, f, arg1, arg2, arg3):
        arg1_save = copy_data(arg1)
        arg2_save = copy_data(arg2)
        arg3_save = copy_data(arg3)
        result = f(arg1, arg2, arg3)
        self.assertEqual(arg1_save, arg1, f"{f} changed arg1 from {arg1_save} to {arg1}")
        self.assertEqual(arg2_save, arg2, f"{f} changed arg2 from {arg2_save} to {arg2}")
        self.assertEqual(arg3_save, arg3, f"{f} changed arg3 from {arg3_save} to {arg3}")
        return result

    def assertImmutable2(self, f, arg1, arg2):
        arg1_save = copy_data(arg1)
        arg2_save = copy_data(arg2)
        result = f(arg1, arg2)
        self.assertEqual(arg1_save, arg1, f"{f} changed arg1 from {arg1_save} to {arg1}")
        self.assertEqual(arg2_save, arg2, f"{f} changed arg2 from {arg2_save} to {arg2}")
        return result

    def assertImmutable1(self, f, arg):
        arg_save = copy_data(arg)

        result = f(arg)
        self.assertEqual(arg_save, arg, f"{f} changed arg from {arg_save} to {arg}")
        return result

    def assertListAlmostEqual(self, ar1, ar2, digits, msg=None):
        self.assertEqual(len(ar1), len(ar2),
                         f"lists have different lengths, {len(ar1)}!={len(ar2)}, {ar1} vs {ar2}" +
                         (f": {msg}" if msg is not None else ""))
        for k in range(len(ar1)):
            self.assertAlmostEqual(ar1[k], ar2[k], digits, msg)

    def check_line_count(self, pyfiles, grace=0):
        for pyfile in pyfiles:
            located = locate_src_file(pyfile)
            assert os.path.exists(located), f"could not locate {located}"

            student_line_count = count_lines_file(located)

            goal_dir = os.path.join(test_directory, 'goal')
            assert os.path.exists(goal_dir), f"directory '{goal_dir}' does not exist"

            goal_file = os.path.join(goal_dir, pyfile + '.linecount')
            assert os.path.exists(goal_file)

            legend = open(goal_file, 'r')
            assert legend, f"could not open {goal_file}"

            goal_line_count, delta = legend.readlines()
            goal_line_count = int(goal_line_count)
            delta = max(2, int(delta) + grace)
            legend.close()

            student_goal = goal_line_count + 2*delta
            self.assertTrue(student_line_count <= student_goal,
                            f"too many lines of code in {pyfile} (ignoring comments and blank lines), found {student_line_count} lines, goal={student_goal} lines")

    def code_check(self, pyfiles, exe):
        import pycodestyle
        issues = []

        def get_line_by_number(fname, lineno):
            fp = open(fname, "r")
            line = fp.readlines()[lineno - 1]
            fp.close()
            return line

        def parse_pep_error(line):
            nnone = [None, None, None, None, None]
            if not line:
                return nnone
            if len(line) > 1 and line[1] == ':':
                # line='c:\\Users\\student\\OneDrive\\Documents\\BscEPITA\\Algebra 2\\linear-algebra-student\\linalg\\tests\\..\\matrix\\Vector.py:163:1: E302 expected 2 blank lines, found 1'
                # skip 'c:' and parse the rest
                fname, lineno, chno, pep = line[2:].split(':', 3)
                # then prepend the 'c:'
                fname = line[0:2] + fname
            else:
                # line="/Users/jnewton/Repos/courses/dir-linear-algebra/linear-algebra/linalg/tests/../matrix/Matrix.py:226:23: E231 missing whitespace after ','"
                fname, lineno, chno, pep = line.split(':', 3)

            if not os.path.isfile(fname):
                return nnone
            culprit = get_line_by_number(fname, int(lineno))
            return fname, lineno, chno, culprit, pep

        for pyfile in pyfiles:
            self.invalid_imports(pyfile)
        self.check_load(pyfiles, exe)

        for pyfile in pyfiles:
            located = locate_src_file(pyfile)
            _, lines = captured(lambda: pycodestyle.StyleGuide(max_line_length=120).input_file(located))
            parsed = [(file, lineno, chno, culprit, pep, line)
                      for line in lines
                      for (file, lineno, chno, culprit, pep) in [parse_pep_error(line)]
                      if not any((": " + ignore + " " in line)
                                 #   E402 module level import not at top of file
                                 #   E401 multiple imports on one line
                                 for ignore in ["E402", "E401"])
                      ]
            for (file, lineno, chno, culprit, pep, line) in parsed:
                prefix = f"   {pyfile} line {lineno}:["
                issues += [f"PEP ERROR: {pep}",
                           f"{file=}",
                           ("-" * (len(prefix) + int(chno) - 2)) + "-+",
                           (" " * (len(prefix) + int(chno) - 2)) + "\\|/",
                           f"{prefix}{culprit}]",
                           ]

        if issues:
            issues_msg = "not expecting PEP issues\n" + '\n'.join(issues)
            report = True
        else:
            issues_msg = ""
            report = False
        self.assertFalse(report, issues_msg)

    def invalid_imports(self, pyfile):
        """Check for certain illegal imports."""
        file_path = locate_src_file(pyfile)
        fp = open(file_path, "r")
        lino = 0
        for statement in fp.readlines():
            lino += 1
            # skip empty line
            if statement.strip() == "":
                continue
            # skip comment line
            if statement.strip()[0] == '#':
                continue
            for tabu in ["math.factorial", "from math import factorial",
                         "math.gcd", "from math import gcd",
                         "from math import *",
                         "numpy", ]:
                self.assertFalse(tabu in statement,
                                 f"invalid line={lino}:[{statement}] in {file_path}")
        fp.close()

    def check_load(self, pyfiles, exe):
        """This method is called with a possible exception which
        was generated by trying to import the student's python file.
        There is code such as the following atop the test case file
        which attempts to import student code.
        The idiom captures any exception thrown by loading the
        student code.
        try:
            from algebra.division import *
            from algebra.polynomial import poly_mult, poly_add
        except Exception as e:
            print(e)
            import_exception = e
        """
        if exe is None:
            return
        self.fail(f"Exception while importing one of {pyfiles}: {exe}")
