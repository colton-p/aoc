from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output
import util.grid2

YEAR = 2022
DAY = 14

iobj = Input.for_date(DAY, year=YEAR, test=1)
iobj.peek()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()


def split_scans(rows):
  for row in rows:
    coords = ints(row)

    pts = list(each_slice(coords))

    for line in each_cons(pts):
      yield line
  
def line_to_pts(line):
  (a, b) = line
  dd = vsub(b, a)
  assert 0 in dd
  dd = vscale(dd, 1/abs(sum(dd)))
  dd = list(map(int, dd))

  x = tuple(a)
  while x != b:
    yield x
    x = vadd(x, dd)
  yield b

def drop_sand(G):
  pt = (500, 0)

  while pt[1] < 2000:
    down = vadd(pt, DIR.DOWN)
    down_left = vadd(vadd(pt, DIR.DOWN), DIR.LEFT)
    down_right = vadd(vadd(pt, DIR.DOWN), DIR.RIGHT)

    if G[down] == '.':
      pt = down
    elif G[down_left] == '.':
      pt = down_left
    elif G[down_right] == '.':
      pt = down_right
    else:
      return pt
  return None

  

def part1(rows, iobj):

  G = defaultdict(lambda: '.')
  for line in split_scans(rows):
    for pt in line_to_pts(line):
      G[pt] = '#'

  gg = util.grid2.OpenGrid(G)

  max_y = gg.max_y() + 2

  skew = 2000
  for x in range(500 - skew, 500 + skew):
    G[(x, max_y)] = '#'
  print(max_y)

  #gg = util.grid2.OpenGrid(G)
  #print(gg.to_s(cell_size=1))

  x = True
  c = 0
  while x != (500, 0):
    x = drop_sand(G)
    c += 1
    print(c, x)

    if x is not None:
      G[x] = 'o'
    
  gg = util.grid2.OpenGrid(G)
  #print(gg.to_s(cell_size=1))


  return c - 1, gg.count('o')

def part2(rows, iobj):

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
