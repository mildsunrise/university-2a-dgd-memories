#!/bin/bash
cd "$(dirname $0)" && mkdir -p build && cd build && pdflatex -shell-escape ../main.tex < /dev/null
