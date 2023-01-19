#!/usr/bin/python3
"""
Module get all states
"""
import MySQLdb


def list_states(username: str, password: str, database: str) -> None:
    """
    lists all states
    """
    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id;")
    rows = cur.fetchall()
    cur.close()
    return rows


if __name__ == "__main__":
    import sys
    from pprint import pprint
    argv = sys.argv
    rows = list_states(argv[1], argv[2], argv[3])
    for row in rows:
        print(row)
