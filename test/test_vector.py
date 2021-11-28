import unittest
import textwrap
import util

class TestVector(unittest.TestCase):
  def test_vscale(self):
    a = util.vscale((1,2,3), 4)

    self.assertEqual(a, (4, 8, 12))

  def test_vadd(self):
    a = util.vadd((1,2,3), (3, 2, 1))

    self.assertEqual(a, (4, 4, 4))

  def test_vsub(self):
    a = util.vsub((1,2,3), (3, 2, 1))

    self.assertEqual(a, (-2, 0, 2))

  def test_vop(self):
    a = util.vop((1,2,3), (1,2,3), lambda x,y: (x+y)*10)

    self.assertEqual(a, (20, 40, 60))
