import serial,time,sys
ser = serial.Serial(port = "/dev/arduino",baudrate = 115200,timeout = 1) 

ser.write("hi")
time.sleep(10)
sys.exit()

