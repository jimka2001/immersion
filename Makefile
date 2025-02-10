PYTHON = python3


all:
	${PYTHON} ./bin/filter-challenges.py ./solutions ./src


test-solutions:
	./make-test-solutions.csh
