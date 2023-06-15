#!/bin/bash
if [ ! -f ./claat ]  # if claat tool doesn't exist then download and setup
then
    sudo apt install golang
    git clone --depth 1 git@github.com:googlecodelabs/tools.git
    cd tools/claat/
    go get ./
    make
    cd bin/
    mv claat ../../../
    rm -rf tools/
fi
    
grep 'https://docs.google.com' README.md | # extract all lines with `https://docs.google.com`
    grep 'document' | # to exclude lines like the command in previous line, also search for `document` in the same line. 
    cut -d '|' -f2 | # split at `|` to separate markdown table cells
    cut -d '/' -f6 | # split at `/` to extract the file IDs
    sed 's/ *$//' | # remove any whitespace
    xargs -i ./claat export -o tmp {} # run `claat` tool for each matching line