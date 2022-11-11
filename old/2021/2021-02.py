from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2021
DAY = 2

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def part1(rows, iobj):

  (h, d) = (0, 0)
  aim = 0

  for row in rows:
    if row.startswith('forward'):
      h += pints(row)[0]
      d += aim * pints(row)[0]

    if row.startswith('up'):
      aim -= pints(row)[0]

    if row.startswith('down'):
      aim += pints(row)[0]

  return h*d

def part2(rows, iobj):

  (h, d) = (0, 0)
  aim = 0
  for (cmd, val) in tt:
    if cmd == 'forward':
      h += val
      d += aim * val

    if cmd == 'up':
      aim -= val

    if cmd == 'down':
      aim += val

  return h*d

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
