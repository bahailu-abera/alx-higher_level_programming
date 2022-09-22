#!/bin/bash
# a script to displays the body of the response
status="$(curl -sI "$1"  | head -n 1 | cut -d " " -f 2)"

if [ "$status" = 200 ]
then
    curl "$1"
fi
