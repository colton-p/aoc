import hashlib

def hash_digest(x, algo='md5'):
  """Hash hexdigest

  >>> hash_digest("The quick brown fox jumps over the lazy dog")
  '9e107d9d372bb6826bd81d3542a419d6'
  """
  h = hashlib.new(algo)
  h.update(x.encode())
  return h.hexdigest()

def hash_func(algo='md5'):
  """Hash as one-arg function
  >>> hash_func()("The quick brown fox jumps over the lazy dog")
  '9e107d9d372bb6826bd81d3542a419d6'
  """
  return lambda x: hash_digest(x, algo)

if __name__ == '__main__':
  import doctest
  doctest.testmod()


