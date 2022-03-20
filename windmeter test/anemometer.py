import time
from machine import UART,Pin

RTS_pin=Pin(4,Pin.OUT)

ComPort = UART(2,9600)                         # init with given baudrate (tx2 en rx2)
ComPort.init(9600, bits=8, parity=None, stop=1, timeout=1000)

data = bytes([0x01, 0x03, 0x00, 0x16, 0x00, 0x01, 0x65, 0xCE]) #inquiry frame

RTS_pin.value(1)
time.sleep(0.2)
print(ComPort.write(data))  #send data
time.sleep(0.2)
print(data)
RTS_pin.value(0)
time.sleep(0.2)                 # print the data
while not ComPort.any():        #wait for received data
    time.sleep(0.2)
dataIn =  ComPort.read(8)        # Wait and read 8 data values
print(dataIn)                   # print the received data
time.sleep(0.2)
