#!/usr/bin/python3
"""
Module for detecting error with requests module
"""
import requests
import sys


def error_code(url):
    """
    prints the error code
    """
    response = request.get(url)
    if (response.status_code >= 400):
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    error_code(url)
