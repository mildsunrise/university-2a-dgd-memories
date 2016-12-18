#!/bin/bash
set -e
cd "$(dirname $0)"

for p in 3 3-extra1 3-extra2 3-extra3; do
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
