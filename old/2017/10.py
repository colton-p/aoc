from util import *
from num_util import *

from collections import defaultdict
from collections import Counter
import collections
import itertools
import re
import math
import operator


  




lengths = [3, 4, 1, 5]
L = [0, 1, 2, 3, 4]

ix = 0
skip = 0

def circle_ixs(ix, size):
  return [(ix + i) % len (L) for i in range(size)]

def sublist(ix, size):
  ixs = circle_ixs(ix, size)

  return [L[i] for i in ixs]


def assign_sublist(ix, size, src):
  ixs = circle_ixs(ix, size)

  for (i,j) in enumerate(ixs):
    L[j] = src[i]

def twist(ix, size):
  m = list(reversed(sublist(ix, size)))

  assign_sublist(ix, size, m)

lengths = '46,41,212,83,1,255,157,65,139,52,39,254,2,86,0,204'

lengths = [ord(x) for x in lengths] + [17,31,73,47,23]

L = range(256)

for iii in range(64):
  for length in lengths:
    twist(ix, length)

    ix += (length + skip)
    ix %= len(L)

    skip += 1

sparse_hash = list(L)

dense_hash = [reduce(lambda a,b: a ^ b, x) for x in grouper(sparse_hash, 16)]

print dense_hash

print ''.join([ "%.2x" % x for x in dense_hash])


print ''
print L[0] * L[1]
