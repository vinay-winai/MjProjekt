from cv2 import cv2
import numpy as np
import os
import glob

def compression1():
    z = 1
    k = 1
    n = 2
    dir_path = r'D:\python_idleprog\Practice\frames'
    nf = len([entry for entry in os.listdir(dir_path) if os.path.isfile(os.path.join(dir_path, entry))])
    print(nf)
    for _ in range(0, nf-1):
        fpath  = "D:\\python_idleprog\\Practice\\frames\\"
        fpath2 = "D:\\python_idleprog\\Practice\\final_op\\"
        a=cv2.imread(fpath + str(k) +".jpg",0)
        b=cv2.imread(fpath + str(n) +".jpg",0)
        m = mse(a,b)
        if m >=  600:
            cv2.imwrite(fpath2 + str(z) +".jpg" , a)
            z = z+1
            k = n
            n = k+1
        else :
            n = n+1

def mse(imageA, imageB):
    err=np.sum((imageA.astype("float") - imageB.astype("float"))**2)
    err /= float(imageA.shape[0]*imageA.shape[1])
    return err


def deleteFrames():
    files = glob.glob('D:\\python_idleprog\\Practice\\frames\\*.jpg')
    for f in files:
        os.remove(f)

