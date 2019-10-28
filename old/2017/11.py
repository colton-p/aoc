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



steps = split_rows(rows, sep=',')[0]

#rows = split_rows(rows, regex='([a-z]+) \((\d+)\)( -> )?(.*)?')


pt = (0, 0)

DIR = {
'ne': (1, -1),
'sw': (-1, 1),
'n': (1, 0),
's': (-1, 0),
'nw': (0, 1),
'se': (0, -1)


}


L = []
print steps
for step in steps:
  d = DIR[step]
  pt = (pt[0] + d[0], pt[1] + d[1])
  L += [sum(pt)]

print pt
print sum(pt)
print max(L)



