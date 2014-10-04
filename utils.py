import sys
from sys import argv
import datetime
import csv
import dateutil.parser

def excel_to_unix(s):
    # 22590 * 86400
    try:
        return 86400 * float(s) - 2209161600.0  
    except:
        sys.exit("Could not convert %r to unix seconds." % s)


def ts_convert(ts):
    try:
        return datetime.datetime.fromtimestamp(excel_to_unix(float(ts)))
    except:
        sys.exit("Could not convert %r to unix ts." % ts)


def check_usage(arguments):
    '''
    Tedious check usage function
    '''

    num_args = len(arguments)
    last_arg = arguments[num_args - 1]
    num_files = num_args - 2
    file_list = []

    # Too few args
    if len(arguments) < 3: 
        usage = "Usage: %s ts_data_1.csv ... col_num_ts" % arguments[0]
        error = "You passed %d argument(s)." % num_args
        sys.exit("%s -- %s" % (usage, error))

    # Last arg is not an int
    try:
        ts_col_num = int(last_arg) - 1 # First column is Zero, not One
    except:
        usage = "Usage: %s ts_data_1.csv ... col_num_ts" % arguments[0]
        error = "Last argument (%r) is not an int." % last_arg
        sys.exit("%s -- %s" % (usage, error))

    for file_num in range(1, num_files + 1):
        this_file = arguments[file_num]
        if '.csv' not in arguments[file_num]:
            usage = "Usage: %s ts_data_1.csv ... col_num_ts" % arguments[0]
            error = "You passed %r for a ts_data_file." % this_file
            sys.exit("%s -- %s" % (usage, error))
        file_list.append(this_file)

    return ts_col_num, file_list


def build_ts_list(file_list, ts_column):
    '''
    Get times, return a ts_list
    '''
    #print file_list
    #print ts_column

    ts_list = []

    for this_file in file_list:
        #print "File: %s" % this_file
        #print ts_list
        #print "\n"
        source = open(this_file)
        reader = csv.reader(source)
        row_num = 0
        for row in reader:
            # Skip the header
            if row_num == 0:
                pass
            # Do not add duplicates to ts_list
            elif row[ts_column] in ts_list:
                print "%s is a dup" % row[ts_column] # DEBUG
            # Add new ts values to the list. Abort if not convertable to datetime
            else:
                try:
                    ts_list.append(dateutil.parser.parse(row[ts_column]))
                except:
                    error = "Could not convert %r to <type 'datetime.datetime'>" % row[ts_column]
                    sys.exit("%s" % error)
            row_num += 1
        source.closed
        ts_list.sort()
    return ts_list


def find_ts_bands(ts_list):
    '''
    Determine find_ts_bands
    '''
    print "\nfinding bands..."
    band_size = 600.0 # seconds
    last_band_start = ts_list[0] - datetime.timedelta(seconds=(band_size + 1))
    #print last_band_start, type(last_band_start)
    for ts in ts_list:
        delta = ts - last_band_start
        if delta.total_seconds() > band_size:
            print ts, "New Band"
            last_band_start = ts
        else:
            print ts, "Continuing Band"





print "Starting..."
ts_column, file_list = check_usage(sys.argv)
print "Timestamps in column[%d], file list is %s." % (ts_column, file_list)
ts_list = build_ts_list(file_list, ts_column)
print "We have %d unique timestamps:" % len(ts_list)
for ts in ts_list:
    #x = dateutil.parser.parse(ts)
    print ts
find_ts_bands(ts_list)

