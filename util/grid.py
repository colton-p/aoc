"""
Grids are left-to-right, top-to-bottom
     01234
     x--->
  y 0.....
  | 1.....
  | 2.....
  v 3.....
"""


def rows_to_grid(rows):
  """
     01234
     x--->
  y 0.....
  | 1.....
  | 2.....
  v 3.....

  >>> rows_to_grid([ [1, 2, 3], [4, 5, 6] ])
  {(0, 0): 1, (1, 0): 2, (2, 0): 3, (0, 1): 4, (1, 1): 5, (2, 1): 6}
  """
  grid = {}
  for (j, row) in enumerate(rows):
    for (i, v) in enumerate(row):
      grid[(i,j)] = v
  return grid


def grid_to_string(grid):
  """
  >>> grid_to_string(rows_to_grid([ [1, 2, 3], [4, 5, 6] ]))
  '123\\n456'
  """
  max_x = max(grid.keys(), key=lambda x:x[0])[0]
  max_y = max(grid.keys(), key=lambda x:x[1])[1]

  min_x = min(grid.keys(), key=lambda x:x[0])[0]
  min_y = min(grid.keys(), key=lambda x:x[1])[1]

  s = ''
  for j in range(min_y, max_y+1):
    for i in range(min_x, max_x+1):
      s += '%1s' % (grid[(i,j)])
    s += "\n"
  return s#.strip()

def print_grid(grid):
  print(grid_to_string(grid))

def rect_adj(pt, diag=False):
  """
  >>> list(rect_adj((0,0)))
  [(0, 1), (0, -1), (1, 0), (-1, 0)]

  >>> list(rect_adj((0,0), diag=True))
  [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
  """
  (x,y) = pt
  for (i,j) in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
    yield (x+i, y+j)
  if diag:
    for (i,j) in [(1, 1), (1, -1), (-1, 1), (-1, -1)]:
      yield (x+i, y+j)

def rect_adj_bounds(pt, min_x, max_x, min_y, max_y, diag=False):
  """
  >>> list(rect_adj_bounds((0,0), 0, 100, 0, 100))
  [(0, 1), (1, 0)]
  >>> list(rect_adj_bounds((0,0), 0, 100, 0, 100, diag=True))
  [(0, 1), (1, 0), (1, 1)]
  >>> list(rect_adj_bounds((20,100), 0, 100, 0, 100))
  [(20, 99), (21, 100), (19, 100)]
  """
  for (x, y) in rect_adj(pt, diag):
    if min_x <= x <= max_x and min_y <= y <= max_y:
      yield (x,y)


if __name__ == '__main__':
  import doctest
  doctest.testmod()

