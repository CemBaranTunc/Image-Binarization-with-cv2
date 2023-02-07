#This project has aimed to reduce the size of the selected image by using the Canny function from cv2

import cv2
from time import strftime
from matplotlib import pyplot as plt

timestr = strftime('%Y%m%d-%H%M%S')

img = cv2.imread('2.jpg', 0)
imgCanny = cv2.Canny(img, 100, 150)

dim = (1280, 720)

resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

filename = timestr+'.jpg'

cv2.imwrite(filename, imgCanny)
print(imgCanny)
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Picture'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(imgCanny,cmap = 'gray')
plt.title('Processed Picture'), plt.xticks([]), plt.yticks([])

plt.show()