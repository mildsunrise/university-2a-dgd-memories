#!/bin/bash
mkdir -p build && cd build && pdflatex -shell-escape ../main.tex < /dev/null
