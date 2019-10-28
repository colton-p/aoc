from collections import defaultdict






R = defaultdict(int)
R['c'] = 1

L = list(line.strip() for line in open('12.in', 'r'))

def val(x):
  try:
    return int(x)
  except ValueError:
    return R[x]

pc = 0
while pc < len(L):
  instr = L[pc]
  #print instr, R
  if instr.startswith('cpy'):
    (_, src, dst) = instr.split()
    R[dst] = val(src)
  elif instr.startswith('inc'):
    (_, dst) = instr.split()
    R[dst] += 1
  elif instr.startswith('dec'):
    (_, dst) = instr.split()
    R[dst] -= 1

  elif instr.startswith('jnz'):
    (_, dst, offset) = instr.split()
    offset = int(offset)
    if val(dst) != 0:
      pc += offset
      continue
  else:
    assert False, line
  pc += 1

for k in sorted(R.keys()):
  print k, R[k]
