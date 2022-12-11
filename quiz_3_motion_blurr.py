import cv2
import numpy as np
from PIL import Image
from skimage.io import imread

img = imread('clock.tiff',0)
size = 7
l=10
kernal=np.zeros((size, size))
for i in range(-(size//2), (size//2)):
  for j in range(-(size//2), (size//2)):
    if(i*2 + j*2 <= l/2 and j!=0 and i/j == -1):
        kernal[i+size//2, j+size//2]=1/l
    else:
        kernal[i+size//2, j+size//2]=0
# print(kernal)
output = cv2.filter2D(img ,-1, kernal)
final_image = Image.fromarray(output)
final_image.show()