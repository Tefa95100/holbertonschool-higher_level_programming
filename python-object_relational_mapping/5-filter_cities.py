#!/usr/bin/python3
"""
Script for search city by state
"""
import MySQLdb
import sys

if __name__ == "__main__":
    """
    Search city by states

    Keyword arguments:
    argument -- argument for username password and name of database
    and states search
    Return: return the response of script
    """

    username, password, database, state = sys.argv[1:5]

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=database, port=3306)

    cursor = db.cursor()

    query = """SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC;"""
    cursor.execute(query, (state,))

    cities = cursor.fetchall()
    print(", ".join([city[0] for city in cities]))

    cursor.close()
    db.close()
