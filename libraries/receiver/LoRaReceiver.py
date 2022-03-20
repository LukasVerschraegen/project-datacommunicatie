
from machine import Pin,I2C
import ssd1306

p16 = Pin(16, Pin.OUT)
p16.value(1) # resets screen

i2c = I2C(1,scl=Pin(15), sda=Pin(4), freq=400000)

oled = ssd1306.SSD1306_I2C(128, 64, i2c)

oled.fill(0)
oled.text('temp',0,0,1)
oled.text('temp',0,20,1)
oled.text('temp',0,40,1)
oled.show()

def receive(lora):
    print("LoRa Receiver")
    counter = 0
    oled.fill(0)
    payload = ['','','']
    #display = Display()

    while True:
        if lora.received_packet():
            if counter==3:
              counter=0
            lora.blink_led()
            print('something here')
            payload[counter] = lora.read_payload()
            print(payload[counter])
            oled.fill(0)
            oled.text(payload[0],0,0,1)
            oled.text(payload[1],0,20,1)
            oled.text(payload[2],0,40,1)
            oled.show()
            print(counter)
            counter += 1
           
            


