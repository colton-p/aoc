from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 7

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

def part1(rows, iobj):

  G = nx.DiGraph()

  for row in rows:
    t = re.split('bags?|\d', row)
    t = [x.strip() for x in t]
    t = [x.strip() for x in t if x not in ['.', ',', 'contain', 'contain no other']]

    u = t[0]
    for v in t[1:]:
      G.add_edge(v, u)


  return len(list(nx.dfs_postorder_nodes(G, 'shiny gold')))

def part2(rows, iobj):
  G = {}

  for row in rows:
    a, b = row.split('bags contain ')
    b = b.split(', ')

    a = a.strip()
    adj = []
    if b != ['no other bags.']:
      for kv in b:
        kv = kv.split(' ')
        adj += [ (int(kv[0]), ' '.join(kv[1:3])) ]
    
    G[a] = adj


  def f(node):
    c = 0
    for (w, k) in G[node]:
      c += (w * (1 + f(k)))

    return c


  return f('shiny gold')

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
