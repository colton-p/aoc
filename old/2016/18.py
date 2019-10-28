start = '.^^.^.^^^^'
start = '.^^^.^.^^^^^..^^^..^..^..^^..^.^.^.^^.^^....^.^...^.^^.^^.^^..^^..^.^..^^^.^^...^...^^....^^.^^^^^^^'



N = len(start)
it = range(len(start))
def f(line):
  out = ''
  line = '.' + line + '.'
  c = 0
  for i in it:
    s = line[i:i+3]
    if s in ['^^.', '.^^', '^..', '..^']:
      out += '^'
    else:
      out += '.'
      c += 1
  return out, c

c = 0
line = str(start)
for i in xrange(400*1000):
  #print line
  #c += sum([1 for c in line if c == '.'])
  line,dc = f(line)
  c += dc
print c
