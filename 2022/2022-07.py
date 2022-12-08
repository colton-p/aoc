from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2022
DAY = 7

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

import dataclasses
@dataclasses.dataclass
class Node:
  name: str
  parent: object
  children: dict = dataclasses.field(default_factory=dict)
  size: int = 0
  total_size: int = 0

def run(rows):
  blocks = []

  block = None
  for line in rows:
    if line.startswith('$'):
      blocks += [block]
      block = [line]
    else:
      block += [line]
  blocks += [block]

  ROOT = Node(name='', children={}, parent=None)
  pwd = None
  paths = {'/': ROOT}

  for block in blocks[1:]:
    inst = block[0].strip()
    if inst == '$ cd /':
      pwd = ROOT
    elif inst == '$ cd ..':
      pwd = pwd.parent
    elif inst.startswith('$ cd'):
      tgt = inst.split(' ')[-1]
      pwd = pwd.children[tgt]

    if inst.startswith('$ cd'): continue
    
    assert inst.startswith('$ ls')

    children = {}
    for c_line in block[1:]:
      if c_line.startswith('dir'):
        (_, f_name) = c_line.split(' ')
        size = 0
      else:
        (size, f_name) = c_line.split(' ')
        size = int(size)

      new_path = pwd.name + "/" + f_name
      new_node = Node(name=pwd.name + "/" + f_name, parent=pwd, size=size)
      paths[new_path] = new_node
      children[f_name] = new_node
      pwd.children = pwd.children | children

  def desc(n):
    s = 0

    for c in n.children.values():
      s += desc(c)

    n.total_size = s + n.size
    return s + n.size

  desc(ROOT)
  return paths

def part1(rows, iobj):
  paths = run(rows)

  return sum([x.total_size for x in paths.values() if x.size == 0 and x.total_size <= 100_000])

def part2(rows, iobj):
  paths = run(rows)

  total = 70000000
  root = paths['/']
  used = root.total_size
  avail = total - used
  need = 30_000_000 - avail
  print('need', need)

  return min([x.total_size for x in paths.values() if x.total_size >= need and x.size == 0])



util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
