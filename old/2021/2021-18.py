from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2021
DAY = 18

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

import dataclasses

@dataclasses.dataclass
class Pair:
  x: any
  y: any
  parent: any = dataclasses.field(repr=False)

  def flat_print(self):
    s = '['
    if type(self.x) == int:
      s += str(self.x)
    else:
      s += self.x.flat_print()

    s += ','
    if type(self.y) == int:
      s += str(self.y)
    else:
      s += self.y.flat_print()
    
    s+=']'
    return s
    
  def add(self, other):
    root = Pair(self, other, None)
    root.x.parent = root
    root.y.parent = root
    return root
  
  def split(self, val):
      #return val
      return Pair(math.floor(val / 2), math.ceil(val / 2), parent=self)
    
  def incr_left(self, val):
    assert self.x is not None
    assert self.y is not None
    cur = self
    while cur.parent is not None and cur.parent.x is cur:
      cur = cur.parent
    
    if cur is None or cur.parent is None: return
    cur = cur.parent

    if type(cur.x) == int:
      cur.x += val
      return

    cur = cur.x
    while type(cur.y) == Pair:
      cur = cur.y

    cur.y += val

  def incr_right(self, val):
    assert self.x is not None
    assert self.y is not None
    cur = self
    while cur.parent is not None and cur.parent.y is cur:
      cur = cur.parent
    
    if cur is None or cur.parent is None: return
    cur = cur.parent

    if type(cur.y) == int:
      cur.y += val
      return

    cur = cur.y
    while type(cur.x) == Pair:
      cur = cur.x

    cur.x += val


  def explode(self):
    assert type(self.x) == int
    assert type(self.y) == int
    self.incr_left(self.x)
    self.incr_right(self.y)

    if self.parent.x is self:
      self.parent.x = 0
    elif self.parent.y is self:
      self.parent.y = 0
    else:
      assert False


  def explode_target(self, d=0):
    if d == 4:
      return self
    
    if type(self.x) == Pair:
      tgt = self.x.explode_target(d+1)
      if tgt: return tgt
    if type(self.y) == Pair:
      tgt = self.y.explode_target(d+1)
      if tgt: return tgt


  def do_split(self):
    if type(self.x) == int and self.x >= 10:
      self.x = self.split(self.x)
      return True
    elif type(self.x) == Pair:
      chk = self.x.do_split()
      if chk: return chk

    if type(self.y) == int and self.y >= 10:
      self.y = self.split(self.y)
      return True
    elif type(self.y) == Pair:
      chk = self.y.do_split()
      if chk: return chk


  def reduce(self, d=0):
    while True:
      tgt = self.explode_target()
      while tgt:
        tgt.explode()
        #print('expld', self.flat_print())
        tgt = self.explode_target()
      
      chk = self.do_split()
      if not chk: break
      #print('split', self.flat_print())
  
  def mag(self):
    m = 0

    if type(self.x) == int:
      mx = self.x
    else:
      mx = self.x.mag()
    if type(self.y) == int:
      my = self.y
    else:
      my = self.y.mag()
    
    return 3*mx + 2*my


@dataclasses.dataclass
class Node:
  left: Pair
  right: Pair
  val: int


def parse(ll):
  if type(ll) == int:
    return ll

  (x, y) = ll
  pair = Pair(parse(x), parse(y), parent=None) 

  if type(x) != int: pair.x.parent = pair
  if type(y) != int: pair.y.parent = pair

  return pair


def part1(rows, iobj):
  nn = [parse(eval(row)) for row in rows]

  p = nn[0]
  for a in nn[1:]:
    p = p.add(a)
    p.reduce()

  print(p)
  return p.mag()


def part2(rows, iobj):

  nn = [row for row in rows]

  m = 0
  for (x,y) in itertools.permutations(nn, 2):
    a = parse(eval(x))
    b = parse(eval(y))

    p = a.add(b)
    p.reduce()
    m = max(m, p.mag())


  return m

#util.output.pretty_answer('P1', part1(rows, iobj))
#util.output.pretty_answer('P2', part2(rows, iobj))

n = Node(None, None, 1)
print(n)
