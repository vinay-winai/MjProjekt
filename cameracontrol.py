# import the opencv library
import cv2
import serial

serialport = serial.Serial('COM4',baudrate=115200,timeout=2)

for i in range(1,13):
    arduinodata = serialport.readline().decode('ascii')
    print(arduinodata)

# define a video capture object
if(arduinodata):
    vid = cv2.VideoCapture(0)
  
    while(True):
      
    # Capture the video frame
    # by frame
        ret, frame = vid.read()
  
    # Display the resulting frame
        cv2.imshow('frame', frame)
      
    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
	# After the loop release the cap object
    vid.release()
# Destroy all the windows
    cv2.destroyAllWindows()
