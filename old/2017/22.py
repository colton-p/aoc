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

grid2 = rows_to_grid(rows)
#rows = map(int, rows)

#count = count_with_predicate(rows, fff)
#print count

#rows = [(int(x.strip()), int(y.strip())) for (x,y) in rows]


#rows = [row.split(': ') for row in rows]
#ADJ = {}
#for (x, adjs) in rows:
#  ADJ[x] = [y.strip() for y in adjs]

#start = '0'
#adj_fn = lambda x: ADJ[x]
#goal_fn = lambda x: False

#row = split_rows(rows, sep=',')[0]

#grid2 = rows_to_grid(['..#', '#..', '...'])
print_grid(grid2)

[ (-1,0), (0, -1), (1, 0), (0, 1)]

def left(dd):
  (dx, dy) = dd
  return (-dy, dx)

def right(dd):
  (dx, dy) = dd
  return (dy, -dx)

print (math.sqrt(len(grid2)))
start = int((math.sqrt(len(grid2))) / 2)


pt = (start, start)
dd = (-1, 0)
c = 0

print dd, right(dd), right(right(dd)), right(right(right(dd))), right(right(right(right(dd))))
print dd, left(dd), left(left(dd)), left(left(left(dd))), left(left(left(left(dd))))
print '-----'


def pp(grid, pt):
  pgrid = collections.defaultdict(lambda : '.')
  pgrid.update(grid)
  if grid[pt] == '.':
    pgrid[pt] = 'O'
  else:
    pgrid[pt] = 'X'
  print_grid(pgrid)

grid = collections.defaultdict(lambda : '.')
grid.update(grid2)

pp(grid,pt)


for i in range(10000000):
  if grid[pt] == '.':
    #print dd, '-->', left(dd)
    grid[pt] = 'w'
    dd = left(dd)
  elif grid[pt] == 'w':
    c += 1
    grid[pt] = '#'
  elif grid[pt] == '#':
    #print dd, '-->', right(dd)
    grid[pt] = 'f'
    dd = right(dd)
  elif grid[pt] == 'f':
    grid[pt] = '.'
    dd = right(right(dd))
  else:
    assert False, grid[pt]

  pt = tuple(map(sum, zip(pt,dd)))
  #print ''
  #pp(grid,pt)
  #print pt
  #print ''

pp(grid,pt)
print len(grid)
print ''
print c
