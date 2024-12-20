PYTHON = python3


all:
	${PYTHON} ./bin/filter-challenges.py ./solutions ./src
	./make-test-solutions.csh
