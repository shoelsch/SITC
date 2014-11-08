#!/usr/bin/env python

import csv
import json
import re

def main():
    seen = list()

    with open("../data/private/volunteers.csv", "rU") as inp:
        cr = csv.reader(inp)
        cr.next()
        
        with open("../data/private/withheld.csv", "wb") as out_private:
            cw_private = csv.writer(out_private)
            cw_private.writerow(["ID", "FIRST", "LAST", "EMAIL", "PHONE"])
            with open("../data/public/csv/volunteers.csv", "wb") as out_public:
                cw_public = csv.writer(out_public)
                cw_public.writerow(["ID", "DOB", "GENDER", "ADDRESS", "CITY", "STATE", "ZIPCODE", "ETHNICITY", "RELIGION", "HIGHSCHOOL", "GRAD_YEAR", "COLLEGE", "CARPOOL", "VOLUNTEERED", "VOLUNTEER_YEARS"])
                                    
                uid = 0
                
                for row in cr:
                    first, last = row[0].lower(), row[1].lower()
                    email, phone = row[2].lower(), row[5]
                    dob, gender = row[3], row[4].lower()
                    address, city, state, zipcode = row[8].lower(), row[10].lower(), row[11].lower(), row[12]
                    ethnicity, religion = row[14].replace("<i>", "").replace("</i>", ""), row[15]
                    highschool, gradyear, college = row[17].lower(), row[18], row[19].lower()
                    carpool = row[20]
                    
                    if re.match(r"^yes", row[16].lower()):
                        past = "Yes"
                        results = re.search(r"(\d)", row[16].lower())
                        pastYears = results.group(0)
                    else:
                        past, pastYears = "No", 0
                    
                    if (first, last) not in seen:
                        seen.append((first,last))
                        cw_private.writerow([uid, first, last, email, phone])
                        cw_public.writerow([uid, dob, gender, address, city, state, zipcode, ethnicity, religion, highschool, gradyear, college, carpool, past, pastYears,])
                        
                        uid += 1

if __name__ == "__main__":
    main()
