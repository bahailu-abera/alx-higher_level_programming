#!/usr/bin/python3
"""
Module for sending request and handling error
"""
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import sys


def send_request(url):
    """
    sends a request to the url
    """
    try:
        with urlopen(url) as res:
            body = res.read()
            print(body.decode('utf-8'))
    except HTTPError as e:
        print("Error code: {}".format(e.code))


if __name__ == "__main__":
    url = sys.argv[1]
    send_request(url)
