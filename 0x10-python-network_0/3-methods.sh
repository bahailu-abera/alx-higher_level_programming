#!/bin/bash
# send delete request with curl
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
