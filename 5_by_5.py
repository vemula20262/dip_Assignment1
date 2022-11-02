import numpy as np
from PIL import Image
from skimage.io import imread

z = imread("ruler.512_2.tiff")
output_img1 = imread("ruler.512_2.tiff")
output_img2 = imread("ruler.512_2.tiff")
l, m = z.shape[:]
print(z)
print(z.shape)
row = l+4
coloumn = m+4
input_img = np.zeros((row,coloumn))
print(z.shape)
for i in range(l):
    for j in range(m):
        input_img[i+2,j+2]=z[i,j]
print(input_img)
print(input_img.shape)
for x in range(2, l - 1):
    for y in range(2, m - 1):
        sum = input_img[x - 1, y - 1] / 25 + input_img[x - 1, y] / 25 + input_img[x - 1, y + 1] / 25 + input_img[x, y - 1] / 25 + input_img[x, y] / 25 + \
              input_img[x, y + 1] / 25 + input_img[x + 1, y - 1] / 25 + input_img[x + 1, y] / 25 + input_img[x + 1, y + 1] / 25 + input_img[
                  x - 2, y - 2] / 25 + input_img[x - 2, y - 1] / 25 + input_img[x - 2, y] / 25 + input_img[x - 2, y + 1] / 25 + input_img[
                  x - 2, y + 2] / 25 + input_img[x + 2, y + 2] / 25 + input_img[x + 2, y + 1] / 25 + input_img[x + 2, y] / 25 + input_img[
                  x + 2, y - 1] / 25 + input_img[x + 2, y - 2] / 25 + input_img[x - 1, y + 2] / 25 + input_img[x, y + 2] / 25 + input_img[
                  x + 1, y + 2] / 25 + input_img[x - 1, y - 2] / 25 + input_img[x, y - 2] / 25 + input_img[x + 1, y - 2] / 25
        list = [input_img[x - 1, y - 1], input_img[x - 1, y], input_img[x - 1, y + 1], input_img[x, y - 1], input_img[x, y], input_img[x, y + 1],
                input_img[x + 1, y - 1], input_img[x + 1, y], input_img[x + 1, y + 1], input_img[x - 2, y - 2], input_img[x - 2, y - 1], input_img[x - 2, y],
                input_img[x - 2, y + 1], input_img[x - 2, y + 2], input_img[x + 2, y + 2], input_img[x + 2, y + 1], input_img[x + 2, y], input_img[x + 2, y - 1],
                input_img[x + 2, y - 2], input_img[x - 1, y + 2], input_img[x, y + 2], input_img[x + 1, y + 2], input_img[x - 1, y - 2], input_img[x, y - 2],
                input_img[x + 1, y - 2]]
        list.sort()
        output_img1[x,y]=sum
        output_img2[x, y] = list[12]

        # new_im1[x][y] = avg1
final_image1 = Image.fromarray(output_img1)
final_image1.save("mean_55.tiff")
final_image1.show()
final_image2 = Image.fromarray(output_img2)
final_image2.save("median_55.tiff")
final_image2.show()
