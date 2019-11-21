import itertools

def transpose(rows):
  """
  >>> transpose([ [1, 2, 3], [4, 5, 6] ])
  [[1, 4], [2, 5], [3, 6]]
  """
  return [ [row[i] for row in rows] for i in range(len(rows[0]))]

def powerset(iterable):
  """
  >>> list(powerset([1,2,3]))
  [(), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
  """
  s = list(iterable)
  return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

def pairwise(iterable):
  """s -> (s0,s1), (s1,s2), (s2, s3), ...

  >>> list(pairwise([1, 2, 3, 4]))
  [(1, 2), (2, 3), (3, 4)]
  """
  a, b = itertools.tee(iterable)
  next(b, None)
  return zip(a, b)

def grouper(iterable, n, fillvalue=None):
  """Collect data into fixed-length chunks or blocks
  >>> list(grouper('ABCDEFG', 3, 'x'))
  [('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'x', 'x')]
  """
  args = [iter(iterable)] * n
  return itertools.zip_longest(fillvalue=fillvalue, *args)

def each_cons(iterable, n=2):
  """
  >>> each_cons([1,2,3,4,5], 3)
  [(1, 2, 3), (2, 3, 4), (3, 4, 5)]
  """
  iters = itertools.tee(iterable, n)
  for ix, it in enumerate(iters):
    for i in range(ix):
      next(it, None)
  return list(zip(*iters))

def each_slice(iterable, n=2):
  """
  >>> list(each_slice([1,2,3,4,5,6], 3))
  [(1, 2, 3), (4, 5, 6)]
  """
  return grouper(iterable, n, fillvalue=None)

def quantify(iterable, pred=bool):
  """
  Count how many times the predicate is true
  >>> quantify([1,2,3,4,5], lambda x: x%2==1)
  3
  >>> quantify([0,1,2])
  2
  >>> quantify([1,2,3,4,5], lambda x: x * 100)
  1500
  """
  return sum(map(pred, iterable))

if __name__ == '__main__':
  import doctest
  doctest.testmod()


