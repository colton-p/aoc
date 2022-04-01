from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2021
DAY = 19

iobj = Input.for_date(DAY, year=YEAR, test=False)
rows = list(iobj.rows)

TX_FN = [
  lambda x,y,z: (x, y, z),
  lambda x,y,z: (x, z, -y),
  lambda x,y,z: (x, -y, -z),
  lambda x,y,z: (x, -z, y),

  lambda x,y,z: (-x, y, -z),
  lambda x,y,z: (-x, -z, -y),
  lambda x,y,z: (-x, -y, z),
  lambda x,y,z: (-x, z, y),

  lambda x,y,z: (y, -x, z),
  lambda x,y,z: (y, z, x),
  lambda x,y,z: (y, x, -z),
  lambda x,y,z: (y, -z, -x),
  lambda x,y,z: (-y, x, z),
  lambda x,y,z: (-y, z, -x),
  lambda x,y,z: (-y, -x, -z),
  lambda x,y,z: (-y, -z, x),

  lambda x,y,z: (z, y, -x),
  lambda x,y,z: (z, -x, -y),
  lambda x,y,z: (z, -y, x),
  lambda x,y,z: (z, x, y),

  lambda x,y,z: (-z, y, x),
  lambda x,y,z: (-z, x, -y),
  lambda x,y,z: (-z, -y, -x),
  lambda x,y,z: (-z, -x, y),

]

def parse(iobj):
  S = {}
  for block in iobj.line_delimited():
    (scanner_s, *lines) = block
    (scanner,) = ints(scanner_s)
    pts = [ tuple(ints(line)) for line in lines]
    S[scanner] = pts
  return S

def compare(s, t, s_ix, t_ix):
  # relative to first beacon
  sp = [vsub(s_i, s[s_ix]) for s_i in s]
  # relative to t_ix beacon
  tp = [vsub(t_i, t[t_ix]) for t_i in t]

  overlap = list(set(sp) & set(tp))
  index_map = {
    s.index(vadd(pt, s[s_ix])): t.index(vadd(pt, t[t_ix])) for pt in overlap
  }
  point_map = {
    s[i]: t[j] for (i,j) in index_map.items()
  }

  return point_map

def transformed_pts(pts):
   return [ 
     ([tx_fn(*pt) for pt in pts], tx_fn)
     for tx_fn in TX_FN
   ]
  

def try_align(A, B):
  for ix_A in range(len(A)):
    for ix_B in range(len(B)):
      for (Bp, fn) in transformed_pts(B):
        point_map = compare(A, Bp, ix_A, ix_B)
        if len(point_map) < 12: continue

        offsets = [ vsub(Ai, Bpi) for (Ai, Bpi) in point_map.items() ]
        assert len(set(offsets)) == 1
        return offsets[0], Bp
  return None, None

def align(known, beacons, skips):
  for ix_A in known:
    for (ix_B, B) in beacons.items():
      if ix_B in known: continue
      if (ix_A , ix_B) in skips: continue
      A = beacons[ix_A]
      print(ix_A, ix_B)
      B_offset, B_rot = try_align(A, B)
      if B_offset and B_rot:
        return (ix_A, ix_B, B_offset, B_rot)
      else:
        skips.add((ix_A, ix_B))


def part1(rows, iobj):
  beacons = parse(iobj)
  known = {0 : (0, 0, 0)}
  skips = set()

  for _i in range(len(beacons)-1):
    (ix_A, ix_B, B_offset, B_rot) = align(known, beacons, skips)
    known[ix_B] = vadd(known[ix_A] , B_offset)
    beacons[ix_B] = B_rot
    print(f'{len(known)}/{len(beacons)} aligned')

  for x in known:
    print(x, known[x])

  true_pts = []
  for (ix, pts) in beacons.items():
    true_pts += [{vadd(pt, known[ix]) for pt in pts}]

  true_beacons = set(itertools.chain(*true_pts))

  return len(true_beacons)
  d, S1r = align(S[0], S[1])
  S[1] = S1r
  print('s1 -> s0', d)

  (x, S4r) = align(S[1], S[4])
  print('s4 -> s1', x)

  print(vadd(x, d))

  return

  for i in range(len(S[1])):
    for (T, fn) in transformed_pts(S[1]):
      rslt = compare(S[0], T, i)
      if len(rslt) > 1:
        print(rslt, len(rslt))
        print([vsub(k, v) for (k,v) in rslt.items()])

def part2(rows, iobj):
  S = {
0: (0, 0, 0),
9: (2, 1164, 41),
11: (27, 140, -1287),
29:(1137, -32, -57),
10:(1289, 1241, -37),
19:(-45, 1174, -1191),
15:(1174, 16, 1239),
36:(2483, 73, 11),
28:(2319, 1204, -73),
34:(1142, 1352, 1164),
26:(-61, 2500, -1165),
20:(1216, 96, 2358),
27:(1118, -1129, 1231),
8:(3601, -16, -80),
18:(2399, 88, -1282),
23:(2405, -1165, 43),
1:(2320, 2356, -48),
6:(2493, 1292, -1245),
14:(1133, 2441, 1205),
13:(29, -1118, 1226),
12:(4772, 105, 56),
16:(3526, 17, -1303),
35:(3667, -1065, 63),
4:(3706, 2481, -87),
25:(2470, 3720, 52),
37:(5957, -46, -95),
24:(3675, -1127, -1148),
5:(3601, 2517, 1178),
7:(4768, 2434, 25),
21:(3594, 2364, -1153),
33:(3554, 3580, 33),
22:(5928, -1, -1243),
3:(4871, 2359, 1248),
31:(3549, 2439, 2354),
32:(4797, 2530, 2345),
2:(4772, 2460, 3667),
17:(4782, 3739, 3602),
30:(4877, 2438, 4735),
  }

  return max(vdist1(a,b) for (a,b) in itertools.combinations(S.values(), 2))

  return

#util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
