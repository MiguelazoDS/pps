import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('1.jpg',0)
edges = cv2.Canny(img,100,200)
cv2.imwrite('modif.jpg',edges)
