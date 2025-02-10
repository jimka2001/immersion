## Copyright (C) 2024 Jim Newton

all: pdf

SRC_DIR  := .
IMAGE_DIR := $(SRC_DIR)/img
%%LATEXMK = latexmk -pvc --pdf
LATEXMK = latexmk --pdf

pdf: polynomials.pdf

SECTIONS := \
	pfg-cubic.tex \
	pfg-line.tex \
	pfg-parabola.tex \
	pfg-quartic-deriv.tex \
	pfg-quartic.tex \
	definitions.tex \
	theorems.tex \
	sec-intro.tex \
	sec-general.tex \
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
