from util import *
from num_util import *

from collections import defaultdict
from collections import Counter
import collections
import itertools
import re
import math
import operator

rows = input_rows('input.txt')

def fff(row):
  s = set(row)
  return (len(s) == len(row), 1)

C = defaultdict(int)
pc = 0

cond_func = {
  '>': operator.gt,
  '<': operator.lt,
  '>=': operator.ge,
  '<=': operator.le,
  '==': operator.eq,
  '!=': operator.ne,
  'inc': operator.add,
  'dec': operator.sub,
}


#rows = split_rows(rows, regex='([a-z]+) \((\d+)\)( -> )?(.*)?')
#grid = rows_to_grid(rows)
#rows = map(int, rows)

#count = count_with_predicate(rows, fff)
#print count

# for row in rows:
#  pass

def eat_garbage(gar):

  gar_score = -1
  cancel = False
  assert gar[0] == '<', gar
  for (i,c) in enumerate(gar):
    if cancel:
      cancel = False
      continue
    if c == '!':
      cancel=True
    elif c == '>':
      return (i+1,gar_score)
    else:
      gar_score += 1
  assert False, gar


def eat_group(group, lvl=1):
  assert group[0] == '{', group
  #print '-->', group, lvl

  ix = 1

  score = lvl
  gar_score = 0

  while ix < len(group):
    c = group[ix]

    if c == ',':
      ix += 1
      continue

    if c == '{':
      (c_score, c_size, c_gar_score) = eat_group(group[ix:], lvl+1)
      score += c_score
      gar_score += c_gar_score
      ix += c_size
    elif c == '}':
      ix += 1
      break
    elif c == '<':
      (c_size,c_gar_score) = eat_garbage(group[ix:])
      gar_score += c_gar_score
      ix += c_size

  #print '<--', group, lvl, score, ix
  return (score, ix, gar_score)





print eat_group ('{}', 1)
print eat_group ('{{{}}}', 1)
print eat_group ('{{},{}}', 1)
print eat_group('{{{},{},{{}}}}', 1)
print eat_group('{<a>,<a>}', 1)
print eat_group('{{<ab>},{<ab>},{<ab>},{<ab>}}')
print eat_group('{{<!!>},{<!!>},{<!!>},{<!!>}}')
print eat_group('{{<a!>},{<a!>},{<a!>},{<ab>}}')

#print f ('{<a>,<a>}', 0)
#print ''

#print f('{{<Ab>},{<Bb>},{<Cb>},{<Db>}}', 0)
#print f('{{<!!>},{<!!>},{<!!>},{<!!>}}', 0)
print eat_group(rows[0])


#print '----'
#print eat_group('{<>,<ab>}', 1)
##
#print eat_garbage('<!!!>>')

