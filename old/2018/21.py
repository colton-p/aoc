#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import sys
import itertools
from itertools import *
import re
import math
import operator as op

print 'Day 21'
print '------'

rows = input_rows('21', test=False)

print 'row count:', len(rows)
print '------'

R = [10, 0,0,0,0,0]

def addr(R, a, b, c):
  R[c] = R[a] + R[b]

def addi(R, a, b, c):
  R[c] = R[a] + b

def mulr(R, a, b, c):
  R[c] = R[a] * R[b]

def muli(R, a, b, c):
  R[c] = R[a] * b

def banr(R, a, b, c):
  R[c] = R[a] & R[b]

def bani(R, a, b, c):
  R[c] = R[a] & b

def borr(R, a, b, c):
  R[c] = R[a] | R[b]

def bori(R, a, b, c):
  R[c] = R[a] | b

def setr(R, a, b, c):
  R[c] = R[a]
def seti(R, a, b, c):
  R[c] = a

def gtir(R, a, b, c):
  R[c] = int(a > R[b])

def gtri(R, a, b, c):
  R[c] = int(R[a] > b)

def gtrr(R, a, b, c):
  R[c] = int(R[a] > R[b])

def eqir(R, a, b, c):
  R[c] = int(a == R[b])

def eqri(R, a, b, c):
  R[c] = int(R[a] == b)

def eqrr(R, a, b, c):
  R[c] = int(R[a] == R[b])


IP_REG = None

def seti(R, a, b, c):
  R[c] = a

def setr(R, a, b, c):
  R[c] = R[a]


def run(val):
  global R

  S = set()
  R[0] = val
  ip = 0

  ip_pragma = rows[0]
  IP_REG = extract_number(ip_pragma)

  instrs = rows[1:]

  cnt = 0
  while True:

    print cnt, ip, instrs[ip], R

    if cnt > 2100:
      break
    if ip == 28:
      print cnt, R[3], R[4]
      sys.stdout.flush()
      if R[4] in S:
        break
      S.add(R[4])

    if ip not in range(len(instrs)):
      break
    line = instrs[ip]
    op = line[:4]
    (a,b,c) = extract_numbers(line.split('#')[0])
    func = eval(op)

    R[IP_REG] = ip

    func(R, a, b, c)

    ip = R[IP_REG]

    ip += 1
    cnt +=1

  return cnt

print run(0)
