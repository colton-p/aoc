print(__doc__)


# Code source: Gaël Varoquaux
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause

import numpy as np


from sklearn.cluster import KMeans
from sklearn import datasets

np.random.seed(5)

iris = datasets.load_iris()
X = iris.data
y = iris.target

estimators = [
              ('k_means_iris_3', KMeans(n_clusters=8))]


X = [
]
Y = []
print(X)

import os

for fname in os.listdir('.'):
  if not fname.endswith('.in'):
    continue
  with open(fname, 'r') as f:
    r = f.read()[:100]

    if not r:
      continue
    r += "\0" * 100
    r = r[:100]

    X += [ [ord(c) for c in r] ]
    Y += [fname]

for name, est in estimators:
    est.fit(X)
    labels = est.labels_
    for (a,b,c) in zip(Y, est.labels_, X):
      print('---- %s (%s) ---' % (b, a))
      print(''.join(chr(cc) for cc in c))
      print('---')

    #ax.scatter(X[:, 3], X[:, 0], X[:, 2],
    #           c=labels.astype(np.float), edgecolor='k')


