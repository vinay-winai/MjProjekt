# import the opencv library
import cv2
import serial
import time
serialport = serial.Serial('COM4',baudrate=115200,timeout=2)
for i in range(0,11):
    arduinodata = serialport.readline()
    print(arduinodata)

# define a video capture object
if(arduinodata == b'1\r\n'):
    capture_duration = 60
    start_time = time.time() # records current time
    vid = cv2.VideoCapture(0)
    while(int(time.time() - start_time) < capture_duration ):
    # Capture the video frame by frame
        ret, frame = vid.read()
    # Display the resulting frame
        cv2.imshow('frame', frame)
	# After the loop release the cap object
    vid.release()
# Destroy all the windows
    cv2.destroyAllWindows()
