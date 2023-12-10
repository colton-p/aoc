from fractions import Fraction
import itertools as its
import math
from util import Input

YEAR = 2023
DAY = 9
iobj = Input.for_date(DAY, year=YEAR, test=0)
rows = list(iobj.rows)

class Poly:
  def __init__(self, coeffs) -> None:
    deg = max(
      ix for (ix, v) in enumerate(coeffs)
      if ix == 0 or v != 0
    )

    self.coeffs = coeffs[:deg+1]
  
  def __str__(self) -> str:
    return str(tuple(self.coeffs))
  
  def eval(self, x):
    return sum(c * x**i for (i,c) in enumerate(self.coeffs))

  @property
  def degree(self):
    return len(self.coeffs) - 1
  
  def __add__(self, oth):
    assert isinstance(oth, Poly), oth

    h_i = [
      f + g for (f, g) in
      its.zip_longest(self.coeffs, oth.coeffs, fillvalue=0)
    ]

    return Poly(h_i)

  def __mul__(self, oth):
    assert isinstance(oth, Poly), oth

    deg = self.degree + oth.degree
    h = [0 for _ in range(deg + 1)]
    for (i, f) in enumerate(self.coeffs):
      for (j, g) in enumerate(oth.coeffs):
        h[i + j] += f*g

    return Poly(h)
  
def lagrange_basis(j, x):
  # (x - x_i)
  binoms = [Poly([-x_i, 1]) for (i, x_i) in enumerate(x) if i != j]
  
  return math.prod(binoms, start=Poly([1]))

def lagrange_weight(j, x):
  # (x_j - x_i)
  weights = [ x[j] - x_i for (i, x_i) in enumerate(x) if i != j]
  return math.prod(weights)

def lagrange_poly(y, x):
  L = Poly([0])
  for (j, y_i) in enumerate(y):
    l_i = lagrange_basis(j, x)
    w_i = lagrange_weight(j, x)
  
    # y_i / w_i * l_i
    L += (Poly([Fraction(y_i , w_i)]) * l_i)
  
  return L

def main():
  points = [
    tuple(int(v) for v in line.split(' '))
    for line in rows
  ]
  polys = [ lagrange_poly(y, range(len(y))) for y in points ]

  def part1():
    values = [poly.eval(len(pts)) for (poly, pts) in zip(polys, points)]
    print(max(p.degree for p in polys))
    print(max(values))

    return sum(values)

  def part2():
    values = [poly.eval(-1) for poly in polys]
    print(max(values))

    return sum(values)

  print('P1', part1())
  print('P2', part2())
main()