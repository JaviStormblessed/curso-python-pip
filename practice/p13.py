x = [[2, 7, 3], [4, 5, 6], [7, 8, 9]]
y = [[5, 8, 1], [6, 7, 3], [4, 5, 9]]

z = list()
temp = list()

for i in range(3):
    temp=[]
    for j in range(3):
        temp.append(x[i][j]+y[i][j])
    z.append(temp)

for i in z:
    print(i)

import numpy as np
if  x.shape[1] == y.shape[0]:
    C = np.zeros((x.shape[0],y.shape[1]),dtype = int)
    for row in range(rows): 
        for col in range(cols):
            for elt in range(len(B)):
              C[row, col] += x[row, elt] * y[elt, col]
    print(C)