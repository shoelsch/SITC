#!/usr/bin/env python

import os
import csv
import re
from collections import Counter

PRIVATE_PATH = "../../data/private/"
PUBLIC_PATH = "../../data/public/"

def buildAttendance():
    id_map = dict()

    with open(PRIVATE_PATH + "withheld.csv", "rb") as inp:
        cr = csv.reader(inp)
        cr.next()
        for row in cr:
            uid, first, last = row[0], row[1], row[2]
            id_map[(first,last)] = uid


    seen = list()

    with open(PUBLIC_PATH + "csv/attendance-2014.csv", "wb") as out:
        cw = csv.writer(out)
        cw.writerow(['ID', '6/24/2014', '6/25/2014', '6/26/2014', '6/27/2014', '7/1/2014', '7/2/2014', '7/3/2014', '7/8/2014', '7/9/2014', '7/10/2014', '7/11/2014', '7/15/2014', '7/16/2014', '7/17/2014', '7/18/2014', '7/22/2014', '7/23/2014', '7/24/2014', '7/25/2014', '7/29/2014', '7/30/2014', '7/31/2014', '8/1/2014', '8/5/2014', '8/6/2014', '8/7/2014', '8/8/2014', '8/12/2014', '8/13/2014', '8/14/2014', '8/15/2014'])
        with open(PRIVATE_PATH + "attendance-2014.csv", "rb") as inp:
            cr = csv.reader(inp)
            for row in cr:
                first, last = row[0].lower(), row[1].lower()
                if first and last:
                    try:                    
                        attendance = [id_map[(first,last)]]
                        for col in range(2,33):
                            attendance.append(row[col])
                        cw.writerow(attendance)
                    except:
                        print "Key Error: " + first + " " + last

def buildVolunteers():
    SEEN = list()
    FILES = ["volunteers-2014.csv", "volunteers-2013.csv"]
    uid = 0

    with open(PRIVATE_PATH + "withheld.csv", "wb") as out_private:
        cw_private = csv.writer(out_private)
        cw_private.writerow(["ID", "FIRST", "LAST", "EMAIL", "PHONE"])
        with open(PUBLIC_PATH + "csv/volunteers.csv", "w") as out_public:
            cw_public = csv.writer(out_public)
            cw_public.writerow(["ID", "YEAR", "DOB", "GENDER", "ADDRESS", "CITY", "STATE", "ZIPCODE", "ETHNICITY", "RELIGION", "HIGHSCHOOL", "GRAD_YEAR", "COLLEGE", "CARPOOL", "VOLUNTEERED", "VOLUNTEER_YEARS"])
            for f in FILES:
                year = f.split("-")[1].split(".")[0]
                with open(PRIVATE_PATH + f, "rU") as inp:
                    cr = csv.reader(inp)
                    cr.next()
                    for row in cr:
                        first, last = row[0].lower(), row[1].lower()
                        email, phone = row[2].lower(), row[5]
                        dob, gender = row[3], row[4].lower()
                        address, city, state, zipcode = row[6].lower(), row[7].lower(), row[8].lower(), row[9]
                        ethnicity, religion = row[10].replace("<i>", "").replace("</i>", ""), row[11]
                        highschool, gradyear, college = row[13].lower(), row[14], row[15].lower()
                        carpool = row[16]
                        
                        if re.match("^yes", row[12].lower()):
                            past = "Yes"
                            results = re.search("(\d)", row[12].lower())
                            pastYears = results.group(0)
                        else:
                            past, pastYears = "No", 0
                        
                        if (first, last) not in SEEN and first and last:
                            address = re.sub('^[0-9]*\S*', '', re.sub('#*[0-9]*$', '', address))
            
            
                            SEEN.append((first,last))
                            cw_private.writerow([uid, first, last, email, phone])
                            cw_public.writerow([uid, year, dob, gender, address, city, state, zipcode, ethnicity, religion, highschool, gradyear, college, carpool, past, pastYears,])
                            
                            uid += 1

if __name__ == "__main__":
    buildVolunteers()
    buildAttendance()
