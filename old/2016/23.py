from collections import defaultdict






R = {'a': 8, 'b':0, 'c':0, 'd':0}
R['c'] = 1

L = list(line.strip() for line in open('22.in', 'r'))

def val(x):
  try:
    return int(x)
  except ValueError:
    return R[x]

pc = 0
while pc < len(L):
  instr = L[pc]
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
    offset = val(offset)
    if val(dst) != 0:
      pc += offset
      continue
  elif instr.startswith('tgl'):
    (_, offset) = instr.split()
    offset = val(offset)


    print instr, R
    if pc + offset < len(L) and pc+offset >= 0:
      tgt = L[pc + offset]


      if tgt.startswith('inc'):
        L[pc+offset] = tgt.replace('inc', 'dec')
      elif tgt.startswith('dec'):
        L[pc+offset] = tgt.replace('dec', 'inc')
      elif tgt.startswith('jnz'):
        L[pc+offset] = tgt.replace('jnz', 'cpy')
      elif tgt.startswith('cpy'):
        L[pc+offset] = tgt.replace('cpy', 'jnz')
      elif tgt.startswith('tgl'):
        L[pc+offset] = tgt.replace('tgl', 'inc')
      else:
        assert False, line

  else:
    assert False, line
  pc += 1

for k in sorted(R.keys()):
  print k, R[k]
