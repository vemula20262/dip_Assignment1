import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("./clock.tiff", 0)

final = img
l = img.shape[0]
m = img.shape[1]

r = 10

img = img/img.max()

X = np.fft.fft2(img)

transform = np.zeros((l,m))

for i in range(l):
    for j in range(m):
      if( (i*i + j*j) <= 100 ):
        transform[i,j]= 1/(314)
      else:
        transform[i,j] = 0

H  = np.fft.fft2(transform)

Y = X*H

final = np.fft.ifft2(Y)

final = np.abs(final)

plt.figure(figsize=(8,8))
plt.imshow(final,cmap = "gray")
plt.axis("off")
plt.show()