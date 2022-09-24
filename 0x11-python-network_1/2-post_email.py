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
    data = {}
    data['email'] = email
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(url) as res:
        print(res.read().decode("utf-8"))


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
