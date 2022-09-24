#!/usr/bin/python3
"""
Module to fetch data from https://alx-intranet.hbtn.io/status
"""


def fetch(url):
    """ fetch from a URL='url'
    """
    import urllib.request as req
    with req.urlopen(url) as response:
        html = response.read()
        print('Body response:')
        print('\t- type: {}'.format(type(html)))
        print('\t- content: {}'.format(html))
        print('\t- utf8 content: {}'.format(html.decode("utf-8")))


if __name__ == "__main__":
    url = "https://intranet.hbtn.io/status"
    fetch(url)
