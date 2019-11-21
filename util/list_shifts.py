
def rotate_string(s, n=13):
  """ROT-13 encoding

  >>> rotate_string('abc-KLM')
  'nop-XYZ'
  >>> rotate_string('abc', 3)
  'def'
  """

  a = 'abcdefghijklmnopqrstuvwxyz'
  A = a.upper()

  def f(c):
    if c not in a+A:
      return c
    if c in a:
      return a[(a.index(c) + n) % len(a)]
    if c in A:
      return A[(A.index(c) + n) % len(A)]

  return ''.join([f(c) for c in s])

def head(L, n):
  """
  >>> head([1,2,3,4,5], 2)
  [1, 2]
  >>> head([1,2, 3], 100)
  [1, 2, 3]
  """
  return L[:n]

def tail(L, n):
  """
  >>> tail([1,2,3,4,5], 2)
  [4, 5]
  >>> tail([1], 2)
  [1]
  """
  return L[-n:]

def rotate_right(L, k):
  """
  >>> rotate_right([1, 2, 3, 4], 1)
  [4, 1, 2, 3]
  """
  return L[-k:] + L[:-k]

def rotate_left(L, k):
  """
  >>> rotate_left([1, 2, 3, 4], 1)
  [2, 3, 4, 1]
  """
  return L[k:] + L[:k]

def insert_after(L, ix, val):
  """
  >>> insert_after([1, 2, 3, 4], 2, 'X')
  [1, 2, 3, 'X', 4]
  """
  return L[:ix+1] + [val] + L[ix+1:]

def insert_before(L, ix, val):
  """
  >>> insert_before([1, 2, 3, 4], 2, 'X')
  [1, 2, 'X', 3, 4]
  """
  return L[:ix] + [val] + L[ix:]

def join(it, sep=''):
  """
  >>> join(['1', '2', '3'], '-')
  '1-2-3'
  """
  return sep.join(it)

if __name__ == '__main__':
  import doctest
  doctest.testmod()


