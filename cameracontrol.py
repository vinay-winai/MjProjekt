# import the opencv library
import cv2
import serial
import time
def camfun():
    capture_duration = 10
    start_time = time.time()
    vid = cv2.VideoCapture(0)
    while( int(time.time() - start_time) < capture_duration ):
        ret, frame = vid.read()
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    vid.release()
    cv2.destroyAllWindows()

serialport = serial.Serial('COM4',baudrate=115200,timeout=2)
while(True):
	arduino_data = serialport.readline().decode('ascii')
	if arduino_data == 1:
		camfun()
	else:
		pass
