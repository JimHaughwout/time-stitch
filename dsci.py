from scipy.spatial import KDTree
import numpy as np
from sys import argv, exit

'''
One-dimensional KDTree to lookup ts with nearest value


usage = "Usage: python  %s value_to_seek optional_distance" % argv[0]
if len(argv) != 2:
    error = "You passed %d argument(s)" % len(argv)
    exit("%s\n%s" % (usage, error))
'''
try:
    lookup_value = float(argv[1])
except:
    error = "Usage Error: %r is not a number." % argv[1]
    exit("%s\n%s" % (usage, error))


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
tree = KDTree(zip(timestamp, timestamp))

print "Values are: %s" % timestamp
double_dist, index = tree.query(np.array([lookup_value, lookup_value]), 1, 0, 1)
# tree.query(lookup, 1, 0, 2, float(argv[3]))
print "Closest is %f at distance %f" % (timestamp[index], double_dist/2.0)