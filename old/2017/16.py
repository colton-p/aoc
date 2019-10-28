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

#rows = [row.split(': ') for row in rows]
#rows = [(int(x.strip()), int(y.strip())) for (x,y) in rows]

#ADJ = {}
#for (x, adjs) in rows:
#  ADJ[x] = [y.strip() for y in adjs]

#start = '0'
#adj_fn = lambda x: ADJ[x]
#goal_fn = lambda x: False

row = split_rows(rows, sep=',')[0]
#rows = split_rows(rows, regex='([a-z]+) \((\d+)\)( -> )?(.*)?')

#L = []
#for row in rows:
#  L += []
#print max(L)


def spin(L, x):
  return L[-x:] + L[:-x]

def exchange(L, a, b):
  ll = list(L)
  ll[a], ll[b] =  ll[b], ll[a]
  return ll

def partner(L, x, y):
  ll = list(L)
  a = L.index(x)
  b = L.index(y)
  ll[a], ll[b] =  ll[b], ll[a]
  return ll

L = list('abcdefghijklmnop')

def dance(L):
  for x in row:
    instr = x[0]
    args = x[1:].split('/')
    if instr == 's':
      L = spin(L, int(args[0]))
    elif instr == 'x':
      L = exchange(L, int(args[0]), int(args[1]))
    elif instr == 'p':
      L = partner(L, (args[0]), (args[1]))

  return L

d = {}

for i in xrange(100):
  print i, ''.join(L)
  d[i] = ''.join(L)
  L = dance(L)

  xxx = str(L)


print d[16]
print d[16+24]
print d[16+24*2]

print 10**9


