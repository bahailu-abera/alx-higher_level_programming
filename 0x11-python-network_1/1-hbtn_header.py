#!/usr/bin/python3
"""
Module for fetching X-Request-Id
"""
import urllib.request
import sys


def fetch(url):
    """
    prints the X-Request-Id
    """
    with urllib.request.urlopen(url) as res:
        header = res.headers
        print(header.get('X-Request-Id'))


if __name__ == "__main__":
    url = sys.argv[1]
    fetch(url)
