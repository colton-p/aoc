import unittest
import textwrap
import util

glider = textwrap.dedent("""
    .#.
    ..#
    ###
""").strip().split('\n')

class TestCA2(unittest.TestCase):
    def test_blinker(self):
        blinker = textwrap.dedent("""
            .....
            .....
            .###.
            .....
            .....
        """)
        
        ca = util.CA2(blinker.strip().split('\n'))
        original_cells = sorted(ca.living_cells())

        ca.evolve()
        self.assertEqual(ca.number_alive(), 3)

        ca.evolve()
        self.assertEqual(ca.number_alive(), 3)
        self.assertEqual(sorted(ca.living_cells()), original_cells)

    def test_beacon(self):
        beacon = textwrap.dedent("""
            ......
            .##...
            .##...
            ...##.
            ...##.
            ......
        """)
        
        ca = util.CA2(beacon.strip().split('\n'))
        original_cells = sorted(ca.living_cells())

        ca.evolve()
        self.assertEqual(ca.number_alive(), 6)

        ca.evolve()
        self.assertEqual(ca.number_alive(), 8)
        self.assertEqual(sorted(ca.living_cells()), original_cells)

    def test_glider(self):
        ca = util.CA2(glider)

        for i in range(20):
            ca.evolve()
            self.assertEqual(ca.number_alive(), 5)

    def test_glider_long(self):
        ca = util.CA2(glider)

        ca.evolve(1000)

        self.assertEqual(ca.number_alive(), 5)

    def test_glider_wrap(self):
        ca = util.CA2(glider, border='wrap', max_x=4, max_y=4)
        original_cells = sorted(ca.living_cells())

        ca.evolve(20)

        self.assertEqual(sorted(ca.living_cells()), original_cells)
    
    def test_hard_border_empty(self):
        ca = util.CA2([['.', '.'], ['.', '.']], border='hard')

        self.assertEqual(ca.max_x, 1)

    def test_highlife_replicator(self):
        replicator = textwrap.dedent("""
            .......
            ...###.
            ..#..#.
            .#...#.
            .#..#..
            .###...
            .......
        """)
        ca = util.CA2(replicator.strip().split('\n'), survival=[2, 3], birth=[3, 6])
        self.assertEqual(ca.number_alive(), 12)

        ca.evolve(12)
        self.assertEqual(ca.number_alive(), 24)

        ca.evolve(12)
        self.assertEqual(ca.number_alive(), 24)

        ca.evolve(12)
        self.assertEqual(ca.number_alive(), 48)




if __name__ == '__main__':
    unittest.main()