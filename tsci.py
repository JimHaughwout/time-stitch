from scipy.spatial import KDTree
import numpy as np
from sys import argv, exit
import datetime as dt
import dateutil.parser
import random

'''
One-dimensional KDTree to lookup ts with nearest value


usage = "Usage: python  %s value_to_seek optional_distance" % argv[0]
if len(argv) != 2:
    error = "You passed %d argument(s)" % len(argv)
    exit("%s\n%s" % (usage, error))
'''

'''
try:
    lookup_value = float(argv[1])
except:
    error = "Usage Error: %r is not a number." % argv[1]
    exit("%s\n%s" % (usage, error))
'''

num_pts = 10
tpoint = dt.datetime.now()
tarray = np.array([])
for pt in xrange(0, num_pts):
    tpoint += dt.timedelta(seconds=random.uniform(300,500))
    # print tpoint
    tarray = np.append(tarray, np.asarray([tpoint]))




# SciPy's KDTree only works with 2+ dimensions
# So we create an identy matrix
# This will double the distance
timestamp = np.array([
    3,
    10,
    19,
    23,
    30,
    37,
    49,
    59,
    62,
    70,
    80,
    89,
    93,
    97 ])





# Build the tree
tree1 = KDTree(zip(timestamp, timestamp))
tree2 = KDTree(zip(tarray, tarray))

# print "Values are: %s" % timestamp
print "Values are: %s" % tarray

# Add one arg dist*2 if desired
# if index == len(ts) OR double_dist = float('inf') then no match
seek_time = dt.datetime.now() + dt.timedelta(seconds=random.uniform(300,4000))
print "Seeking: %s" % seek_time

print tree2.query(np.array([seek_time, seek_time]), 1, 0, 1)

'''
double_dist, index = tree.query(np.array([lookup_value, lookup_value]), 1, 0, 1)
# tree.query(lookup, 1, 0, 2, float(argv[3]))
print "Closest is %f at distance %f" % (timestamp[index], double_dist/2.0)
'''