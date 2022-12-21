from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2022
DAY = 15

iobj = Input.for_date(DAY, year=YEAR, test=0)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def xcover(pt, dd):

  for d in range(dd+1):
    for xd in range(d+1):
      yd = d - xd

      yield vadd(pt, (xd, yd))
      yield vadd(pt, (xd, -yd))

      yield vadd(pt, (-xd, yd))
      yield vadd(pt, (-xd, -yd))
  
NNN = 2000000
      
def cover(pt, dd):

  yd = abs(pt[1] - NNN )

  if yd > dd:
    return

  for xd in range(0, dd-yd+1):
    yield vadd(pt, (xd, NNN-pt[1]))
    yield vadd(pt, (-xd,NNN-pt[1]))



def part1(rows, iobj):
  return
  L = []

  for row in rows:
    (x0, y0, x1, y1) = ints(row)

    L += [ ( (x0, y0), (x1, y1))]

  #for mark in sorted(set(cover((8, 7), 9))):
  #  print(mark)
  
  EX = {}
  for (pt, sensor) in L:
    dd = util.vdist1(pt, sensor)
    print(pt, dd, sum(EX.values()))
    for mark in cover(pt, dd):
      assert mark[1] == NNN
      EX[mark] = 1
      assert vdist1(mark, pt) <= dd

  for (pt, sen) in L:
    EX[pt] = 0
    EX[sen] = 0

  return sum(EX.values())



  return

MAX = 4_000_000

def bounds(pt, dd, tgt):
  yd = abs(pt[1] - tgt)

  if yd > dd:
    return
  
  xd = dd - yd

  return Interval(max(0, pt[0] - xd), min(MAX, pt[0] + xd))

class Interval:
  def __init__(self, left, right):
    self.left = left
    self.right = right
  
  def overlaps(self, other):
    if self.left <= other.left:
      return self.right >= other.left
    else:
      return other.right >= self.left
    
  def __str__(self):
    return '(%d, %d)' % (self.left, self.right)
  
  def __repr__(self):
    return str(self)

  def union(self, other):
    assert self.overlaps(other)

    return Interval(min(self.left, other.left), max(self.right, other.right))


class ISet:
  def __init__(self, ii):
    self.ii = ii
  
  def __repr__(self):
    return ' '.join([str(i) for i in self.ii])
  
  def check(self):
    if len(self.ii) == 1:
      return self.ii[0].left == 0 and self.ii[0].right == MAX
    
    for (a,b) in each_cons(self.ii):
      if a.right + 1 == b.left:
        return True
    
    return False
  
  def union(self, ival):

    keep = [ii for ii in self.ii if not ii.overlaps(ival)]

    to_merge = sorted([ii for ii in self.ii if ii.overlaps(ival)], key=lambda x:x.left)

    if to_merge:
      merged = to_merge[0].union(ival)
      for m in to_merge[1:]:
        merged = merged.union(m)
      return ISet(keep + [merged])
    else:
      return ISet(keep + [ival])


def part2(rows, iobj):
  L = []

  for row in rows:
    (x0, y0, x1, y1) = ints(row)

    L += [ ( (x0, y0), (x1, y1), vdist1((x0, y0), (x1, y1)))]
  
  for TGT in range(1_300_000, MAX+1):
    if TGT % 1000 == 0:
      print(TGT)
    iset = ISet([])
    for (pt, _ , dd) in L:
        r = (bounds(pt, dd, TGT))
        if not r: continue

        iset = iset.union(r)
    
    if not iset.check():
      print('------------')
      print(TGT, iset)
      return

  return


  for (x,y) in its.product(range(20), repeat=2):
    chk = (x,y)

    if any(vdist1(pt, chk) <= dd for (pt, _, dd) in L):
      continue
    else:
      print(x,y)





  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
