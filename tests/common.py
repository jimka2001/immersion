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
                raise TimeoutError(
                    f"{signum=} {frame=} Function '{func.__name__}' timed out after {TIMEOUT_SECONDS} seconds.")

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


def locate_src_file(pyfile: str) -> str:
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


def canonicalize(seq, epsilon):
    s1 = sorted(seq)
    rounded = {int(round(x/epsilon)) for x in s1}
    return sorted([x*epsilon for x in rounded])



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
        if ar1 == [] and ar2 == []:
            return
        self.assertTrue(ar1 and ar2,
                        f"lists different: {ar1=} {ar2=}")
        self.assertEqual(len(ar1), len(ar2),
                         f"lists have different lengths, {len(ar1)}!={len(ar2)}, {ar1} vs {ar2}" +
                         (f": {msg}" if msg is not None else ""))
        for k in range(len(ar1)):
            self.assertAlmostEqual(ar1[k], ar2[k], digits, msg)

    def code_check(self, pyfiles, exe):
        self.check_load(pyfiles, exe)

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
