#!/usr/bin/env python

_input = input
from collections import *
from itertools import *
import re
import math
import operator as op

from util import *
from util.intcode import *
YEAR = 2019
DAY = 25

iobj = Input.for_date(DAY, year=YEAR, test=False)
rows = list(iobj.rows)


def parse_screen(output):
  text = ''.join(chr(c) for c in output)
  items = []
  dirs = []
  room = None
  tgt = None

  lines = [x.strip() for x in text.split('\n')]
  for line in lines:
    if line == "Doors here lead:":
      tgt = dirs
    elif line == "Items here:":
      tgt = items
    elif line.startswith('-'):
      tgt.append(line[2:])
    elif line.startswith('=='):
      room = line[3:-3]
    else:
      tgt = None

  return (room, dirs, items)


def bfs(start=None, adjacent_fn=None):
  Q = collections.deque()

  open_set = set()
  closed_set = set()

  # a dictionary to maintain meta information (used for path formation)
  meta = dict()  # key -> (parent state, action to reach child)

  # initialize
  meta[start[1]] = (None)
  open_set.add(start[1])
  Q.append(start)

  while len(Q) > 0:
    parent_state = Q.popleft()
    open_set.remove(parent_state[1])

    for (child_state,action) in adjacent_fn(parent_state):

      (pp, name, items, directions) = child_state
      if name in closed_set:
        continue

      if name not in open_set:
        meta[name] = (parent_state[1], action)

        Q.append(child_state)
        open_set.add(name)

    closed_set.add(parent_state[1])
  return meta


def adj(state):
  (orig, _name, _directions, _items) = state

  print(_name, _directions)
  for dd in _directions:
    pp = orig.fork()
    pp.input += [ord(x) for x in dd] + [10]
    pp.run()

    (name, directions, items) = parse_screen(pp.output)

    yield ((pp, name, directions, items), dd)


def part1(rows, iobj):
  ll = list(iobj.ints())
  pp = Intcode(ll)
  pp.run()

  (name, directions, items) = parse_screen(pp.output)

  state = (pp, name, directions, items)

  meta = bfs(state, adjacent_fn=adj)
  print(meta)


print('P1', part1(rows, iobj))
