#!/bin/bash

# all this does is make it executable in linux
# using a bash or (.sh) file which is basically 
# a text file

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"  # Get the directory of the script
python3 "$DIR/Clock.py"
