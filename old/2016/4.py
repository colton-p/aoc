from util import *

import re
import itertools
import collections

rows = input_rows('4.in')


def do_line(line):
  m = re.match('([\-a-z]+)-(\d+)\[([a-z]{5})\]', line)

  c = collections.Counter(m.group(1))
  del c['-']
  key = [k for (k,v) in sorted(c.most_common(), key = lambda x: (-x[1],x[0]))][:5]
  return (''.join(key) == m.group(3), int(m.group(2)))

print count_with_predicate(rows, do_line)

for line in rows:
  (incl, val) = do_line(line)
  if incl:
    print line, val
    #import codecs
    #print codecs.decode(line, 'rot13')
