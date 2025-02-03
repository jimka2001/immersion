## Copyright (C) 2024 Jim Newton

all: pdf

SRC_DIR  := .
IMAGE_DIR := $(SRC_DIR)/img
LATEXMK = latexmk -pvc --pdf
%%LATEXMK = latexmk --pdf

pdf: polynomials.pdf

SECTIONS := \
	pfg-cubic.tex \
	pfg-cubic-binary1.tex \
	pfg-line.tex \
	pfg-parabola.tex \
	pfg-quartic.tex \
	pfg-quintic.tex \
	definitions.tex \
	theorems.tex \
	sec-intro.tex \
	sec-github.tex \
	sec-general.tex \
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
