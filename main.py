import numpy as np

from imageio import imread,imwrite
import cv2

img = imread('day.png')

arr = img*np.array([0.1,0.2,0.5])

arr2 = (255*arr/arr.max()).asttype(np.uint8)

imwrite('night.png',arr2)

img2 = cv2.imread('night.png')

gamma = 2

gamma_img = np.array(255*(img/255)**gamma,dtype = 'unit8')

cv2.imwrite('night_final.png',gamma_img)

print("conversion done")