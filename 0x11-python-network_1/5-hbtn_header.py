#!/usr/bin/python3
"""
Module for getting X-Request-Id header using the requests module
"""
import requests
import sys


def get_header(url):
    """
    gets the header of the url
    """
    response = requests.get(url)
    xr_id = response.raw.getheader("X-Request-Id")
    print(xr_id)


if __name__ == "__main__":
    url = sys.argv[1]
    get_header(url)
