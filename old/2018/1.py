from util import *
from num_util import *

import collections
import itertools
import re
import math
import operator

rows = input_rows('1.in')

x = map(int,rows)

c = set([0])

s = 0
while True:
  for i in x:
    s += i
    if s in c:
      print s
      exit()
      break
    c.add(s)





