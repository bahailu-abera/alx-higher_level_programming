#!/usr/bin/python3
"""
Module for listing github commits
"""
import requests
import sys


def list_commits(url, repo_name, user_name):
    """
    lists a resent top 10 commits of a user from the repo repo_name
    """
    full_url = url + '/' + user_name + '/' + repo_name + '/commits'
    res = requests.get(full_url)
    for js in res.json()[:10]:
        print(js['sha'], end="")
        print(" :", js['commit']['author']['name'])


if __name__ == "__main__":
    url = "https://api.github.com/repos"
    repo_name = sys.argv[1]
    user_name = sys.argv[2]
    list_commits(url, repo_name, user_name)
