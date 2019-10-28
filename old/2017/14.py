from util import *
from num_util import *

import collections
import itertools
import re
import math
import operator

#rows = input_rows('input.txt')

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

#row = split_rows(rows, sep=',')[0]
#rows = split_rows(rows, regex='([a-z]+) \((\d+)\)( -> )?(.*)?')

#L = []
#for row in rows:
#  L += []
#print max(L)

key = "nbysizxe"


def H(lengths):
  lengths = [ord(x) for x in lengths] + [17,31,73,47,23]

  L = range(256)
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

  for iii in range(64):
    for length in lengths:
      twist(ix, length)

      ix += (length + skip)
      ix %= len(L)

      skip += 1

  sparse_hash = list(L)

  dense_hash = [reduce(lambda a,b: a ^ b, x) for x in grouper(sparse_hash, 16)]

  dense_hash

  return ''.join([ "%.2x" % x for x in dense_hash])



def hash_to_bin(hashed):
  s = []
  for h in hashed:
    s += [int(x) for x in bin(int(h, 16))[2:].zfill(4)]
  return s


def f(row):
  row_key = "%s-%d" % (key, row)
  hashed = H(row_key)

  bin_rep = hash_to_bin(hashed)

  return bin_rep




G = collections.defaultdict(int)#{}


print f(0)[:8]
print f(2)[:8]

s = 0
for row in range(128):
  xxx = f(row)
  for col in range(128):
    G[(row, col)] = xxx[col]
    #s += xxx[col]

print '---'

to_visit = set([pt for pt in G if G[pt] == 1])

def adj(pt):
  for nx in util.rect_adj(pt, diag=False):
    if G[nx] == 1:
      yield nx

def s(start):
  adj_fn = lambda x: adj(x)
  goal_fn = lambda x: False
  pr = dfs(start=start, adjacent_fn=adj_fn, goal_fn=goal_fn)
  return set(pr.keys())

i = 1
while to_visit:
  start = (list(to_visit)[0])
  to_del = s(start)

 #for pt in to_del:
 #  G[pt] = 0
 #G[start] = 0

  to_visit = to_visit - to_del - set([start])
  print i, len(to_visit), len(to_del)

  i += 1





print s
