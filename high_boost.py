import numpy as np
from PIL import Image
from skimage.io import imread
z = imread("7.1.03.tiff")
output_img1 = imread("7.1.03.tiff")
l,m = z.shape[:]
row = l+2
coloumn = m+2
input_img = np.zeros((row,coloumn))
print(z.shape)
for i in range(l):
    for j in range(m):
        input_img[i+1,j+1]=z[i,j]
for x in range(1, l-1):
    for y in range(1, m-1):
        sum =input_img[x-1, y-1]/9+ input_img[x-1, y]/9+input_img[x-1, y+1]/9+input_img[x, y-1]/9+input_img[x, y]/9+input_img[x, y+1]/9+input_img[x+1, y-1]/9+input_img[x+1, y]/9+input_img[x+1, y+1]/9
        output_img1[x,y] = sum
mask = z-output_img1
final_output = mask+z
final_image1 = Image.fromarray(final_output)
final_image1.save("highboost.tiff")
final_image1.show()