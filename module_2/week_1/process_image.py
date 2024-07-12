import matplotlib.image as mpimg
import numpy as np

img = mpimg.imread('dog.jpeg')

# Three ways to convert an image to grayscale
gray_img_01 = (np.max(img, axis=2) + np.min(img, axis=2)) / 2
gray_img_02 = np.mean(img, axis=2)
gray_img_03 = np.dot(img[..., :3], [0.21, 0.72, 0.07])

print(f'gray_img_01 shape: {gray_img_01[0, 0]}')
print(f'gray_img_02 shape: {gray_img_02[0, 0]}')
print(f'gray_img_03 shape: {gray_img_03[0, 0]}')