import numpy as np
import cv2

img = cv2.imread('./demo_image_input.JPG')#step 1

ret, mask = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)#step 2

rows, cols, channels = mask.shape

row_start = row_end = 0
col = int(cols/2)

i = rows - 1
while i >= 0:
    res = np.greater_equal(mask[i, col], [150, 150, 150])
    if(np.array_equal(res, [True, True, True])):
        row_end = i
        break
    i -= 20
    
i = 0
while i < rows:
    res = np.greater_equal(mask[i, col], [150, 150, 150])
    if(np.array_equal(res, [True, True, True])):
        row_start = i
        break
    i+=20

cropped = img[row_start:row_end, 0:cols]#step 3

cv2.namedWindow('Cropped_Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Original_Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Masked_Image', cv2.WINDOW_NORMAL)
cv2.imshow('Original_Image', img)
cv2.imshow('Masked_Image', mask)
cv2.imshow('Cropped_Image', cropped)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('./demo_image_output.JPG', cropped)
