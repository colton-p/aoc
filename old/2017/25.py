import collections


TAPE = collections.defaultdict(int)


def get(i):
  return TAPE[i]

def write(i, v):
  TAPE[i] = v


def fx(state, pos):
  value = get(pos)

  tx = {
    ('A', 0): (1, 1, 'B'),
    ('A', 1): (0, 1, 'F'),

    ('B', 0): (0, -1, 'B'),
    ('B', 1): (1, -1, 'C'),

    ('C', 0): (1, -1, 'D'),
    ('C', 1): (0, 1, 'C'),

    ('D', 0): (1, -1, 'E'),
    ('D', 1): (1, 1, 'A'),

    ('E', 0): (1, -1, 'F'),
    ('E', 1): (0, -1, 'D'),

    ('F', 0): (1, 1, 'A'),
    ('F', 1): (0, -1, 'E'),
  }
  return tx[(state, value)]



write(0, 0)
pos = 0
state = 'A'

for i in range(12425180):
  (value, dx, new_state) =  fx(state, pos)
  write(pos, value)
  pos += dx
  state = new_state

print sum(TAPE.values())
