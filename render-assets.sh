#!/bin/bash
# Renders assets in a specified project directory.
# Example: ./render-assets 1A

set -e
cd "$(dirname $0)"
git submodule update --init --recursive bdf2tikz vwf2tikz

# Make sure project is checked out
ORIG="$1/project"
ASSETS="$1/assets"
git submodule update --init "$ORIG"
(cd "$ORIG"; git clean -dxf)

# Render BDF schematics
mkdir -p "$ASSETS/schematics"
for filename in $(find "$ORIG" | grep '\.bdf$'); do
  name=$(basename "$filename")
  name="${name%.*}"
  echo -e "\x1b[1mRendering schematic for $name...\x1b[m"
  python bdf2tikz/main.py "$filename" "$ASSETS/schematics/$name.tex"
done

# Render BSF symbols
mkdir -p "$ASSETS/symbols"
for filename in $(find "$ORIG" | grep '\.bsf$'); do
  name=$(basename "$filename")
  name="${name%.*}"
  echo -e "\x1b[1mRendering symbol for $name...\x1b[m"
  python bdf2tikz/main.py "$filename" "$ASSETS/symbols/$name.tex"
done

# Copy VHDL files
mkdir -p "$ASSETS/vhdl"
for filename in $(find "$ORIG" | grep '\.vhd$'); do
  name=$(basename "$filename")
  echo -e "\x1b[1mCopying VHDL for $name...\x1b[m"
  dos2unix -q -n "$filename" "$ASSETS/vhdl/$name"
done
