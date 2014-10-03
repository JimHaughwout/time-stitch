from sys import argv
import sys
import csv
import datetime

# argv[0] = script
# argv[1] = master time series
# argv[2+] = other time series
# argv[last] = target






# Get the data row count and reset to start

ts_file = open(argv[1])
ts_reader = csv.reader(ts_file)
data_row_count = len(list(ts_reader)) - 1
ts_file.seek(0)

print data_row_count

row_num = 0
for row in ts_reader:
    if row_num == 0: #Header
        print row
    else:
        print row[0]
        print type(row)
    row_num += 1