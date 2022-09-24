#!/usr/bin/python3
"""
Module for posting an email to the server using requests module
"""
import requests
import sys


def post_email(url, email):
    """
    post an email to a server
    """
    values = {}
    values['email'] = email
    response = requests.post(url, data=values)
    print(response.text)


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    post_email(url, email)
