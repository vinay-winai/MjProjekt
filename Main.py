# import the opencv library
#5172556132:AAFOLQF8BpBrckxNnKLsfyeljlLmWHdZpQw    API token
#1122917287   group chat id

import serial
import RecordVideo
import RecordTwo
import Compress
import MakeVideo
import pcacompress
serialport = serial.Serial('COM4',baudrate=115200,timeout=2)
def readData():
    arduinodata = serialport.readline()
    print(arduinodata)
    if(arduinodata == b'1\r\n'):
        serialport.close()
        RecordVideo.record()
        Compress.compression1()
        Compress.deleteFrames()
        MakeVideo.makeVideo()
        RecordTwo.record()
        pcacompress.compression1()
        MakeVideo.makeVideo()
        Compress.deleteFrames()
        serialport.open()
    else:
        pass

while(True):
    readData()  
