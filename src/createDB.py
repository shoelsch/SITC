#!/usr/bin/env python

import sys
import sqlite3 as sqlite

def main():
    with sqlite.connect("attendance.db") as con:
        cur = con.cursor()

        # Create a volunteers table
        tbl_name = "volunteers"
        sql = "DROP TABLE IF EXISTS %s" % tbl_name
        cur.execute(sql)

if __name__ == "__main__":
    main()
