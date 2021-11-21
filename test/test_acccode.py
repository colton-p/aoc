import unittest
import util.acccode as a
import util.input as input

EX_S ="""nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""

iobj = input.Input(EX_S.split("\n"))
EX = iobj.tuples()


class TestAccCode(unittest.TestCase):

  def test_works(self):
    (state, acc) = a.AccCode.go(EX)

    self.assertEqual(acc, 5)
    self.assertEqual(state, 'cycled')

  def test_flip_cylce(self):
    p = a.AccCode(EX)
    p.flip_op(0)
    p.run()

    self.assertEqual(p.state, 'cycled')
    self.assertEqual(p.acc, 0)

  def test_halts(self):
    p = a.AccCode(EX)
    p.flip_op(-2)
    p.run()

    self.assertEqual(p.state, 'halted')
    self.assertEqual(p.acc, 8)




if __name__ == '__main__':
    unittest.main()