from datetime import datetime
from cv2 import cv2
import glob
import os
import SendVideo
def makeVideo():
    img_array = []
    dir_path = r'D:\python_idleprog\Practice\final_op'
    n = len([entry for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))])
    print(n)
    for i in range(1,n+1):
        filename = 'D:\\python_idleprog\\Practice\\final_op\\'+str(i)+'.jpg'
        img = cv2.imread(filename)
        img = cv2.resize(img,(640,480))
        img_array.append(img)
    now = datetime.now()
    sstring = "output-"+now.strftime("%H_%M_%S")
    out = cv2.VideoWriter(f"D:\\python_idleprog\\Practice\\{sstring}.avi",cv2.VideoWriter_fourcc(*'DIVX'), 24, (640,480))

    for i in range(len(img_array)):
        out.write(img_array[i])
    out.release()       

    files = glob.glob('D:\\python_idleprog\\Practice\\final_op\\*.jpg')
    for f in files:
        os.remove(f)      
    SendVideo.sendVideo(sstring+".avi")
