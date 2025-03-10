PYTHON = python3


all: test-solutions
	${PYTHON} ./bin/filter-challenges.py ./solutions ./src


test-solutions:
	./make-test-solutions.csh
