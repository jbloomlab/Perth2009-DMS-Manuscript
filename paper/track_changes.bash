#!/bin/bash

# make track changes version

# path on Jesse's laptop
PDFLATEX="/Library/TeX/texbin/pdflatex"

TRACKCHANGES="manuscript_trackchanges"

latexdiff manuscript_PNAS_original_submission.tex manuscript.tex > $TRACKCHANGES.tex
$PDFLATEX $TRACKCHANGES
bibtex $TRACKCHANGES
$PDFLATEX $TRACKCHANGES
$PDFLATEX $TRACKCHANGES
