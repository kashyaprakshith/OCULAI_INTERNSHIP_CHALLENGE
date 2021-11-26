import numpy as np
import cv2


# input
Video_in = "data/high.mp4"

# output
Video_out = "output/XY.mp4"

# Video Settings
winName = 'output'
cv2.namedWindow(winName)
cv2.resizeWindow(winName, 500, 500)
cap = cv2.VideoCapture(Video_in)

fps = int(cap.get(cv2.CAP_PROP_FPS))
length_video = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(cap.get(3))
height = int(cap.get(4))

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(Video_out, fourcc, fps, (width, height))

n_frame = 0
frames = []
_, first_frame = cap.read()
first_gray = cv2.cvtColor(first_frame, cv2.COLOR_BGR2GRAY)
first_gray = cv2.GaussianBlur(first_gray, (5, 5), 0)


while cap.isOpened():
    # get frame from video
    _, frame = cap.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)

    print('video_progress: ', round(n_frame*100/length_video, 1), '%')



    # Do something
    difference = cv2.absdiff(first_frame, frame)
    _, difference = cv2.threshold(difference, 25, 255, cv2.THRESH_BINARY)
    cv2.imshow("First FRAME", first_frame)
    cv2.imshow("Frame", frame)
    cv2.imshow("difference", difference)
    key = cv2.waitKey(30)
    if key == 27:
        break




    #if ret:
     #   out.write(frame)
      #  cv2.namedWindow(winName, cv2.WINDOW_NORMAL)
       # cv2.imshow('output', frame)
        #if cv2.waitKey(1) == ord('q'):
         #   break
    #else:
     #   break
    #n_frame += 1

cap.release()
cv2.destroyAllWindows()