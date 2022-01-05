# import the opencv library
#5020621550:AAHn14UaYU7DffWprSDVswQgxyH9H1PK0ak    API token
#-790881518   group chat id

from cv2 import cv2
import telegram
import serial
import time

serialport = serial.Serial('COM4',baudrate=115200,timeout=2)
i = 0

def sendVideo():
    # initializing a telegram bot 
    bot = telegram.Bot('5020621550:AAHn14UaYU7DffWprSDVswQgxyH9H1PK0ak')
    # to send video
    if bot.get_updates():
        chat_id =  '-790881518' 
        video=open('D:\\python_idleprog\\Practice', 'rb')
        bot.send_video(chat_id,video, supports_streaming=True)
    else:
        pass

def cameraFunction():
    capture_duration = 10
    start_time = time.time()    # records current time
    vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)    # define a video capture object
    if(vid.isOpened() == False):
        print("Unable to read camera feed")
    #default resolutions of the frame are obtained. System dependent
    frame_width = int(vid.get(3))   
    frame_height = int(vid.get(4))
    out = cv2.VideoWriter(f"output{i}.avi",cv2.VideoWriter_fourcc('M','J','P','G'), 10, (frame_width,frame_height))
    while(int(time.time() - start_time) < capture_duration ):
        ret, frame = vid.read() # Capture the video frame by frame
        if ret == True:
            out.write(frame)    # writing file into output.avi
            cv2.imshow('frame', frame)  # Display the resulting frame
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break  
    vid.release()   # After the loop release the cap object
    out.release()
    cv2.destroyAllWindows() # Destroy all the windows
    sendVideo(f"output{i}.avi")
    
def readData():
    arduinodata = serialport.readline()
    print(arduinodata)
    if(arduinodata == b'1\r\n'):
        serialport.close()
        cameraFunction()
        serialport.open()
    else:
        pass
i += 1


while(True):
    readData()
