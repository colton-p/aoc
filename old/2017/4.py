from util import *

import collections
import itertools
import re

rows = input_rows('4.in')



def fff(row):
  s = set(row)
  return (len(s) == len(row), 1)

def ggg(row):
  ss = set([tuple(sorted(collections.Counter(r).items())) for r in row])
  print ss
  return (len(ss) == len(row), 1)

#grid = rows_to_grid(rows)
rows = split_rows(rows, sep=' ')

count = count_with_predicate(rows, fff)
print count

count = count_with_predicate(rows, ggg)
print count


print ggg(['abcde', 'fghij'])
print ggg(['abcde', 'edcba'])
print ggg('a ab abc abd abf abj'.split(' '))
print ggg('iiii oiii ooii oooi oooo'.split(' '))
print ggg('oiii ioii iioi iiio'.split(' '))
