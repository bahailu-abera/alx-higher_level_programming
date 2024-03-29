#!/usr/bin/python3
"""
Module for posting email to a server
"""
import urllib.request
import urllib.parse
import sys


def post_email(url, email):
    """
    post an email to the specified url
    """
    values = {'email': email}
    values = urllib.parse.urlencode(values).encode('ascii')
    req = urllib.request.Request(url, data=values)
    with urllib.request.urlopen(url) as res:
        body = res.read()
        print(body.decode("utf-8").strip())


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
