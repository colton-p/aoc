import sys



L = list(line.strip() for line in open('25.in', 'r'))
def run(v):
  R = {'a': v, 'b':0, 'c':0, 'd':0}
  global L

  RET = []

  def val(x):
    try:
      return int(x)
    except ValueError:
      return R[x]

  count = 0
  pc = 0
  while pc < len(L) and len(RET) < 20:
    count += 1
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
    elif instr.startswith('out'):
      (_, dst) = instr.split()
      RET += [ R[dst] ]

    elif instr.startswith('jnz'):
      (_, dst, offset) = instr.split()
      offset = val(offset)
      if val(dst) != 0:
        pc += offset
        continue
    elif instr.startswith('tgl'):
      (_, offset) = instr.split()
      offset = val(offset)

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
      assert False, instr
    pc += 1
  return RET, count
  #for k in sorted(R.keys()):
  #  print k, R[k]

for i in range(10000):
  (r,c) = run(i)
  print i, c, r
  if r == [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0] or r == [0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1]:
    print i, r
    break
