#!/usr/bin/python3
"""
Module for basic auth to github api
"""
import requests
import sys


def basic_auth(url, username, psd):
    """
    Basic auth with username and psd
    """
    res = requests.get(url, auth=(username, psd))
    print(res.json().get('id'))


if __name__ == "__main__":
    url = "https://api.github.com/user"
    username = sys.argv[1]
    password = sys.argv[2]
    basic_auth(url, username, password)
