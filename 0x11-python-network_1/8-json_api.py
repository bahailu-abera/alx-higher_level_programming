#!/usr/bin/python3
"""
Module for sending search query to a server
"""
import requests
import sys


def post_req(url, q=""):
    """
    sends a query q to a server
    """
    values = {}
    values['q'] = q
    res = requests.post(url, data=values)
    try:
        json_obj = res.json()
        if (not json_obj):
            print("No result")
        else:
            print("[{}] {}".format(json_obj.get('id'), json_obj.get('name')))
    except Exception:
        print("Not a valid JSON")


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    try:
        post_req(url, sys.argv[1])
    except IndexError:
        post_req(url)
