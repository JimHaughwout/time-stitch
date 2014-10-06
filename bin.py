from sys import argv, exit
import datetime as dt
import dateutil.parser
import random
from bisect import bisect_left
from utils import ts_diff_in_seconds as time_diff


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


def find_closest_ts(timestamp_list, seek_timestamp, max_dist=float('inf')):
    '''
    Find the timestamp that is closest to a given timestamp from a sorted list 
    of timestamps. Only returns values that fall within the optional max_dist 
    (in seconds).
    
    Note: This uses bisect.bisectl_left for the binary search. bisect_left will
    sometimes return the one index off based one how it splits the list. 
    As such we need to check the distance of the returned index vs those one 
    index higher and lower. I check both as I cannot be sure whether my 
    timestamp list is sorted ASC or DESC.
    '''
    idx = bisect_left(timestamp_list, seek_timestamp)
    
    # Return Nones if no values match
    if idx == len(timestamp_list):
        return None, None

    # Otherwise check if the timestamp (and values around it) fall within the
    # specified max_dist
    else:
        lower = max(0, idx - 1)
        upper = min(idx + 1, len(timestamp_list) - 1)
        closest_timestamp = min(timestamp_list[lower:upper+1], \
            key=lambda x:time_diff(x, seek_timestamp))
        distance = time_diff(closest_timestamp, seek_timestamp)
        if distance <= max_dist:
            return closest_timestamp, distance
        else:
            return None, None


# Create and print timepoint list
list_len = 15
time_pts = built_test_ts_list(list_len, 300, 500)
print "Points:"
for idx in xrange(0, len(time_pts)):
    print "\t%4d:\t%s" % (idx, time_pts[idx])

# Get a time to seek
seek_ts = dt.datetime.now() +\
 dt.timedelta(seconds=random.uniform(300, 500*list_len))
print "\nSeeking:\t%s" % seek_ts

# Find it
closest_ts, diff_sec = find_closest_ts(time_pts, seek_ts)
if closest_ts == None:
    print "No match found"
else:
    print "Closest point:\t%s, %f seconds away." % (closest_ts, diff_sec)
