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
    cd ../../../
    rm -rf tools/
fi
