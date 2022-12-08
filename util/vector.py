import math
import operator

def vscale(v1, k):
  return tuple( k*x for x in v1)

def vadd(v1,v2):
  """
  >>> vadd([1,2,3], [10, 10, 20])
  (11, 12, 23)
  """
  assert len(v1) == len(v2)
  return tuple([(x+y) for (x,y) in zip(v1, v2)])

def vsub(v1,v2):
  """
  >>> vsub([10,20,30], [3, 2, 1])
  (7, 18, 29)
  """
  assert len(v1) == len(v2)
  return tuple([(x-y) for (x,y) in zip(v1, v2)])

def vop(v1, v2, op):
  """
  >>> vop([10,20,30], [3, 2, 1], operator.sub)
  (7, 18, 29)

  >>> vop([10,0,30], [1, 20, 3], max)
  (10, 20, 30)

  >>> vop([10,20,30], [1, 2, 3], lambda x, y: 100 * y - x)
  (90, 180, 270)
  """
  assert len(v1) == len(v2)

  return tuple([op(x,y) for (x,y) in zip(v1, v2)])

def vdist1(pt1, pt2):
  """
  >>> vdist1([10,10,10], [11, 12, 15])
  8
  >>> vdist1([10,10,10], [12, 8, 10])
  4
  """
  assert len(pt1) == len(pt2)
  return sum([abs(x-y) for (x,y) in zip(pt1, pt2)])

def vdist2(pt1, pt2):
  """
  >>> vdist2([14,13,10], [10, 10, 10])
  5.0
  >>> vdist2([10,10,10], [11, 9, 10])
  1.4142135623730951
  """
  assert len(pt1) == len(pt2)
  return math.dist(pt1, pt2)

def vdistn(pt1, pt2, k=2):
  """
  >>> vdistn([10,10,10], [12, 10, 10], 3)
  2.0
  >>> vdistn([10,10,10], [12, 7, 10], 3)
  3.2710663101885897
  """
  assert len(pt1) == len(pt2)
  s = sum([abs(x-y)**k for (x,y) in zip(pt1, pt2)])
  return math.pow(s, 1.0/k)



if __name__ == '__main__':
  import doctest
  doctest.testmod()


