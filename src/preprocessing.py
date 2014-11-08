#!/usr/bin/env python

import csv

def main():
    with open("../original_data/attendance.csv", "wb") as fh:
        c = csv.reader(fh)
        header = c.next()

        for row in c:
            for col in range(len(row)):
                # print "%s:%s" % (header[col], row[col])
                pass

if __name__ == "__main__":
    main()
