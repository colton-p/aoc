#!/usr/bin/env python

from collections import *
from itertools import *
import re
import math
import operator as op

from util import *

YEAR = 2019
DAY = 20

iobj = Input.for_date(DAY, year=YEAR, test=False)
#iobj.peak()
#iobj.pp_analyze()
rows = list(iobj.rows)


def build_graph(E, lvl):
  G = nx.Graph()
  kk = list(E.keys())
  for k in kk:
    if E[k] == '#':
      continue

    for adj in rect_adj(k):
      if E[adj] != '#':
        w = 1
        if len(E[k]) == 2 or len(E[adj]) == 2:
          w=0

        G.add_edge(k, adj, weight=w)
  kk = list(E.keys())



  # portal -> portal
  for k in kk:
    if len(E[k]) != 2:
      continue

    adj = [adj_k for adj_k in E if k!= adj_k and E[adj_k] == E[k]]
    if len(adj) == 1:
      G.add_edge(k, adj[0],weight=1)
    else:
      print('ST', k, E[k])


def part1(rows, iobj):
  # ll = iobj.ints()
  DD = rows_to_grid(rows)


  D = defaultdict(lambda: '#')
  for k,v in DD.items():
    D[k] = v
  print_grid(D)


  E = defaultdict(lambda: '#')

  for k in DD:
    if D[k] == '.' or D[k] == '#':
      E[k] = D[k]
    elif D[k] == '_':
      E[k] = '#'
    else:
      adj = set([D[a] for a in rect_adj(k)])
      adj_letters = [x for x in adj if x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']
      adj_letters_pos = [a for a in rect_adj(k) if D[a] in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ']

      assert len(adj_letters) <= 1

      if len(adj) == 3:
        if '.' in adj and ('#' in adj or '_' in adj) and len(adj_letters) == 1:

          if adj_letters_pos[0][0] < k[0]:
            E[k] = adj_letters[0] + D[k]
          elif adj_letters_pos[0][0] > k[0]:
            E[k] = D[k] + adj_letters[0]
          elif adj_letters_pos[0][1] < k[1]:
            E[k] = adj_letters[0] + D[k]
          elif adj_letters_pos[0][1] > k[1]:
            E[k] = D[k] + adj_letters[0]


  G = nx.Graph()
  kk = list(E.keys())
  for k in kk:
    if E[k] == '#':
      continue

    for adj in rect_adj(k):
      if E[adj] != '#':
        w = 1
        if len(E[k]) == 2 or len(E[adj]) == 2:
          w=0

        G.add_edge(k, adj, weight=w)
  kk = list(E.keys())
  for k in kk:
    if len(E[k]) != 2:
      continue

    adj = [adj_k for adj_k in E if k!= adj_k and E[adj_k] == E[k]]
    if len(adj) == 1:
      G.add_edge(k, adj[0],weight=1)
    else:
      print('ST', k, E[k])

  print(nx.info(G))





  (xn) = [k for k in E if E[k] == 'SU']

  (aa,) = [k for k in E if E[k] == 'AA']
  (zz,) = [k for k in E if E[k] == 'ZZ']
  print(aa, zz)

  c = 0
  for x in nx.shortest_path(G, aa, zz, 'weight'):
    if len(E[x]) == 2:
      c += 1
    print(x, E[x])

  p = nx.shortest_path_length(G, aa, zz,'weight')

  return p


def grid_with_portals(rows):

  DD = rows_to_grid(rows)

  max_x = len(rows[0])
  max_y = len(rows)

  ys = sorted(set(k[1] for k in DD if DD[k] not in '#._'))
  ys = (ys[1], ys[2], ys[-3], ys[-2])

  xs = sorted(set(k[0] for k in DD if DD[k] not in '#._'))
  xs = (xs[1], xs[2], xs[-3], xs[-2])

  #print(sorted(set(k[1] for k in DD if DD[k] not in '#._')))
  
  E = dict(DD)
  portals = defaultdict(list)

  # Vertical
  # outside, down
  y_tgt = ys[0]
  for x in range(max_x):
    if DD[(x,y_tgt)] in '#._':
      continue
    portal_name = DD[(x,y_tgt-1)] + DD[(x,y_tgt)]
    pos = (x,y_tgt+1)

    E[(x,y_tgt-1)] = E[(x,y_tgt)] = '_'
    E[pos] =  portal_name
    portals[portal_name] += [pos]

  # outside, up
  y_tgt = ys[3]
  for x in range(max_x):
    if DD[(x,y_tgt)] in '#._':
      continue
    portal_name = DD[(x,y_tgt)] + DD[(x,y_tgt+1)]
    pos = (x,y_tgt-1)

    E[(x,y_tgt+1)] = E[(x,y_tgt)] = '_'
    E[pos] =  portal_name
    portals[portal_name] += [pos]

  # Horizontal
  # outside, right
  x_tgt = xs[0]
  for y in range(max_y):
    if DD[(x_tgt,y)] in '#._':
      continue
    portal_name = DD[(x_tgt-1,y)] + DD[(x_tgt,y)]
    pos = (x_tgt+1,y)

    E[(x_tgt-1,y)] = E[(x_tgt,y)] = '_'
    E[pos] =  portal_name
    portals[portal_name] += [pos]

  # outside, left
  x_tgt = xs[3]
  for y in range(max_y):
    if DD[(x_tgt,y)] in '#._':
      continue
    portal_name = DD[(x_tgt,y)] + DD[(x_tgt+1,y)]
    pos = (x_tgt-1,y)

    E[(x_tgt,y)] = E[(x_tgt+1,y)] = '_'
    E[pos] =  portal_name
    portals[portal_name] += [pos]


  # Vertical
  # inside, down
  y_tgt = ys[2]
  for x in range(max_x):
    if DD[(x,y_tgt)] in '#._':
      continue
    portal_name = DD[(x,y_tgt-1)] + DD[(x,y_tgt)]
    pos = (x,y_tgt+1)

    E[(x,y_tgt-1)] = E[(x,y_tgt)] = '_'
    E[pos] =  portal_name
    portals[portal_name] += [pos]


  # inside, up
  y_tgt = ys[1]
  for x in range(max_x):
    if DD[(x,y_tgt)] in '#._':
      continue
    portal_name = DD[(x,y_tgt)] + DD[(x,y_tgt+1)]
    pos = (x,y_tgt-1)

    E[(x,y_tgt+1)] = E[(x,y_tgt)] = '_'
    E[pos] =  portal_name
    portals[portal_name] += [pos]

  # Horizontal
  # inside, right
  x_tgt = xs[2]
  for y in range(max_y):
    if DD[(x_tgt,y)] in '#._':
      continue
    portal_name = DD[(x_tgt-1,y)] + DD[(x_tgt,y)]
    pos = (x_tgt+1,y)

    E[(x_tgt-1,y)] = E[(x_tgt,y)] = '_'
    E[pos] =  portal_name
    portals[portal_name] += [pos]

  # inside, left
  x_tgt = xs[1]
  for y in range(max_y):
    if DD[(x_tgt,y)] in '#._':
      continue
    portal_name = DD[(x_tgt,y)] + DD[(x_tgt+1,y)]
    pos = (x_tgt-1,y)

    E[(x_tgt,y)] = E[(x_tgt+1,y)] = '_'
    E[pos] =  portal_name
    portals[portal_name] += [pos]


  source = portals['AA'][0]
  sink = portals['ZZ'][0]
  del portals['AA']
  del portals['ZZ']

  return E, portals, source, sink

def build_p1_graph(E, portals):
  adj = defaultdict(list)

  # normal movement
  for s in E:
    for t in rect_adj(s):
      if E.get(s, '#') in '#_' or E.get(t, '#') in '#_':
        continue
      adj[s] += [t]

  # connect portals

  for (inside, outside) in portals.values():
    adj[inside] += [outside]

  return nx.Graph(adj)

def build_p2_graph_tier_adj(E, lvl):
  adj = defaultdict(list)

  # normal movement
  for s in E:
    for t in rect_adj(s):
      if E.get(s, '#') in '#_' or E.get(t, '#') in '#_':
        continue
      sx = tuple(list(s) + [lvl])
      tx = tuple(list(t) + [lvl])
      adj[sx] += [tx]
      adj[tx] += [sx]

  return adj

def build_p2_graph(E, portals):

  max_lvl = 50

  adj = defaultdict(list)
  for lvl in range(max_lvl):
    aa = build_p2_graph_tier_adj(E, lvl)
    for k in aa:
      adj[k] += aa[k]


  for lvl in range(max_lvl):
    for (outside, inside) in portals.values():
      if lvl + 1 < max_lvl:
        s = (inside[0], inside[1], lvl)
        t = (outside[0], outside[1], lvl+1)
        adj[s] += [t]

    for (outside, inside) in portals.values():
      if lvl != 0:
        s = (outside[0], outside[1], lvl)
        t = (inside[0], inside[1], lvl-1)
        adj[s] += [t]

  return nx.DiGraph(adj)


def part1(rows, iobj):
  (E, portals,source,sink) = grid_with_portals(rows)
  print(portals)

  G = build_p1_graph(E, portals)

  return nx.shortest_path_length(G, source, sink)

def part2(rows, iobj):
  (E, portals,source,sink) = grid_with_portals(rows)

  G = build_p2_graph(E, portals)

  source = (source[0], source[1], 0)
  sink = (sink[0], sink[1], 0)


  print(max(x[2] for x in nx.shortest_path(G, source, sink)))

  return nx.shortest_path_length(G, source, sink)

print('P1', part1(rows, iobj))
print('P2', part2(rows, iobj))
