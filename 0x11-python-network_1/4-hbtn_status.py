#!/usr/bin/python3
"""
Module for fetching from url using requests library
"""
import requests


def fetch(url):
    """
    fetch data from url
    """
    res = requests.get(url)
    print("Body response:")
    print("\t- type: {}".format(type(res.text)))
    print("\t- content: {}".format(res.text))


if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    fetch(url)
