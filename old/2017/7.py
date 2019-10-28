from util import *
from num_util import *

import collections
import itertools
import re
import math

rows = input_rows('7.in')

def fff(row):
  s = set(row)
  return (len(s) == len(row), 1)

rows = split_rows(rows, regex='([a-z]+) \((\d+)\)( -> )?(.*)?')

rows = [(x,y,[i.strip() for i in z.split(',')]) for (x,y,_,z) in rows]

#print rows

G = {}
weights = {}

for (node, w, adjs) in rows:
  weights[node] = int(w)
  for adj in adjs:
    G[adj] = node

bottom =  list(set(G.values()) - set(G.keys()))[0]
print 'Part 1:', bottom

W = {}

def adj(n):
  return [child for (child, parent) in G.items() if parent == n and child != '']

def weight(n):
  if n in W:
    return W[n]

  children = adj(n)
  W[n] = sum([weight(c) for c in children]) + weights[n]
  return W[n]

print weight(bottom)


def f(n):
  print '-- (%s %d) -- ' % (n, weights[n])
  for x in adj(n):
    print x, weight(x)
  c = collections.Counter([weight(x) for x in adj(n)])
  assert len(c) == 2
  for x in adj(n):
    if c[weight(x)] == 1:
      f(x)


f(bottom)



