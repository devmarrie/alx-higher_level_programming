#!/usr/bin/python3
"""
Displays all values in the states table of the database hbtn_0e_0_usa
whose name matches that supplied as argument.
Safe from SQL injections.
Usage: ./3-my_safe_filter_states.py <mysql username> \
                                    <mysql password> \
                                    <database name> \
                                    <state name searched>
"""
import sys 
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3], charset="utf8")
    curr = conn.cursor()
    curr.execute("SELECT * FROM states WHERE name = '%s' ORDER BY id ASC",(sys.argv[4]))
    rows = curr.fetchall()
    for row in rows:
        print(row)
    curr.close()
    conn.close()