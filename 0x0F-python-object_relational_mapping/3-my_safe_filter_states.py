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
    sf_name = MySQLdb.escape_string(name).decode()
    sqlquery = ("""SELECT * FROM states WHERE \
    BINARY states.name='{}' ORDER BY states.id""".format(sf_name))
    cur.execute(sqlquery)
    rows = cur.fetchall()
    cur.close()

    return rows


if __name__ == "__main__":
    import sys
    argv = sys.argv

    rows = filter_by_user_input(argv[1], argv[2], argv[3], argv[4])
    for row in rows:
        print(row)
