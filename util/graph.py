import networkx as nx

def path_weight(G, path):
  return sum(G[s][t]['w'] for (s,t) in __pairwise(path))





# TODO: fix these imports???
import itertools
def __pairwise(iterable):
  """s -> (s0,s1), (s1,s2), (s2, s3), ...

  >>> list(pairwise([1, 2, 3, 4]))
  [(1, 2), (2, 3), (3, 4)]
  """
  a, b = itertools.tee(iterable)
  next(b, None)
  return zip(a, b)



if __name__ == '__main__':
  import doctest
  doctest.testmod()


