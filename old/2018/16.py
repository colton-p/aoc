#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import operator as op

print 'Day 16'
print '------'

rows = input_rows('16', test=False)

samples = list(grouper(rows, 4, fillvalue=''))


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

FUNCS = [addi, addr, bani, banr, bori, borr, eqir, eqri, eqrr, gtir, gtri, gtrr, muli, mulr, seti, setr]

def parse_sample(sample):
  before = extract_numbers(sample[0])
  after = extract_numbers(sample[2])
  opcode = extract_numbers(sample[1])
  (op, v1, v2, v3) = opcode
  return (before, after, op, v1, v2, v3)



def apply(func, R, a, b, c):
  R = list(R)
  func(R, a, b, c)
  return R

def behaves_like(sample):
  (before, after, op, a, b, c) = parse_sample(sample)

  L = []
  cnt = 0
  for func in FUNCS:
    rslt = apply(func, before, a, b, c)
    if rslt == after:
      cnt +=1
      L += [func]
  return (op, set(L))

P1 = 0
s = set()

M = defaultdict(list)


for sample in samples:
  (op, options) = behaves_like(sample)
  M[op] += [options]

for op in M:
  M[op] = M[op][0].intersection(*M[op][1:])

left = set(FUNCS)

done = set()

for op in M:
  print op, len(M[op])


for i in range(10):

  for op in M:
    if len(M[op]) == 1:
      done |= M[op]

  for op in M:
    if len(M[op]) > 1:
      M[op] -= done

for op in M:
  M[op] = M[op].pop()
M = dict(M)

with open('16.in2', 'r') as f:
  prog = [line.strip() for line in f]

prog = [extract_numbers(line) for line in prog]
R = [0,0,0,0]

for (opcode, a, b, c) in prog:
  func = M[opcode]
  func(R, a, b, c)
  print R


print R

