#%%
import cv2
# read target image from project and resize for better visibility
img = cv2.imread('target.jpg')

# show image
cv2.imshow('target', img)
cv2.waitKey(0)


#%%
"""
correct function depends on the target
+ Chessboard/Checkerboard --> cv2.findChessboardCorners
+ Circles (Symmetric and Asymmetric) --> cv2.findCirclesGird
"""
# Define the amount of corners/feature as tuple (must not be quadratic)
gridSize = (12, 8)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, corners = cv2.findCirclesGrid(gray, gridSize, cv2.CALIB_CB_ASYMMETRIC_GRID)
print(ret)
if ret == True: # target found
    # define stopping criteria for refining the grid
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
    corners2 = cv2.cornerSubPix(gray, corners, gridSize, (-1, -1), criteria)

    featured_img = cv2.drawChessboardCorners(img, gridSize, corners, ret)
    cv2.imshow('img', img)
    cv2.waitKey(0)

    cv2.imwrite('featured_target.jpg', featured_img)