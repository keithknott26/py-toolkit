#!/usr/bin/env python

"""Demo file reading CSV file."""

import csv

from dateutil.parser import parse
from datetime import date


CSV_FILE = "./input/sample1.csv"

print("Reading data from the CSV ...")
with open(CSV_FILE, 'r') as f:
    csv_reader = csv.reader(f)
    next(csv_reader)
    for row in csv_reader:
        print(row)
        # example of reading few fields
        firstname = row[0]
        lastname = row[1]
        dob = parse(row[3])
        age = date.today().year - dob.year
        print("Patient {0} {1}, Age {2}".format(firstname, lastname, age))
        print "Test"