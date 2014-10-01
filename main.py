from sys import argv
import sys
import csv

# argv[0] = script
# argv[1] = master time series
# argv[2+] = other time series
# argv[last] = target
if len(argv) < 4: # Usage guidance
    usage = "Usage: %s master_ts.csv other_ts_1.csv ... other_ts_last.csv target.csv" % argv[0]
    error = "You passed %d arguments." % len(argv)
    sys.exit("%s -- %s" % (usage, error))

'''master = 
stitch =


if '.csv' not in master_ts:
    usage = "Usage: %s input_file.csv num_slices output_file.json" % argv[0]
    error = "You passed %r for input_file.csv" % source
    sys.exit("%s -- %s" % (usage, error))



# target = open(destination, 'w')
ts_master = open(source)
reader = csv.reader(data)
data_row_count = len(list(reader)) - 1
data_write_count = 0
invalid_count = 0
data.seek(0)

'''