# import the opencv library
from cv2 import cv2
print(cv2.__version__)
import serial
import time
serialport = serial.Serial('COM4',baudrate=115200,timeout=2)
while(True):
    arduinodata = serialport.readline()
    print(arduinodata)

# define a video capture object
    if(arduinodata == b'1\r\n'):
        serialport.close()
        capture_duration = 15
        start_time = time.time() # records current time
        vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        while(int(time.time() - start_time) < capture_duration ):
    # Capture the video frame by frame
            ret, frame = vid.read()
        # Display the resulting frame
            cv2.imshow('frame', frame)
        # After the loop release the cap object
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        vid.release()
    # Destroy all the windows
        cv2.destroyAllWindows()
        serialport.open()
