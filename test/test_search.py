import unittest
import util.search as util

r"""
      A  
   /  |   \ 
  B   C   E 
 /|   |   |
D F   G   H
   \______/
"""
G = {
  'A': 'BCE',
  'B': 'ADF',
  'C': 'AG',
  'D': 'B',
  'E': 'AFH',
  'F': 'BEH',
  'G': 'C',
  'H': 'EF',
}

WG = {
  1: [(2, 7), (3,9), (6,14)],
  2: [(1, 7), (3,10), (4,15)],
  3: [(1, 9), (6,2), (2,10)],
  4: [(2, 15), (3,11), (5,6)],
  5: [(4,6), (6,9)],
  6: [(1,14), (3,2), (5,9)],
}

class TestSearch(unittest.TestCase):

  def test_shortest_path_lengths(self):
    dist = util.shortest_path_lengths(1, lambda x: WG[x])

    self.assertEqual(dist[4], 22)
    self.assertEqual(dist[5], 20)
    self.assertEqual(dist[6], 11)

  def test_shortest_path_length(self):
    dist = util.shortest_path_length(1, lambda x: WG[x], 4)

    self.assertEqual(dist, 22)

  def test_shortest_path(self):
    dist, path = util.shortest_path(1, lambda x: WG[x], 4)

    self.assertEqual(dist, 22)
    self.assertEqual(path, [1, 2, 4])

  def test_dfs(self):
    path, parents = util.dfs('A', lambda v: G[v])

    self.assertIsNone(path)
    self.assertEqual(['A', 'B', 'F'], util.construct_path('F', parents))
    self.assertEqual(['A', 'C', 'G'], util.construct_path('G', parents))
    self.assertEqual(['A'], util.construct_path('A', parents))
    self.assertEqual([], util.construct_path('X', parents))

  def test_dfs_with_goal_fn(self):
    path, _parents = util.dfs('A', lambda v: G[v], lambda v: v == 'H')
    self.assertEqual(['A', 'B', 'F', 'H'], path)

  def test_dfs_with_goal_label(self):
    path, _parents = util.dfs('A', lambda v: G[v], 'H')
    self.assertEqual(['A', 'B', 'F', 'H'], path)

  def test_bfs(self):
    path, parents = util.bfs('A', lambda v: G[v])

    self.assertIsNone(path)
    self.assertEqual(['A', 'B', 'F'], util.construct_path('F', parents))
    self.assertEqual(['A', 'C', 'G'], util.construct_path('G', parents))
    self.assertEqual(['A'], util.construct_path('A', parents))
    self.assertEqual([], util.construct_path('X', parents))

  def test_bfs_with_goal_fn(self):
    path, _parents = util.bfs('A', lambda v: G[v], lambda v: v == 'H')
    self.assertEqual(['A', 'E', 'H'], path)

  def test_bfs_with_goal_label(self):
    path, _parents = util.bfs('A', lambda v: G[v], 'H')
    self.assertEqual(['A', 'E', 'H'], path)

if __name__ == '__main__':
    unittest.main()