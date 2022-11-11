from collections import *
from itertools import *
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 1

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

def part1(rows, iobj):

  return


def part2(rows, iobj):

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
