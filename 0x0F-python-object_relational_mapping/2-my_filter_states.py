#!/usr/bin/python3
"""
Module filter by user input
"""
import MySQLdb


def filter_by_user_input(username, password, database, name):
    """
    Script that takes in an argument and displays all values
    in the states table of database where name matches the argument
    """
    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name = %s \
    ORDER BY states.id", (name, ))
    rows = cur.fetchall()

    return rows


if __name__ == "__main__":
    import sys
    argv = sys.argv

    rows = filter_by_user_input(argv[1], argv[2], argv[3], argv[4])
    for row in rows:
        print(row)