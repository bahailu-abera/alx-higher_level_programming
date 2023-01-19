#!/usr/bin/python3
"""
Module Cities by states
"""
import MySQLdb


def cities_list(username, password, database):
    """
    Lists all cities
    """
    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         db=database)
    cur = db.cursor()
    sqlquery = ("""SELECT cities.id, cities.name, states.name \
    FROM cities INNER JOIN states ON cities.state_id = states.id \
    ORDER BY cities.id""")
    cur.execute(sqlquery)

    rows = cur.fetchall()
    cur.close()
    db.close()

    return rows


if __name__ == "__main__":
    import sys
    argv = sys.argv

    cities = cities_list(argv[1], argv[2], argv[3])
    for city in cities:
        print(city)
