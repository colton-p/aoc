"""
Search algorithms.
"""

import collections
from heapdict import heapdict


def _build_goal_fn(goal):
  if callable(goal):
    return goal
  elif goal is not None:
    return lambda x: (x == goal)
  else:
    return None

def dfs(start, adjacent_fn, goal=None):
  """
  Depth-first search
  """
  goal_fn = _build_goal_fn(goal)
  stack = collections.deque()

  stack.append(start)
  visited = set()
  parent_map = {start: None}

  while len(stack):
    v = stack.pop()
    if v in visited: continue
    visited.add(v)

    for child_state in reversed(sorted(adjacent_fn(v))):
      if child_state not in parent_map:
          parent_map[child_state] = v

      if goal_fn and goal_fn(child_state):
          return construct_path(child_state, parent_map), parent_map

      stack.append(child_state)

  assert set(parent_map.keys()) == visited
  return None, parent_map

def bfs(start, adjacent_fn, goal=None):
  """
  Breadth-first search
  """
  goal_fn = _build_goal_fn(goal)

  queue = collections.deque()
  visited = set()

  parent_map = dict()

  parent_map[start] = (None)
  queue.append(start)

  while len(queue) > 0:
    parent_state = queue.popleft()

    if goal_fn and goal_fn(parent_state):
      return construct_path(parent_state, parent_map), parent_map

    for child_state in adjacent_fn(parent_state):

      if child_state in visited:
        continue

      if child_state not in parent_map:
        parent_map[child_state] = parent_state
        queue.append(child_state)

    visited.add(parent_state)

  return None, parent_map

def construct_path(state, parent_map):
  """
  Path from predecessor dict.
  """
  path = []

  while state in parent_map:
    path.append(state)
    state = parent_map[state]

  return list(reversed(path))

def shortest_path(start, adjacent_fn, goal):
  """
  Dijkstra shortest path

  - adjacent_fn: (u) -> (v, weight)

  Returns shortest `(dist, path)` from start to goal.
  """
  seen = set()
  Q = heapdict()
  dist = collections.defaultdict(lambda: 9999999999)
  prev = {}

  prev[start] = None
  dist[start] = 0
  Q[start] = 0

  while len(Q) != 0:
    (u, _) = Q.popitem()

    if u == goal:
      return dist[u], construct_path(u, prev)

    seen.add(u)

    for (v, weight) in adjacent_fn(u):
      if v in seen:
        continue
      Q[v] = dist[v]

      alt = dist[u] + weight
      if alt < dist[v]:
        dist[v] = alt
        Q[v] = alt

        prev[v] = u

  return dict(dist)[u], None

def shortest_path_lengths(start, adjacent_fn, goal=None):
  """ all destinations shortest path"""
  seen = set()
  Q = heapdict()
  dist = collections.defaultdict(lambda: 9999999999)

  dist[start] = 0
  Q[start] = 0

  while len(Q) != 0:
    (u, _) = Q.popitem()

    if goal and u == goal:
      return dist

    seen.add(u)

    for (v, weight) in adjacent_fn(u):
      if v in seen:
        continue
      Q[v] = dist[v]

      alt = dist[u] + weight
      if alt < dist[v]:
        dist[v] = alt
        Q[v] = alt

  return dist

def shortest_path_length(start, adjacent_fn, goal):
  """ single pair shortest path"""
  return shortest_path_lengths(start, adjacent_fn, goal)[goal]