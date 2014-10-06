from sys import argv, exit
import datetime as dt
import dateutil.parser
import random
from bisect import bisect_left


def built_test_ts_list(length=1, min_diff=60, max_diff=60, start_dt=None):

    if start_dt == None: 
        time_point = dt.datetime.now()
    else: 
        time_point = start_dt

    timestamp_list = []
    
    for point in xrange(0, length):
        time_point += dt.timedelta(seconds=random.uniform(min_diff, max_diff))
        timestamp_list.append(time_point)

    return timestamp_list


def ts_diff_sec(ts_1, ts_2):
    return abs((ts_1 - ts_2).total_seconds())

def find_closest_ts(timestamp_list, seek_timestamp, max_dist=float('inf')):

    idx = bisect_left(timestamp_list, seek_timestamp)
    
    if idx == len(timestamp_list):
        return None, None, None
    
    else:
        closest_timestamp = timestamp_list[idx]
        distance = ts_diff_sec(closest_timestamp, seek_timestamp)
        if distance <= max_dist:
            return closest_timestamp, idx, distance
        else:
            return None, None, None


# Create and print timepoint list
list_len = 15
time_pts = built_test_ts_list(list_len, 300, 500)
print "Points:"
for idx in xrange(0, len(time_pts)):
    print "\t%4d:\t%s" % (idx, time_pts[idx])

# Get a time to seek
seek_ts = dt.datetime.now() + dt.timedelta(seconds=random.uniform(300, 500*list_len))
print "\nSeeking:\t%s" % seek_ts

# Find it
closest_ts, index, diff_sec = find_closest_ts(time_pts, seek_ts)
if closest_ts == None:
    print "No match found"
else:
    print "Closest point:\t%s, Index: %d, %f seconds away." % (closest_ts, index, diff_sec)
    # Test it, it appears sometimes I need to jump one point back
    before = max(0, index - 1)
    after = min(len(time_pts) - 1, index + 1)
    print "Point before:\t%s, Index: %d, %f seconds away." % (time_pts[before], before, ts_diff_sec(time_pts[before], seek_ts))
    print "Point after:\t%s, Index: %d, %f seconds away." % (time_pts[after], after, ts_diff_sec(time_pts[after], seek_ts))



#print min(time_pts, key=lambda x:abs((x - seek_ts).total_seconds()))