import sys
import os
import subprocess
from os import listdir
from os.path import isfile, join

assert len(sys.argv) == 3, f"usage {sys.argv[0]} in-dir out-dir"
in_dir = sys.argv[1]
out_dir = sys.argv[2]

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

for f in listdir(in_dir):
    if f.startswith('.'):
        continue
    if f.startswith('#'):
        continue
    if not f.endswith('.py'):
        continue
    def hint():
        global count_skip, skipping, indent_prefix
        if count_skip <= 1:
            print(indent_prefix + f"# HINT: goal = 1 line of code", file=out_fp)
        else:
            print(indent_prefix + f"# HINT: goal <= {count_skip} lines of code", file=out_fp)
        print(indent_prefix + "raise NotImplementedError()",
              file=out_fp)
        print('', file=out_fp)
        count_skip = 0
        skipping = False
        indent_prefix = ''

    print(f"filtering: {f}")
    in_fp = open(join(in_dir, f), 'r')
    out_fp = open(join(out_dir, f), 'w')
    skipping = False
    indent_prefix = ''
    count_skip = 0
    for line in in_fp.readlines():
        if line.startswith('from solutions.'):
            print('from src', end='', file=out_fp)
            print(line[len('from solutions'):], end='', file=out_fp)
            continue
        if '# CHALLENGE: ' in line:
            skipping = True
            indent_prefix = line.split('#')[0]
            print(line, end='', file=out_fp)
            continue
        # if skipping and we find a blank line, just skip it.
        if not skipping and line == '\n' and not indent_prefix:
            print(line, end='', file=out_fp)
            continue
        if skipping and line == '\n':
            continue
        # if indentation lessens (block ends) then stop skipping
        if skipping and not line.startswith(indent_prefix):
            hint()
        #if skipping and not (line == '\n' or line.startswith(' ') or line.startswith('\t')):
        #    skipping = False
        if not skipping:
            print(line,
                  end='',
                  file=out_fp)
        if skipping and indent_prefix and not line.startswith(indent_prefix + "#"):
            count_skip += 1
    if skipping:
        hint()
    in_fp.close()
    out_fp.close()

    num_source_lines = count_lines_file(join(in_dir, f))
    num_target_lines = count_lines_file(join(out_dir, f))
    delta = num_source_lines - num_target_lines

    for dir in [in_dir, out_dir]:
        goal_dir = join(dir, '..', 'tests','goal')
        if not os.path.exists(goal_dir):
            os.makedirs(goal_dir)
        legend = open(join(goal_dir, f + '.linecount'), 'w')
        print(f"{num_source_lines}", file=legend)
        print(f"{delta}", file=legend)
        legend.close()
