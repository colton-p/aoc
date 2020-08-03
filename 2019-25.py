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
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def part1(rows, iobj):
  ll = list(iobj.ints())
  pp = Intcode(ll)


  todo = [
    "south",
    "take cake",
    "south",
    "west",
    "take mutex",
    "east",
    "north",
    "north",

    "west",
    "take klein bottle",
    "south",
    "east",
    "take monolith",
    "south",
    "take fuel cell",
    "west",
    "west",
    "take astrolabe",

    "east",
    "east",
    "north",
    "west",
    "north",
    "west",
    "north",
    "take tambourine",

    "south",
    "west",
    "take dark matter",
    "west",
    "inv",
    "north",
  ]

  items = [x for x in todo if x.startswith("take")]
  print(items)

  for subs in powerset(items):
    ll = list(iobj.ints())
    pp = Intcode(ll)
    for cmd in todo:
      if cmd.startswith("take") and cmd not in subs:
        continue
      print(cmd)
      pp.input += [ord(x) for x in cmd] + [10]
      pp.run()
      for c in pp.output:
        print(chr(c), end='')
      pp.output = []
      print('-' * 40)

  return


def part2(rows, iobj):

  return


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
