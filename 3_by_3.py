import numpy as np
from PIL import Image
from skimage.io import imread
z = imread("ruler.512_2.tiff")
output_img1 = imread("ruler.512_2.tiff")
output_img2 = imread("ruler.512_2.tiff")
l,m = z.shape[:]
row = l+2
coloumn = m+2
input_img = np.zeros((row,coloumn))
print(z.shape)
for i in range(l):
    for j in range(m):
        input_img[i+1,j+1]=z[i,j]
# print(input_img.shape)
# print(input_img)
for x in range(1, l-1):
    for y in range(1, m-1):
        sum =input_img[x-1, y-1]/9+ input_img[x-1, y]/9+input_img[x-1, y+1]/9+input_img[x, y-1]/9+input_img[x, y]/9+input_img[x, y+1]/9+input_img[x+1, y-1]/9+input_img[x+1, y]/9+input_img[x+1, y+1]/9
        list = [input_img[x-1, y-1],input_img[x-1, y],input_img[x-1, y+1],input_img[x, y-1],input_img[x, y],input_img[x, y+1],input_img[x+1, y-1],input_img[x+1, y],input_img[x+1, y+1]]
        list.sort()

        output_img1[x,y] = sum
        output_img2[x,y] = list[4]

        # new_im1[x][y] = avg1
print(output_img1)
print(output_img2)
final_image = Image.fromarray(output_img1)
final_image.save("mean_33.tiff")
final_image.show()
final_image2 = Image.fromarray(output_img2)
final_image2.save("median_33.tiff")
final_image2.show()
