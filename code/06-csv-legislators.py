"""
  How many active legislators have Twitter handles?
  From: https://sunlightlabs.github.io/congress/#legislator-spreadsheet

  NOTE: A mistake was made below -- it only checks how many
    Twitter IDs are in the data! Some of the legislators in
    the dataset are not currently in office.

  ANOTHER SOLUTION: 
    https://github.com/compjour/search-script-scrape/blob/master/scripts/18.py
"""

import csv

LEGISLATORS_FILE = "../datasets/06-legislators.csv"

ntwitter = 0
with open(LEGISLATORS_FILE, 'r') as fin:
    reader = csv.DictReader(fin)
    for row in reader:
        print(row['twitter_id'])
        if (row['twitter_id'] != '') and (row['twitter_id'] != None):
            ntwitter += 1

print(ntwitter)