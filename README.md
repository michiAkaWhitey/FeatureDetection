# FeatureDetection
Python code which illustrates how to detect features for typical calibration tasks.

### Starting Image
A calibration target from the internet with cirlces and a grid shape of
* with = 12
* height = 10

<div style="width:300px">

![target](target.jpg)
</div>

### Detection of feature
1. Convert image to grayscale
2. Detect corners by the right function 
   1. Checkerboard
      ```python
      cv2.findChessboardCorners(image,patternSize[,corners[,flags]]) -> retval, corners
   2. Circles
      ```python
      cv2.findCirclesGrid(image,patternSize[,centers[,flags[,blobDetector]]]) -> retval, centers
3. Refine corners by calling 
   ```Python
    cv2.cornerSubPix(image,corners,winSize,zeroZone,criteria) -> corners
4. Plot find features by
    ```Python
   	cv2.drawChessboardCorners(image,patternSize,corners,patternWasFound) ->	image
   

### Finished result

<div style="width:300px">

![features](featured_target.jpg)
</div>

