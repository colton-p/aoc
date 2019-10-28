from util import *
from num_util import *

import collections
import itertools
import re
import math
import operator

rows = input_rows('input.txt')

def fff(row):
  s = set(row)
  return (len(s) == len(row), 1)

#grid = rows_to_grid(rows)
#rows = map(int, rows)

#count = count_with_predicate(rows, fff)
#print count

# c = 0
# for row in rows:


# print c

C = collections.defaultdict(int)
cond_func = {
  '>': operator.gt,
  '<': operator.lt,
  '>=': operator.ge,
  '<=': operator.le,
  '==': operator.eq,
  '!=': operator.ne,
}

rows = [row.split(': ') for row in rows]
rows = [(int(x.strip()), int(y.strip())) for (x,y) in rows]

#ADJ = {}
#for (x, adjs) in rows:
#  ADJ[x] = [y.strip() for y in adjs]

#start = '0'
#adj_fn = lambda x: ADJ[x]
#goal_fn = lambda x: False

#row = split_rows(rows, sep=',')[0]
#rows = split_rows(rows, regex='([a-z]+) \((\d+)\)( -> )?(.*)?')

#L = []
#for row in rows:
#  L += []
#print max(L)


depth = dict(rows)

#depth = {0: 3, 1: 2, 4:4, 6:4}

def go(delay):
  sev = 0
  for t in range(max(depth.keys())+1):
    if t in depth:
      #print t, depth[t]
      if (t+delay) % (depth[t]*2-2) == 0:
        return False
        sev += (depth[t]*t)
  return True

def go2(delay):
  return list(((0+delay) % (dd*2-2)) for (t,dd) in depth.iteritems())

def go3(delay):
  return list(((t+delay) % (dd*2-2)) for (t,dd) in depth.iteritems())



print 'M', list((dd*2-2) for (t,dd) in depth.iteritems())
print 't', list(((t+0) % (dd*2-2)) for (t,dd) in depth.iteritems())
print 'd', go2(3941460)
print 'x', go3(3941460)

i=0
while not go2(i):
  i += 1
print i

#print rows
for i in range(1,10):#000000):
  x = go(i)
  if x:
    print '------'
    print i
    break
