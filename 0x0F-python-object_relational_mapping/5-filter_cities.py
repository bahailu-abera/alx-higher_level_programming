#!/usr/bin/python3
"""
Module Cities by states
"""
import MySQLdb


def cities_list(username, password, database, state_name):
    """
    Lists all cities
    """
    db = MySQLdb.connect(host='localhost', user=username, passwd=password,
                         db=database)
    cur = db.cursor()
    sf_state_name = MySQLdb.escape_string(state_name).decode()
    sqlquery = ("""SELECT cities.name \
    FROM states INNER JOIN cities ON states.id = cities.state_id \
    WHERE states.name='{}'""".format(sf_state_name))
    cur.execute(sqlquery)

    rows = cur.fetchall()
    cur.close()
    db.close()

    return rows


if __name__ == "__main__":
    import sys
    argv = sys.argv

    cities = cities_list(argv[1], argv[2], argv[3], argv[4])
    for city in cities[:-1]:
        print(city[0], end=', ')
    print(cities[-1][0])
