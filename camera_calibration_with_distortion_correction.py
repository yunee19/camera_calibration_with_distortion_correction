import numpy as np
import cv2 as cv

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

# Open the video file
video = cv.VideoCapture('chessboard.mp4')

# Define the codec and create VideoWriter object
fourcc = cv.VideoWriter_fourcc(*'MP4V') # or 'H264'
out = cv.VideoWriter('Camera_Calibration_Results.mp4', fourcc, 20.0, (640, 480))

while True:
    ret, frame = video.read()
    if not ret:
        break
    
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (7,6), None)
    
    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray, corners, (11,11), (-1,-1), criteria)
        imgpoints.append(corners2)
        
        # Draw and display the corners
        cv.drawChessboardCorners(frame, (7,6), corners2, ret)
        
        # Perform camera calibration
        ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
        
        # Undistort the frame
        undistorted_frame = cv.undistort(frame, mtx, dist)
        
        # Write undistorted frame to the output video
        out.write(undistorted_frame)
        
        # Show undistorted frame
        cv.imshow('Camera Calibration with distortion correction', undistorted_frame)
        cv.waitKey(500)

# Release everything if job is finished
video.release()
out.release()
cv.destroyAllWindows()
