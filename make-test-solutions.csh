#!/bin/csh -f
cd tests
touch x-solution.py
rm *-solution.py
foreach test (test_*.py)
    cat $test | sed -e 's/from src[.]/from solutions./' > ${test:r}-solution.py
end
