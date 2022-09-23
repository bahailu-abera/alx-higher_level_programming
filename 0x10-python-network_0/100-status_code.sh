#!/bin/bash
# a script to print a status code
curl -s -o /dev/null -w "%{http_code}" "$1"
