R = [0, 0, 0, 0, 0, 16]

cnt = 0

S = set()
while True:
  cnt+=1
  #print '1', R
  R[3] = 65536 | R[4]
  R[4] = 4332021

  while True:
    #print '1.1', R


    R[4] += (R[3] & 255)
    R[4] = R[4] & 16777215
    R[4] *= 65899
    R[4] = R[4] & 16777215
    #print '2', R

    if 256 > R[3]:
      break

    #R[2] = 0
    #while True:
    #  R[1] = 256 * (R[2] + 1)
    #  if R[1] > R[3]:
    #    break
    #  R[2] +=1
    #print '3', R
    #R[3] = R[2]

    R[3] = R[3] / 256

  print cnt, R[3], R[4]
  if R[4] in S:
    print '!!!'
    print R[4]
    break
  S.add(R[4])
  if R[4] == R[0]:
    exit()

