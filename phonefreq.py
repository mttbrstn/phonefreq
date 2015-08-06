#!/usr/bin/env python2
"""
phonedatamine.py:

A python script for determining the most frequently accessed numbers in
AT&T mobile service exported csv files.

Run the file from your *nix command line with the csv as your argument,
and the script will return a list of phone numbers and frequency of
access.

Version 1.0
Matt Burstein
mttbrstn@gmail.com

"""
import re
import sys
import csv
import collections

file = sys.argv[1]
data = []
with open(file, 'r') as csvfile:
    full_data = csv.reader(csvfile, delimiter='|')
    for row in full_data:
        data.append(' '.join(row))

digits = []
for line in data:
    digits.append(str(re.findall('\d\d\d.\d\d\d.\d\d\d\d', line)))

freq = collections.Counter(digits)
for item in list(freq.most_common()):
    items = str(item)
    fitems = items.translate(None, '\"\'()[]')
    print re.sub(',', ':', fitems)
