#!/usr/bin/python3
"""
Module filter states
"""
import MySQLdb


def filter_states(username, password, database):
    """
    Listes all states with a name starting N(upper N)
    from the database
    """
    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         db=database)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE states.name LIKE 'N%' ORDER \
    BY states.id")
    rows = cur.fetchall()
    cur.close()

    return rows


if __name__ == "__main__":
    import sys
    rows = filter_states(sys.argv[1], sys.argv[2], sys.argv[3])
    for row in rows:
        print(row)
