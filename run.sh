#!/bin/sh

# Shortcut for running 3n+1 game for one value (passed in as param)
if [ $1 ] && [ $1 -eq $1 2> /dev/null ] ;
then
    python game.py one $1
else
    echo 'ERROR: need an integer parameter passed in'
fi
