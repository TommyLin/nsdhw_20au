#!/usr/bin/env bash
if [ $# -lt 1 ]; then
    echo "missing file name"
elif [ $# -gt 1 ]; then
    echo "only one argument is allowed"
else
    if [ -f $1 ]; then
        line=$(cat $1 | wc -l)
        echo "$line lines in $1"
    else
        echo "$1 not found"
    fi
fi
