from util import *

import collections
import itertools
import re

rows = input_rows('input.txt')

def fff(row):
  s = set(row)
  return (len(s) == len(row), 1)

#grid = rows_to_grid(rows)
rows = split_rows(rows, sep='\t')[0]
rows = map(int ,rows)

#count = count_with_predicate(rows, fff)
#print count

print rows

l = (0,2,7,0)
l = tuple(rows)

s = {}
s[l] = 0

def f(l):
  m = max(l)
  ix = l.index(m)

  ll = list(l)
  ll[ix] = 0
  while m > 0:
    for i in itertools.chain(range(ix+1, len(l)), range(ix+1)):
      if m > 0:
        ll[i] += 1
        m -= 1
  return tuple(ll)

c = 0
while True:
  l = f(l)
  c+=1
  if l in s:
    print s[l], c
    print c - s[l]
    break
  s[l] = c

print c

