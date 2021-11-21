from collections import *
import itertools as its
import re
import math
import operator as op

from util import *
import util.output

YEAR = 2020
DAY = 20

iobj = Input.for_date(DAY, year=YEAR, test=False)
iobj.peak()
iobj.pp_analyze()
rows = list(iobj.rows)
IMAGE_SIZE = 12

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()

TILES = {}
B = {}

ALIGNED_TILES = defaultdict(set)

for tile in iobj.line_delimited():
  (ix,) = ints(tile[0])
  TILES[ix] = Grid.from_rows(tile[1:])


def all_borders(G):
  return { 
    tuple(G[0, x] for x in range(10)),
    tuple(G[x, 0] for x in range(10)),
    tuple(G[9, x] for x in range(10)),
    tuple(G[x, 9] for x in range(10)),
    tuple(G[0, x] for x in reversed(range(10))),
    tuple(G[x, 0] for x in reversed(range(10))),
    tuple(G[9, x] for x in reversed(range(10))),
    tuple(G[x, 9] for x in reversed(range(10))),
  }

for ix in TILES:
  for b in all_borders(TILES[ix]):
    ALIGNED_TILES[b].add(ix)

def top(G):
  return tuple(G[x, 0] for x in range(10))
def bottom(G):
  return tuple(G[x, 9] for x in range(10))
def left(G):
  return tuple(G[0, x] for x in range(10))
def right(G):
  return tuple(G[9, x] for x in range(10))

class Board():
  def __init__(self, ix_map, tile_map, next_to_place):
    self.ix_map = ix_map
    self.tile_map = tile_map
    self.next_to_place = next_to_place
    
    assert next_to_place not in ix_map
    assert next_to_place not in tile_map
    assert set(ix_map.keys()) == set(tile_map.keys())
    assert len(ix_map.values()) == len(set(ix_map.values()))
    assert set(ix_map.values()) <= set(TILES.keys())

    self.unplaced = set(TILES.keys()) - set(ix_map.values())
  
  def next_boards(self):
    for (tile_ix, _o_ix, tile) in self.orientated_candidates_to_place():
      yield self.place_tile(tile_ix, tile)

  def place_tile(self, tile_ix, tile):
    assert tile_ix in self.unplaced

    new_ix = {**self.ix_map, **{self.next_to_place: tile_ix}}
    new_tile = {**self.tile_map, **{self.next_to_place: tile}}

    (x, y) = self.next_to_place
    pos = IMAGE_SIZE*y + x + 1
    new_next = (pos % IMAGE_SIZE, pos // IMAGE_SIZE)

    return Board(new_ix, new_tile, new_next)


  def candidates_to_place(self):
    candidates = set(self.unplaced)

    up_adj = vadd(self.next_to_place, DIR.UP)
    if up_adj in self.tile_map:
      edge = bottom(self.tile_map[up_adj])
      candidates &= ALIGNED_TILES[edge]
    
    left_adj = vadd(self.next_to_place, DIR.LEFT)
    if left_adj in self.tile_map:
      edge = right(self.tile_map[left_adj])
      candidates &= ALIGNED_TILES[edge]

    return candidates
  
  def orientated_candidates_to_place(self):
    for tile_ix in self.candidates_to_place():
      for (o_ix, tile) in enumerate(TILES[tile_ix].all_orientations()):
        tile.recenter()
        if self.can_place(tile):
          yield (tile_ix, o_ix, tile)


  def can_place(self, tile):
    up_adj = vadd(self.next_to_place, DIR.UP)
    if up_adj in self.tile_map:
      if top(tile) != bottom(self.tile_map[up_adj]): return False

    #down_adj = vadd(self.next_to_place, DIR.DOWN)
    #if down_adj in self.tile_map:
    #  if bottom(tile) != top(self.tile_map[down_adj]): return False

    left_adj = vadd(self.next_to_place, DIR.LEFT)
    if left_adj in self.tile_map:
      if left(tile) != right(self.tile_map[left_adj]): return False

    #right_adj = vadd(self.next_to_place, DIR.RIGHT)
    #if right_adj in self.tile_map:
    #  if right(tile) != left(self.tile_map[right_adj]): return False
    
    return True

def f(S):
  if not S.unplaced:
    return S

  for T in S.next_boards():
    r = f(T)
    if r: return r


def part1(rows, iobj):

  S = Board({}, {}, (0,0))
  # S = S.place_tile(1951, TILES[1951].flip_vertical().recenter())

  T = f(S)

  #r = [T.ix_map[p] for p in [ (0,0), (IMAGE_SIZE-1, 0), (0, IMAGE_SIZE-1), (IMAGE_SIZE-1, IMAGE_SIZE-1)] ]
  #print(r)
  #return prod(r)

  I = {}

  for (X,Y) in T.tile_map.keys():
    tile = T.tile_map[(X,Y)].subgrid(1, 1, 8 ,8).recenter()

    for ((x,y), val) in tile.grid.items():
      (a, b) = 8*X + x, 8*Y + y
      assert (a,b) not in I
      I[(a,b)] = val

  monster_string = """
                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
  """
  MONSTER = Grid.from_string(monster_string)

  def is_monster(image, pos):
    s = set()
    M = Grid(MONSTER.grid).translate(pos[0], pos[1])
    for p in M.grid:
      if p not in image:
        return False
      if M[p] != '#': continue
      if image[p] != '#':
        return False
      s.add(p)
    return s
  
  def count_monsters(image):
    monster = set()
    for pos in image.grid:
      r = is_monster(image.grid, pos)
      if r:
        monster |= r
    
    if monster:
      return len({k for k in image.grid if image.grid[k] == '#'} - monster)
    return None

  for image in Grid(I).all_orientations():
    image.recenter()
    r = count_monsters(image)
    if r:
      return r



def part2(rows, iobj):

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
