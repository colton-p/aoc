import collections
import itertools
import networkx as nx

# TODO: make pt in G work
# TODO: count adj
# TODO: beam iterator
# TODO: row major, col major iterators


class Grid:
  """
  Grids are left-to-right, top-to-bottom
      01234
      x--->
    y 0.....
    | 1.....
    | 2.....
    v 3.....
  """
  # TODO: sum adj
  @classmethod
  def from_string(cls, string, sep='\n', **kwargs):
      return cls.from_rows(string.split(sep), **kwargs)
  
  @classmethod
  def from_dict(cls, dict):
    return cls(dict)
  
  @classmethod
  def from_grid(cls, grid):
    return cls(grid.dict, default=grid.default, border_type=grid.border_type)

  @classmethod
  def from_rows(cls, rows, **kwargs):
    grid = {} 
    for (j, row) in enumerate(rows):
      for (i, v) in enumerate(row):
        grid[(i,j)] = v
    return cls(grid, **kwargs)

  def __init__(self, grid, default='.', border_type=False, bounds='deduce'):
    if border_type:
      self.grid = dict(grid)
    else:
      self.grid = collections.defaultdict(lambda: default, grid)

    self.default = default
    self.border_type = border_type
    self._min_x = self._min_y = self._max_x = self._max_y = None
    
  def __getitem__(self, key):
    return self.grid[key]

  def __setitem__(self, key, value):
    self.grid[key] = value
  

  def adj_k(self, pt, diag=True):
    """ adjacent positions"""
    return list(self.neighborhood(pt, diag=diag).keys())
  def adj_v(self, pt, diag=True):
    """adjacent values"""
    return list(self.neighborhood(pt, diag=diag).values())

  def neighborhood(self, pt, diag=True):
    """
    dictionary of adjacent cells
    """
    # TODO: wrap
    if self.border_type == 'hard':
      return {x: self[x] for x in rect_adj_bounds(pt, 0, self.max_x(), 0, self.max_y(), diag=diag)}
    else:
      return {x: self[x] for x in rect_adj(pt, diag=diag)}

  
  def min_x(self):
    if not self._min_x:
      self._min_x = min(self.grid.keys(), key=lambda x:x[0])[0]
    return self._min_x
  def min_y(self):
    if not self._min_y:
      self._min_y = min(self.grid.keys(), key=lambda x:x[1])[1]
    return self._min_y
  def max_x(self):
    if not self._max_x:
      self._max_x = max(self.grid.keys(), key=lambda x:x[0])[0]
    return self._max_x
  def max_y(self):
    if not self._max_y:
      self._max_y = max(self.grid.keys(), key=lambda x:x[1])[1]
    return self._max_y

  def dims(self):
    return (self.ncols(), self.nrows())
  def nrows(self):
    return self.max_y() - self.min_y() + 1
  def ncols(self):
    return self.max_x() - self.min_x() + 1

  def recenter(self):
    (dx, dy) = (-self.min_x(), -self.min_y())
    return self.translate(dx, dy)

  def translate(self, dx, dy):
    return self.transform(lambda x, y: (x+dx, y+dy))

  def rotate_right(self):
    return self.transform(lambda x,y: (-y, x))
  def rotate_left(self):
    return self.transform(lambda x,y: (y, -x))
  def rotate_180(self):
    return self.transform(lambda x,y: (-x, -y))
  def flip_horizontal(self):
    return self.transform(lambda x,y: (-x, y))
  def flip_vertical(self):
    return self.transform(lambda x,y: (x, -y))
  def transpose(self):
    return self.transform(lambda x,y: (y, x))
  def transpose_antidiagonal(self):
    return self.transform(lambda x,y: (-y, -x))
  
  def all_rotations(self):
    yield Grid(dict(self.grid))
    yield Grid(dict(self.grid)).rotate_right()
    yield Grid(dict(self.grid)).rotate_left()
    yield Grid(dict(self.grid)).rotate_180()

  def all_orientations(self):
    yield Grid(dict(self.grid))
    yield Grid(dict(self.grid)).rotate_right()
    yield Grid(dict(self.grid)).rotate_left()
    yield Grid(dict(self.grid)).rotate_180()
    yield Grid(dict(self.grid)).flip_vertical()
    yield Grid(dict(self.grid)).flip_horizontal()
    yield Grid(dict(self.grid)).transpose()
    yield Grid(dict(self.grid)).transpose_antidiagonal()
  
  def transform(self, func):
    new_grid = {}
    for (x,y) in self.grid:
      new_grid[func(x,y)] = self.grid[(x,y)]
    self.grid = new_grid
    return self
  
  def subgrid(self, x0, y0, nx, ny):
    g = {}
    for (x,y) in itertools.product(
      range(x0, x0 + nx),
      range(y0, y0 + ny)
    ):
      g[(x,y)] = self[(x,y)]
    return Grid(g)
      
  def subgrids(self, nx, ny):
    for (x0, y0) in itertools.product(
      range(self.min_x(), self.max_x(), nx),
      range(self.min_y(), self.max_y(), ny)
    ):
      yield ((x0 // nx, y0 // ny), self.subgrid(x0, y0, nx, ny))
      

  def count(self, val):
    return sum(1 for v in self.grid.values() if v == val)
  
  def to_s(self, sep='\n', cell_size=1):
    grid = self.grid
    max_x = max(grid.keys(), key=lambda x:x[0])[0]
    max_y = max(grid.keys(), key=lambda x:x[1])[1]

    min_x = min(grid.keys(), key=lambda x:x[0])[0]
    min_y = min(grid.keys(), key=lambda x:x[1])[1]

    s = ''
    cell_fmt = f'%{cell_size}s'
    for j in range(min_y, max_y+1):
      for i in range(min_x, max_x+1):
        s += cell_fmt % (grid[(i,j)])
      s += sep
    return s[:-1]
  
  def print(self):
    print(self.to_s())
  
  def to_nx(self, passable=None, impassable=None):
    graph = nx.Graph()

    if impassable is None:
      impassable = set(self.grid.values()) - set(passable)
    else:
      impassable = set(impassable)

    for k,v in self.grid.items():
      if v in impassable: continue
      graph.add_node(k, label=v)
    
    for k,v in self.grid.items():
      if v in impassable: continue
      for adj_k, adj_v in self.neighborhood(k, diag=False).items():
        if adj_v in impassable: continue
        graph.add_edge(k, adj_k)

    return graph

class GridIterators:
  @classmethod
  def spiral(cls, origin=(0,0), direction='ccw'):
    pt = origin
    yield pt

    step = 1
    d = (1,0)



    while True:
      for _i in range(step):
        pt = (pt[0] + d[0], pt[1]+d[1])
        yield pt
      #d = (-d[1], d[0]) # 90deg
      d = (d[1], -d[0]) # 90deg

      for _i in range(step):
        pt = (pt[0] + d[0], pt[1]+d[1])
        yield pt
      #d = (-d[1], d[0]) # 90deg
      d = (d[1], -d[0]) # 270deg

      step += 1





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
      s += '%1.1s' % (grid[(i,j)])
    s += "\n"
  return s.strip()

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

