#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import datetime
import operator as op

print 'Day 4'
print '------'

rows = input_rows('4.in')

print 'input rows:' ,len(rows)
print ''

rows = split_rows(rows, regex='\[(.*) (\d+:\d+)\] (.*)')

rows = sorted(rows, key=lambda x: [x[0], x[1]])
for r in rows:
  print r


sleep_times = defaultdict(int)

def now(d, t):
  (y,m,d) = map(int, d.split('-'))
  (h,mm) = map(int, t.split(':'))
  dt = datetime.datetime(y,m,d, h, mm)
  return dt

active = None
fell_asleep = None
for (d, t, instr) in rows:
  if instr == 'falls asleep':
    fell_asleep = now(d, t)
    awake = False
  elif instr == 'wakes up':
    sleep_times[active] += (now(d, t) - fell_asleep).total_seconds() / 60
  else:
    (guard,) = re.findall('\d+', instr)
    active = guard

(sleepiest, sleeping) =  max(sleep_times.items(), key=lambda x: x[1])
print 'sleepiest'
print sleepiest, sleeping


minutes = defaultdict(lambda : defaultdict(int))
active = None
fell_asleep_min = None
for (d, t, instr) in rows:
  if instr == 'falls asleep':
    fell_asleep = now(d, t)
    fell_asleep_min = int(t.split(':')[1])
    awake = False
  elif instr == 'wakes up':
    for mm in range(fell_asleep_min, int(t.split(':')[1])):
      minutes[active][mm] += 1
  else:
    (guard,) = re.findall('\d+', instr)
    active = guard


#(a,b) = max(minutes.items(), key=lambda x: x[1])
#print a,b
#print '---'
#print int(sleepiest) * int(a)


a = 0

for g in minutes:
  (a,b) = max(minutes[g].items(), key=lambda x: x[1])
  print g, a, b

