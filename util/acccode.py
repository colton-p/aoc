
class AccCode:
  @classmethod
  def go(cls, listing, input=None, ret=0):
    pp = AccCode(listing, input)
    pp.run()

    return (pp.state, pp.acc)

  def __init__(self, listing, input=None):
    self.listing = list(listing)
    self.original_listing = tuple(listing)

    self.pc = 0
    self.acc = 0
    self.state = 'running'

    self.executed = set()
  
  def flip_op(self, ix):
    (op, val) = self.listing[ix]
    if op == 'jmp':
      self.listing[ix] = ('nop', val)
    elif op == 'nop':
      self.listing[ix] = ('jmp', val)
    else:
      pass
  
  def run(self):
    while self.run_one():
      pass

    return self.acc

  def run_one(self):
    (op, val) = self.listing[self.pc]

    if op == 'acc':
      self.acc += val
      self.pc += 1
    elif op == 'jmp':
      self.pc += val
    elif op == 'nop':
      self.pc += 1
    else:
      assert False, self.listing[self.pc]

    # halt: pc off end
    if self.pc >= len(self.listing):
      self.state = 'halted'
      return False

    # cycle detected
    if self.pc in self.executed:
      self.state = 'cycled'
      return False
    self.executed.add(self.pc)

    return True