from collections import *
import itertools as its
import re
import math
import operator as op

#from util import *
import util.output

from util.input import Input

import dataclasses

YEAR = 2022
DAY = 19

iobj = Input.for_date(DAY, year=YEAR, test=0)
iobj.peek()
iobj.pp_analyze()
rows = list(iobj.rows)

(ss, nn, ll, nts, tt, ww) = iobj.safe_inputs()


from dataclasses import dataclass
import functools

@dataclass(frozen=True, eq=True)
@functools.total_ordering
class State:
  time: int = 0

  geo: int = 0
  geo_bots: int = 0
  obs: int = 0
  obs_bots: int = 0
  clay: int = 0
  clay_bots: int = 0
  ore: int = 0
  ore_bots: int = 0

  def worse(self, other):
    return self != other and all(x <= y for (x,y) in zip(self.value(), other.value()))

  def value(self):
    return (self.geo, self.geo_bots, self.obs, self.obs_bots, self.clay, self.clay_bots, self.ore, self.ore_bots)
    t = (24 - self.time)
    return (self.geo + t * self.geo_bots, self.obs + t * self.obs_bots, self.clay + t * self.clay_bots, self.ore + t* self.ore_bots)
  def __lt__(self, other):
    return self.value() < other.value()
    return (self.geo, self.obs, self.clay, self.ore) < (other.geo, other.obs, other.clay, other.ore)

  def evolve(self, delta):
    changes = {k: getattr(self, k) + delta[k] for k in delta}
    return dataclasses.replace(self, **changes, time=self.time+1)


@dataclasses.dataclass(frozen=True)
class Blueprint:
  index: int
  ore_cost: dict
  clay_cost: dict
  obs_cost: dict
  geo_cost: dict

  @staticmethod
  def from_line(line):
    costs = {}
    (index,) = re.findall('Blueprint (\d+):', line)
    index = int(index)
    for cost_line in line.split('. '):
      (bot,) = re.findall('Each (ore|clay|obs|geo)', cost_line)
      cost = {res: int(val) for (val, res) in re.findall('(\d+) (ore|clay|obs)', cost_line) }

      cost = tuple(cost.get(res, 0) for res in ['geo', 'obs', 'clay', 'ore'])
      costs[bot] = cost
      print(bot, cost)
    
    return Blueprint(index=index, ore_cost=costs['ore'], clay_cost=costs['clay'], obs_cost=costs['obs'], geo_cost=costs['geo'])
  
  @functools.cached_property
  def max_ore(self):
    return max(c[-1] for c in [self.ore_cost, self.clay_cost, self.obs_cost, self.geo_cost])

  @functools.cached_property
  def max_clay(self):
    return max(c[2] for c in [self.ore_cost, self.clay_cost, self.obs_cost, self.geo_cost])

  @functools.cached_property
  def max_obs(self):
    return max(c[1] for c in [self.ore_cost, self.clay_cost, self.obs_cost, self.geo_cost])

  @functools.cached_property
  def max_geo(self):
    return max(c[0] for c in [self.ore_cost, self.clay_cost, self.obs_cost, self.geo_cost])

def can_buy(cost, state):
  return all(c <= s for (c, s) in zip(cost, state))

from util.vector import vsub
def adjacent_states(bp, state):
  (time, mats, bots) = state
  if time >= 32:
    return []

  # buy geo bot
  if can_buy(bp.geo_cost, mats):
    delta = vsub(bots, bp.geo_cost)
    return [
      (time + 1, vadd(delta, mats), vadd(bots, (1, 0, 0, 0)))
    ]

  if all(v > c for (v,c) in zip(mats, bp.geo_cost)):
    return []
  if all(c > v for (v, c) in zip(bots, bp.geo_cost)):
    return []
  if bots[1] > bp.max_obs or bots[2] > bp.max_clay or bots[3] > bp.max_ore:
    return []
  
  opts = []
  # buy obs bot
  if can_buy(bp.obs_cost, mats):
    delta = vsub(bots, bp.obs_cost)
    opts += [
      (time + 1, vadd(delta, mats), vadd(bots, (0, 1, 0, 0)))
    ]
  # buy clay bot
  if can_buy(bp.clay_cost, mats):
    delta = vsub(bots, bp.clay_cost)
    opts += [
      (time + 1, vadd(delta, mats), vadd(bots, (0, 0, 1, 0)))
    ]

  # buy ore bot
  if can_buy(bp.ore_cost, mats):
    delta = vsub(bots, bp.ore_cost)
    opts += [
      (time + 1, vadd(delta, mats), vadd(bots, (0, 0, 0, 1)))
    ]

  # all bots mine
  opts += [ (time + 1, vadd(bots, mats), bots) ]

  return opts



import util.search

def bfs(start, adjacent_fn):
  """
  Breadth-first search
  """

  queue = deque()

  visited = defaultdict(set)
  visited[-1] = set()

  queue.append(start)

  cc = 0
  best = 0
  lvl = -1
  skip = 0
  max_bots = None
  while len(queue) > 0:
    parent_state = queue.popleft()
    cc += 1

    if parent_state[0] > lvl:
      lvl = parent_state[0]
      t_left = 32 - parent_state[0]
      max_bots = t_left * (t_left -1) // 2

      print(best, parent_state, len(queue), len(visited[lvl]), cc, skip)
      del visited[lvl-1]

    if cc % 100_000 == 0:
      print(best, parent_state, len(queue), len(visited[lvl]), cc, skip)
    if parent_state[1][0] > best:
      best = parent_state[1][0]
      print(best, parent_state, len(queue), len(visited[lvl]), cc, skip)
    

    if parent_state[1][0] + parent_state[2][0] * max_bots < best:
      skip += 1
      continue

    #if parent_state.value() not in visited:
    #  visited[parent_state.value()] = parent_state.time
    #elif parent_state.time >= visited[parent_state.value()]:
    #  #print('-->', parent_state, visited[parent_state.value()])
    #  cc += 1
    #  continue
    #else:
    #  visited[parent_state.value()] = parent_state.time

    for child_state in adjacent_fn(parent_state):
      if child_state not in visited[child_state[0]]:
        queue.append(child_state)
        visited[child_state[0]].add(child_state)

  return best

from util.vector import vadd, vsub

def part1(rows, iobj):

  r = 1

  for row in rows[:3]:
    bp = Blueprint.from_line(row)
    print(bp.max_clay)
    print('------------', bp.index, '-----------')
    start = (0, (0, 0, 0, 0), (0, 0, 0, 1))

    def adj_fn(state):
      return adjacent_states(bp, state)

    v = bfs(start, adj_fn)

    r *= (v)

    print(f'{r} *= {v}')
    print('')

  return r

  ss = []
  for x in path:
    if x.time == 5 or x.time == 4:
      ss += [x]
  
  for s in ss:
    print(s, any(s.worse(t) for t in ss))

  return


def part2(rows, iobj):

  return

util.output.pretty_answer('P1', part1(rows, iobj))
util.output.pretty_answer('P2', part2(rows, iobj))
