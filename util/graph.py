import networkx as nx



def tsp(G):
  paths = itertools.permutations(G)

  for path in paths:
    p, W = None, 9999999
    for (s,t) in pairwise(path):
      edge = G[s][t]
      if 'w' in edge:
        w += e['w']

    if w < W:
      p, W = path, w

  return w, p




if __name__ == '__main__':
  import doctest
  doctest.testmod()


