from util import *

import collections
import itertools
import re

rows = input_rows('5.in')

def fff(row):
  s = set(row)
  return (len(s) == len(row), 1)

#grid = rows_to_grid(rows)
#rows = split_rows(rows, sep=' ')

#count = count_with_predicate(rows, fff)
#print count

rows = map(int, rows)
#print rows

c = 0
ix = 0
while ix < len(rows):

  old_ix = ix
  ix += rows[ix]

  if rows[old_ix] >= 3:
    rows[old_ix] -= 1
  else:
    rows[old_ix] += 1

  c += 1
print c

print rows
