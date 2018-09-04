import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('1.jpg',0)

plt.plot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.show()
