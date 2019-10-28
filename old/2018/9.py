#!/usr/bin/env python

from util import *
from num_util import *

from collections import *
import itertools
from itertools import *
import re
import math
import operator as op

print('Day 9')
print('------')

rows = input_rows('9', test=False)

(n_players, n_marbles) = map(int, re.findall('\d+', rows[0]))

n_marbles *= 100

scores = defaultdict(int)
L = deque()
L.append(0)

marble_iter = range(1, n_marbles + 1)
player_iter = itertools.cycle(range(1, n_players + 1))

for (marble, player) in zip(marble_iter, player_iter):
  if marble % 23 != 0:
    L.rotate(-2)
    L.appendleft(marble)
  else:
    scores[player] += marble
    L.rotate(7)
    scores[player] += L.popleft()
  #print player, ''.join(['(%2d)' % i if i == L[current_ix] else '%4d' % i for i in L])

print(max(scores.values()))
