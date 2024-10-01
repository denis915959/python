import numpy as np
def conv(M, k, col=1): # convolution by definition (filter as tensor)
  kh, kw = k.shape[0:2]
  h_, w_ = M.shape[0:2]
  h, w = (h_ - kh + 1, w_ - kw + 1)
  out = np.zeros((h, w))
  for y in range(h):
    for x in range(w):
      for i in range(kh):
        for j in range(kw):
          if col == 1:
            out[y][x] += M[y+i][x+j] * k[i][j]
          else:
            for c in range(col):
              out[y][x] += M[y+i][x+j][c] * k[i][j][c]
  return out

X = np.ones((3, 3, 5))
print(X.shape)
print("X:")
print(X)
print("Первый фильтр")
k1 = np.array([[0, 1, 0],
               [1, 0, -1],
               [0, -1, 0]])
k1 = np.stack((k1, k1, k1, k1, k1), axis=2) #глубина 5, тензор 5-тиканальный
print(k1.shape)

res = conv(X, k1, col=5)
print(res.shape)
print(res)
###########################################################
print("Второй фильтр")
k2 = np.array([[0, 2, 0],
               [2, 0, -2],
               [0, -2, 0]])
k2 = np.stack((k2, k2, k2, k2, k2), axis=2)
print(k2.shape)

res = conv(X, k2, col=5)
print(res.shape)
print(res)