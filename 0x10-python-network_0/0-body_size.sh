#!/bin/bash
# a script to display http response body length
curl -sI "$1" | grep -i content-length | grep -Eo "[0-9]+"
