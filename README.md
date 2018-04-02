# automatic-extracting-of-a-strip-with-blood-stain
It is an **image processing** project that extracts a white strip with blood stain from its background image.

## _Assignment Documentation:_

### There are 2 python files:
1.	**demo_code.py:**  for explaining the algorithm**
2.	**cropper_Swati_Kanchan.py:** the actual algorithm that crops the image files stored in “data” folder.**

### The algorithm flow goes in this way:
### demo_code:
```python
import numpy as np
import cv2
```

**Importing numpy and openCV modules**

```python
img = cv2.imread('./demo_image_input.JPG')
```

**Reading the demo image demo_image_input.JPG**

![alt tag](https://github.com/Swati707/automatic-extracting-of-a-strip-with-blood-stain/blob/master/Original%20Image.JPG)
```python
ret, mask = cv2.threshold(img, 120, 255, cv2.THRESH_TOZERO)
```

**Converting the image to a masked image using threshold of 120 and creating a black background.**

![alt tag](https://github.com/Swati707/automatic-extracting-of-a-strip-with-blood-stain/blob/master/Masked%20Image.JPG)

```python
rows, cols, channels = mask.shape
```

**Getting the total number of row and column pixels and number of channels.**

```python
row_start = row_end = 0
col_mid = int(cols/2)
```

**row_start and row_end stores the starting row pixel and ending row pixel of the white strip in the masked image.**
 ```python
i = rows - 1
while i >= 0:
    res = np.greater_equal(mask[i, col_mid], [150, 150, 150])
    if(np.array_equal(res, [True, True, True])):
        row_end = i
        break
    i -= 20
```
**Calculates the end row pixel of the white strip in the image.**
```python
i = 0
while i < rows:
    res = np.greater_equal(mask[i, col_mid], [150, 150, 150])
    if(np.array_equal(res, [True, True, True])):
        row_start = i
        break
    i+=20
```
**Calculates the start row pixel of the white strip in the image.**
```python
cropped = img[row_start:row_end, 0:cols]
```
**Region of image from row_start to row_end(vertically) and 0 to cols(horizontally) is stored in cropped.**
![alt tag](https://github.com/Swati707/automatic-extracting-of-a-strip-with-blood-stain/blob/master/Cropped%20Image.JPG)

```python
cv2.namedWindow('Cropped_Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Original_Image', cv2.WINDOW_NORMAL)
cv2.namedWindow('Masked_Image', cv2.WINDOW_NORMAL)
cv2.imshow('Original_Image', img)
cv2.imshow('Masked_Image', mask)
cv2.imshow('Cropped_Image', cropped)
```
**Creates 3 different resizeable windows each showing all the 3 stages of the image.**
```python
cv2.waitKey(0)
cv2.destroyAllWindows()
```
**All the windows wait for any key to be clicked and closes all the windows automatically.**

```python
cv2.imwrite('./demo_output_image.JPG', cropped)
```
**Finally writes the cropped image into a new file named “demo_output_image.jpg”.**

_**Resources:**_
1. [Upto 7th tutorial on OpenCV by sentdex](https://www.youtube.com/watch?v=Z78zbnLlPUA&list=PLQVvvaa0QuDdttJXlLtAJxJetJcqmqlQq)
2. [Download link for OpenCV](https://www.lfd.uci.edu/~gohlke/pythonlibs/#opencv)
3. [Image thresholding CV2 function](https://docs.opencv.org/3.4.0/d7/d4d/tutorial_py_thresholding.html)
4. [Python - Install Anaconda, Jupyter Notebook, Spyder on Windows](https://www.youtube.com/watch?v=Q0jGAZAdZqM&t=269s)
5. [Quick introduction to Jupyter Notebook](https://www.youtube.com/watch?v=jZ952vChhuI&t=40s)
6. [Download Anaconda3-5.0.1-Windows-x86_64](https://anaconda.org/conda-forge/zip)
