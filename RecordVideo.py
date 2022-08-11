from cv2 import cv2
import time

def record():
    capture_duration = 10
    start_time = time.time()    # records current time
    vid = cv2.VideoCapture(0, cv2.CAP_DSHOW)    # define a video capture object
    if(vid.isOpened() == False):
        print("Unable to read camera feed")
    #default resolutions of the frame are obtained. System dependent
    c = 1
    while(int(time.time() - start_time) < capture_duration ):
        rval,frame = vid.read() # Capture the video frame by frame
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imwrite(f"D:\\python_idleprog\\practice\\frames\\{c}.jpg",gray)
        c = c + 1
        cv2.waitKey(1)
        
    vid.release()   # After the loop release the cap object
    cv2.destroyAllWindows() # Destroy all the windows
    

