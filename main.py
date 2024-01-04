import cv2
# //ammoutn of cameras and or video files
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
writer = cv2.VideoWriter('output.mp4', fourcc, 30, (1280, 720))
recording = False

while True:
    ret, frame = cap.read()
    if ret:
        cv2.imshow('video', frame)
        if recording == True:
            writer.write(frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    elif key == ord('r'):
        recording = not recording
        print('recording:', recording)
    
cap.release()
writer.release()
cv2.destroyAllWindows()