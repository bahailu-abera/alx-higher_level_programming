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
    sqlquery = ("""SELECT cities.id, cities.name, states.name \
    FROM cities INNER JOIN states ON cities.state_id = states.id \
    WHERE states.name='{}'
    ORDER BY cities.id""".format(sf_state_name))
    cur.execute(sqlquery)

    rows = cur.fetchall()
    cur.close()
    db.close()

    return rows


if __name__ == "__main__":
    import sys
    argv = sys.argv

    cities = cities_list(argv[1], argv[2], argv[3], argv[4])
    for city in cities:
        print(city)
