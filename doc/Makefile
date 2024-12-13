## Copyright (C) 2024 Jim Newton

all: pdf

SRC_DIR  := .
IMAGE_DIR := $(SRC_DIR)/img
LATEXMK = latexmk -pvc --pdf
%%LATEXMK = latexmk --pdf

pdf: polynomials.pdf

SECTIONS := \
	definitions.tex \
	sec-intro.tex \
	sec-github.tex \
	sec-line.tex \
	sec-quadratic.tex \
	sec-cubic.tex \
	sec-quartic.tex \
	sec-quintic.tex

polynomials.pdf : ${SRC_DIR}/polynomials.tex ${SECTIONS}
	TEXINPUTS=$(TEXINPUTS):$(IMAGE_DIR) \
	${LATEXMK} ${SRC_DIR}/polynomials.tex

clean:
	rm *.pdf *.aux *.log *.toc *.fls *.fdb_latexmk *.out
