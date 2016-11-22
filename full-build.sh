#!/bin/bash
set -e
cd "$(dirname $0)"

for p in 2 2-extra1 2-extra2 2-extra3 2-extra4; do
  ./render-assets.sh $p
  ./build-blocks.py $p
done

rm -r build < /dev/null 2< /dev/null
mkdir build
cd build
pdflatex -shell-escape ../main.tex < /dev/null
pdflatex -shell-escape ../main.tex < /dev/null
pdflatex -shell-escape ../main.tex < /dev/null

echo "Build completed."
