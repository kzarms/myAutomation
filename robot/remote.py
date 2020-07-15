import serial
import time


#Open port COM4
s = serial.Serial('COM4')
start = '$1#'
stop = '$6#'

#Run the car
s.write(start.encode('ascii'))
time.sleep(5.5)
#Stop the car
s.write(stop.encode('ascii'))


s.close()

print(s.read())

