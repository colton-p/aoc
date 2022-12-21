from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2022
DAY = 20

iobj = Input.for_date(DAY, year=YEAR, test=0)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

from dataclasses import dataclass

@dataclass
class Node:
  val: int = 0
  prev: object = None
  next: object = None

  def check(self):
    assert self.next.prev == self
    assert self.prev.next == self

  def __repr__(self):
    return f'Node(val={self.val} next={self.next.val} prev={self.prev.val})'


def insert_after(tgt, to_ins):
  to_ins.next = tgt.next
  to_ins.prev = tgt
  tgt.next.prev = to_ins
  tgt.next = to_ins

def remove(tgt):
  new_next = tgt.next
  new_prev = tgt.prev
  new_prev.next = new_next
  new_next.prev = new_prev

def walk(tgt, val):
  while val != 0:
    if val > 0:
      tgt = tgt.next
      # tgt.check()
      val -= 1
    else:
      tgt = tgt.prev
      val += 1
  
  return tgt


def make_list(node):
  l = [node.val]
  while True:
    node = node.next
    if node.val == l[0]:
      break
    l += [node.val]
  
  return l


def pprint(node):
  start = node.val
  while True:
    print(node.val, end=' ')

    node = node.next
    if node.val == start:
      break
  print('')


def move(node, val=None):
  if val is None:
    val = node.val
  if val == 0: return
  remove(node)
  tgt = walk(node, val)
  if val < 0:
    assert False
    insert_after(tgt.prev, node)
  else:
    insert_after(tgt, node)


def make_ring(orig):
  nodes = [Node(val=val) for val in orig]
  index = {node.val: node for node in nodes}

  for i in range(len(orig)):
    me = nodes[i]
    next = nodes[(i+1)%len(orig)]
    prev = nodes[i-1]

    me.next = next
    me.prev = prev
  
  return nodes, index




def part1(rows, iobj):
  orig = [811589153 * x for x in list(ll)]
  N = len(orig) - 1
  print(N)

  nodes, index = make_ring(orig)

  L = make_list(index[0])

  for i in range(10):
    for node in nodes:
      move(node, node.val % N)

  a = walk(index[0], 1000 % (N+1)).val
  b = walk(index[0], 2000 % (N+1)).val
  c = walk(index[0], 3000 % (N+1)).val
  print(a, b, c)
  l = make_list(index[0])
  #print(l)
  print(l[1000], l[2000], l[3000])

  return a + b + c

  L = list(ll)

  for v in orig:
    ix = L.index(v)
    L = rotate_left(L, ix)
    if v < 0:
      new_ix = (len(L) + v) % len(L) + 0
    else:
      new_ix = (len(L) + v) % len(L) + 1
    L = L[:new_ix] + [v] + L[new_ix:]
    del L[0]


  ix = L.index(0)
  return sum([L[(ix + 1000) % len(L)], L[(ix + 2000) % len(L)], L[(ix + 3000) % len(L)]])

def part2(rows, iobj):

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
