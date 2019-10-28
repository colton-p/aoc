#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import operator as op


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

ip = 0

IP_REG = None

def seti(R, a, b, c):
  R[c] = a

def setr(R, a, b, c):
  R[c] = R[a]

def pretty_instruction(op_code, a, b, c):

  imm_func = lambda x: '%d' % x
  reg_func = lambda x: 'R[%d]' % x
  m = {
   'addi': ['+', reg_func, imm_func],
   'addr': ['+', reg_func, reg_func],
   'bani': ['&', reg_func, imm_func],
   'banr': ['&', reg_func, reg_func],
   'bori': ['|', reg_func, imm_func],
   'borr': ['|', reg_func, reg_func],
   'eqir': ['==', imm_func, imm_func],
   'eqri': ['==', reg_func, imm_func],
   'eqrr': ['==', reg_func, reg_func],
   'gtir': ['>', imm_func, imm_func],
   'gtri': ['>', reg_func, imm_func],
   'gtrr': ['>', reg_func, reg_func],
   'muli': ['*', reg_func, imm_func],
   'mulr': ['*', reg_func, reg_func],
   'seti': ['', reg_func, lambda x: ''],
   'setr': ['', reg_func, lambda x: '']
  }
  (op, lhs, rhs) = m[op_code]

  line = '%s = %s %s %s' % (reg_func(c), lhs(a), op, rhs(b))

  return line + (20 - len(line)) * ' '


def run(rows, limit=None):

  R = [0, 0, 0, 0, 0, 0]

  ip_pragma = rows[0]


  IP_REG = extract_number(ip_pragma)
  print IP_REG
  assert ip_pragma == "#ip %d" % IP_REG, ip_pragma

  ip = R[IP_REG]

  instructions = rows[1:]

  count = 0
  while True:
    if limit and count > limit:
      break


    if ip not in range(len(instructions)):
      break
    line = instructions[ip]

    op = line[:4]
    (a,b,c) = extract_numbers(line)
    func = eval(op)

    print "%3d |  %3d  %12s   |   %s   |   %s" % (count, ip, line, pretty_instruction(op,a,b,c), ' '.join(['%6d' % x for x in R]))

    R[IP_REG] = ip

    func(R, a, b, c)

    ip = R[IP_REG]

    ip += 1
    count +=1

  print R


if __name__ == "__main__":
  code = """#ip 5
  addi 5 16 5
  seti 1 8 3
  seti 1 1 1
  mulr 3 1 4
  eqrr 4 2 4
  addr 4 5 5
  addi 5 1 5
  addr 3 0 0
  addi 1 1 1
  gtrr 1 2 4
  addr 5 4 5
  seti 2 7 5
  addi 3 1 3
  gtrr 3 2 4
  addr 4 5 5
  seti 1 5 5
  mulr 5 5 5
  addi 2 2 2
  mulr 2 2 2
  mulr 5 2 2
  muli 2 11 2
  addi 4 8 4
  mulr 4 5 4
  addi 4 20 4
  addr 2 4 2
  addr 5 0 5
  seti 0 4 5
  setr 5 8 4
  mulr 4 5 4
  addr 5 4 4
  mulr 5 4 4
  muli 4 14 4
  mulr 4 5 4
  addr 2 4 2
  seti 0 7 0
  seti 0 9 5"""

  rows = [row.strip() for row in code.split('\n')]
  print rows

  run(rows, limit=100)

