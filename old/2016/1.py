


with open('1.in', 'r') as f:
  lines = [line.strip() for line in f]


(line,) = lines

steps = line.split(', ')
print steps
