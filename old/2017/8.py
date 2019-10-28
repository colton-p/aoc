from util import *
from num_util import *

import collections
import itertools
import re
import math
import operator

rows = input_rows('8.in')

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

REG = collections.defaultdict(int)

rows = split_rows(rows, sep=' ')

cond_func = {
  '>': operator.gt,
  '<': operator.lt,
  '>=': operator.ge,
  '<=': operator.le,
  '==': operator.eq,
  '!=': operator.ne,
}

val = 0

for row in rows:
  var = row[0]
  inst = row[1]
  op = int(row[2])

  var2 = row[4]
  cond_sym = row[5]
  op2 = int(row[6])

  if inst == 'inc':
    f = operator.add
  elif inst == 'dec':
    f = operator.sub
  else:
    assert False, inst

  if cond_func[cond_sym](REG[var2], int(op2)):
    REG[var] = f(REG[var], int(op))
    val = max(val, max(REG.values()))

print max(REG.values())
print val
