import serial

serialport = serial.Serial('COM4',baudrate=115200,timeout=2)

for i in range(1,13):
    arduinodata = serialport.readline()
    print(arduinodata)

