from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2021
DAY = 22

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def part1(rows, iobj):

  G = defaultdict(int)
  for row in rows:
    rr = ints(row)
    op = row.split(' ')[0]

    x0 = max(-50, rr[0])
    x1 = min(50, rr[1])

    y0 = max(-50, rr[2])
    y1 = min(50, rr[3])

    z0 = max(-50, rr[4])
    z1 = min(50, rr[5])

    for pt in itertools.product(range(x0,x1+1), range(y0,y1+1), range(z0,z1+1)):
      if op == 'off':
        G[pt] = 0
      else:
        G[pt] = 1

  return sum(G.values())

def vol(rr):
  (x0, x1, y0, y1, z0, z1) = rr

  return (1+x1- x0)*(1+y1-y0)*(1+z1-z0)

def within(smol, big):
  (a_x0, a_x1, a_y0, a_y1, a_z0, a_z1) = smol
  (b_x0, b_x1, b_y0, b_y1, b_z0, b_z1) = big

  return (
    a_x0 >= b_x0 and a_x1 <= b_x1 and
    a_y0 >= b_y0 and a_y1 <= b_y1 and
    a_z0 >= b_z0 and a_z1 <= b_z1
  )
  #if b_x0 >= a_x1 or a_x0 >= b_x1 or b_y0 >= a_y1 or a_y0 >= b_y1:# or b_z0 >= a_z1 or a_z0 >= b_z1:
  if b_x0 > a_x1 or a_x0 > b_x1 or b_y0 > a_y1 or a_y0 > b_y1 or b_z0 > a_z1 or a_z0 > b_z1:
    return False
  return True

def overlap_pts(p1, p2):
  (a_x0, a_x1, a_y0, a_y1, a_z0, a_z1) = p1
  (b_x0, b_x1, b_y0, b_y1, b_z0, b_z1) = p2

  if b_x0 > a_x1 or a_x0 > b_x1 or b_y0 > a_y1 or a_y0 > b_y1 or b_z0 > a_z1 or a_z0 > b_z1:
    return None

  left = min((a_x0, a_x1), (b_x0, b_x1))
  right = max((a_x0, a_x1), (b_x0, b_x1))

  left_x = min(left[0], right[0])  
  start_x = max(left[0], right[0])
  end_x = min(left[1], right[1])
  right_x = max(left[1], right[1])  

  left = min((a_y0, a_y1), (b_y0, b_y1))
  right = max((a_y0, a_y1), (b_y0, b_y1))
  left_y = min(left[0], right[0])  
  start_y = max(left[0], right[0])
  end_y = min(left[1], right[1])
  right_y = max(left[1], right[1])  

  left = min((a_z0, a_z1), (b_z0, b_z1))
  right = max((a_z0, a_z1), (b_z0, b_z1))
  left_z = min(left[0], right[0])  
  start_z = max(left[0], right[0])
  end_z = min(left[1], right[1])
  right_z = max(left[1], right[1])  

  new_cubes = itertools.product(
    [(left_x, start_x-1), (+start_x, end_x), (1+end_x, right_x)],
    [(left_y, start_y-1), (+start_y, end_y), (1+end_y, right_y)],
    [(left_z, start_z-1), (+start_z, end_z), (1+end_z, right_z)],
  )

  r = defaultdict(list)
  for v in new_cubes:
    if v[2][0] > v[2][1]: continue
    vv = tuple(itertools.chain(*v)) 
    if within(vv, p1) and within(vv, p2): 
      r['both'] += [vv]
    elif within(vv, p1):
      r['a'] += [vv]
    elif within(vv, p2):
      r['b'] += [vv]

  return r

def add(cubes, new):

  to_del = set()
  to_add = set()
  for old in cubes:
    r = overlap_pts(old, new)
    if not r: continue

    to_del.add(old)
    to_add |= set(r['a'])
    to_add |= set(r['both'])
    to_add |= set(r['b'])
  
  return cubes 
  return (to_add, to_del)

import dataclasses
@dataclasses.dataclass(frozen=False)
class Cube:
  x: any
  y: any
  z: any
  ind: int

  def vol(self):
    (x0, x1) = self.x
    (y0, y1) = self.y
    (z0, z1) = self.z
    return self.ind * (1 + x1 - x0) * (1 + y1 - y0) * (1 + z1 - z0)
  
  def overlap(self, other):
    if max(self.x[0], other.x[0]) > min(self.x[1], other.x[1]): return None
    if max(self.y[0], other.y[0]) > min(self.y[1], other.y[1]): return None
    if max(self.z[0], other.z[0]) > min(self.z[1], other.z[1]): return None

    # -------- #
        # ------------ #

    if other.ind == 1:
      ind = -1
    else:
      ind = 1

    return Cube(
      (max(self.x[0], other.x[0]), min(self.x[1], other.x[1])),
      (max(self.y[0], other.y[0]), min(self.y[1], other.y[1])),
      (max(self.z[0], other.z[0]), min(self.z[1], other.z[1])),
      ind=1,
    )


def part2(rows, iobj):
  C = 0

  all_cubes = []
  for row in rows:
    (x0, x1, y0, y1, z0, z1) = ints(row)
    ind = row.split(' ')[0] == 'on' and 1 or -1
    all_cubes += [Cube((x0, x1), (y0, y1), (z0, z1), ind=ind)]

  cubes = [all_cubes[0]]

  for b in all_cubes[1:]:
    print('b', b)
    for a in cubes.copy():
      c = b.overlap(a)
      if c:
        if a.ind == 1:
          c.ind = -1
        cubes += [c]
    if b.ind == 1:
      cubes += [b]


  #for cube in cubes:
  #  print(cube.vol(), cube)

  return sum(cube.vol() for cube in cubes)

#util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
