#!/bin/csh -f
cd tests
touch x_solution.py
rm *solution.py
foreach test (test_*.py)
    cat $test | sed -e 's/from src[.]/from solutions./' > ${test:r}_solution.py
end
