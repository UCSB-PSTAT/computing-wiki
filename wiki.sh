#!/bin/bash
if [ ! -f ./claat-linux-amd64 ]  # if claat tool doesn't exist then download and setup
then
    wget https://github.com/googlecodelabs/tools/releases/download/v2.2.5/claat-linux-amd64
    chmod u+x claat-linux-amd64
fi
    
grep ' https://docs.google.com' README.md | # extract all lines with `https://docs.google.com`
    grep 'document' | # to exclude lines like the command in previous line, also search for `document` in the same line. 
    cut -d '|' -f2 | # split at `|` to separate markdown table cells
    cut -d '/' -f6 | # split at `/` to extract the file IDs
    sed 's/ *$//' | # remove any whitespace
    xargs -i ./claat-linux-amd64 export -o docs {} # run `claat` tool for each matching line