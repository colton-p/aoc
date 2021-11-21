import collections
import os

from util.input_stats import InputStats


def files():
    for path in sorted(os.listdir('inputs')):
        if path.endswith('.txt'):# and path == '2015-2.txt':
            yield path


def inputs():
    for path in files():
        with open('inputs/'+path, 'r') as datafile:
            data = [line.strip() for line in datafile]
        yield (path, InputStats(data))

C = collections.Counter()
for (path, i) in inputs():
    (kind, extra) = i.guess_kind()
    C[kind] += 1
    print(path[:-4], kind, extra)

print()
for k in C:
    print(k, C[k])

print(sum(C.values())- C[None])
