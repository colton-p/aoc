from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 4

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()
ww = iobj.word_tuples()

def part2(rows, iobj):
  pp = []

  p = ''
  for row in rows:
    if row:
      p += row + ' '
    else:
      pp += [ p ]
      p = ''
  else:
      pp += [ p ]

  EXP = set(*['byr iyr eyr hgt hcl ecl pid'.split(' ')])

  def chk(p):
    if not p: return False
    keys = re.split('[: ]+', p)

    d = { k: v for (k,v) in each_slice(keys) if k}

    if any(e not in d for e in EXP):
      return False

    # print(d)

    (hgt_x,) = ints(d['hgt'])
    hgt_u = d['hgt'][-2:]
    if hgt_u == 'cm':
      hgt = (150 <= hgt_x <= 193)
    elif hgt_u == 'in':
      hgt = (59 <= hgt_x <= 76)
    else:
      hgt = False
    
    hcl = bool(re.match('^#[0-9a-f]{6}$', d['hcl'].strip()))
    ecl = d['ecl'] in 'amb blu brn gry grn hzl oth'.split(' ')
    pid = len(d['pid']) == 9 and safe_int(d['pid']) != d['pid']
    byr = 1920 <= int(d['byr']) <= 2002
    iyr = 2010 <= int(d['iyr']) <=2020
    eyr = 2020 <= int(d['eyr']) <=2030

    return (hcl and ecl and pid and byr and iyr and eyr and hgt)

  return quantify(pp, chk)

def part1(rows, iobj):
  pp = []

  p = ''
  for row in rows:
    if row:
      p += row + ' '
    else:
      pp += [ p ]
      p = ''
  else:
      pp += [ p ]

  EXP = set(*['byr iyr eyr hgt hcl ecl pid'.split(' ')])

  def chk(p):
    if not p: return False
    keys = re.split('[: ]+', p)

    d = [ k for (k,v) in each_slice(keys) if k]

    return all(e in d for e in EXP)

  return quantify(pp, chk)

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
