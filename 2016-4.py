#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2016
DAY = 4

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)


def part1(rows, iobj):

  return


def part2(rows, iobj):
    for x in iobj.rows:
        (shift,) = pints(x)
        words = x.split('-')[:-2]
        print(shift, ' '.join(rotate_string(word, shift) for word in words))

    return


print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
