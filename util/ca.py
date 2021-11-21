# Celluar automata
from collections import defaultdict
import itertools

from util import grid

class CA2:
    # TODO: should compose with grid
    def __init__(self, rows, survival=[2, 3], birth=[3], border=None, max_x=None, max_y=None):
        # TODO: options
        # neighborhood = moore, vn
        # borders = wrap unbounded hard
        # sparse?

        self.ALIVE = '#'
        self.DEAD = '.'
        self.survival = survival
        self.birth = birth
        self.border_type = border

        self.max_x = max_x
        self.max_y = max_y

        self.grid = defaultdict(lambda: self.DEAD)
        for (j, row) in enumerate(rows):
            for (i, v) in enumerate(row):
                if v == self.ALIVE or border is not None:
                    self.grid[(i, j)] = v
        if self.max_x is None:
            self.max_x = max(self.grid.keys(), key=lambda x: x[0])[0]
            self.max_y = max(self.grid.keys(), key=lambda x: x[1])[1]

    def evolve(self, n=1):
        for _i in range(n):
            self._evolve()

    def _evolve(self):
        child = defaultdict(lambda: self.DEAD)
        to_evolve = set(itertools.chain(
            *[self.neighborhood(pt) for pt in self.grid.keys()]))
        for pt in to_evolve:
            nadj = self.living_neighbours(pt)
            if self.grid[pt] == self.ALIVE and nadj in self.survival:
                child[pt] = self.ALIVE
            elif self.grid[pt] == self.DEAD and nadj in self.birth:
                child[pt] = self.ALIVE
            else:
                pass
                # child[pt] = self.DEAD
        self.grid = child

    def number_alive(self):
        return sum(1 for v in self.grid.values() if v == self.ALIVE)

    def living_cells(self):
        return [k for k, v in self.grid.items() if v == self.ALIVE]

    def living_neighbours(self, pt):
        return sum(1 for i in self.neighborhood(pt) if self.grid[i] == self.ALIVE)

    def neighborhood(self, pt):
        if self.border_type is None:
            return grid.rect_adj(pt, diag=True)
        if self.border_type == 'hard':
            return grid.rect_adj_bounds(pt, 0, self.max_x, 0, self.max_y, diag=True)
        if self.border_type == 'wrap':
            bounds = grid.rect_adj(pt, diag=True)
            return (((1+self.max_x+x) % (1+self.max_x), (1+self.max_y+y) % (1+self.max_y)) for (x, y) in bounds)

    def print(self):
        g = grid.Grid([])
        g.grid = self.grid
        if (0, 0) not in g.grid:
            g.grid[(0, 0)] = '.'
        if (self.max_x, self.max_y) not in g.grid:
            g.grid[(self.max_x, self.max_y)] = '.'
        g.print()
