#!/usr/bin/python3
""" Lists all states from the database hbtn_0e_0_usa with a name"""
import MySQLdb
import sys


if __name__ == "__main__":
    database = MySQLdb.connect(host="localhost", user=sys.argv[1],
                            passwd=sys.argv[2], db=sys.argv[3], port=3306)
    curs = database.cursor()
    curs.execute("""SELECT cities.name FROM
                cities INNER JOIN states ON states.id=cities.state_id
                WHERE states.name=%s""", (sys.argv[4],))
    rows = curs.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=", ")
    curs.close()
    database.close()
