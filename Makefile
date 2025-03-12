# Define PYTHON conditionally based on availability of python3 or python
ifeq ($(shell command -v python3),)
    ifeq ($(shell command -v python),)
        $(error No suitable Python interpreter found)
    else
        PYTHON = python
    endif
else
    PYTHON = python3
endif


all: test-solutions
	${PYTHON} ./bin/filter-challenges.py ./solutions ./src


test-solutions:
	./make-test-solutions.csh
