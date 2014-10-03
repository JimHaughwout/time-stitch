from sys import argv
import sys
import csv

# argv[0] = script
# argv[1] = master time series
# argv[2+] = other time series
# argv[last] = target

if len(argv) < 2: # Usage guidance
    usage = "Usage: %s ts_data.csv" % argv[0]
    error = "You passed %d arguments." % len(argv)
    sys.exit("%s -- %s" % (usage, error))


if '.csv' not in argv[1]:
    usage = "Usage: %s ts_data.csv" % argv[0]
    error = "You passed %r for ts_data.csv" % argv[1]
    sys.exit("%s -- %s" % (usage, error))


# Get the data row count and reset to start

ts_file = open(argv[1])
reader = csv.reader(ts_file)
data_row_count = len(list(reader)) - 1
ts_file.seek(0)

print data_row_count