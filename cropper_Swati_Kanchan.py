import numpy as np
import cv2
import os

def cropper(img):
    ret, mask = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)#step 2
    rows, cols, channels = mask.shape

    i1 = i2 = 0
    col = int(cols/2)

    i = rows - 1
    while i >= 0:
        res = np.greater_equal(mask[i, col], [150, 150, 150])
        if(np.array_equal(res, [True, True, True])):
            i2 = i
            break
        i -= 20  
    i = 0
    while i < rows:
        res = np.greater_equal(mask[i, col], [150, 150, 150])
        if(np.array_equal(res, [True, True, True])):
            i1 = i
            break
        i+=20
    
    roi = img[i1:i2, 0:cols]#step 3
    return roi

def ensure_dir(file_path):
    directory = os.path.dirname(file_path)
    if not os.path.exists(directory):
        os.makedirs(directory)

folders = ['10^-1', '10^-4', '10^-10', '10_Original_Sample']
for folder in folders:
    directory = './data/'+folder
    for file in os.listdir(directory):
        img = cv2.imread(os.path.join(directory, file))#step 1
        if img is not None:
            cropped_image = cropper(img)
            new_file_path = directory+'_Cropped/'+file
            ensure_dir(new_file_path)
            cv2.imwrite(new_file_path, cropped_image)
print("Task completed...Yayyy")

