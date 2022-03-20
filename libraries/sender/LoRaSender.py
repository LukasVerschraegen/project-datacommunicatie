

from time import sleep
#from uPySensors.ssd1306_i2c import Display
from machine import Pin, I2C
import BME280

# ESP32 - Pin assignment
i2c = I2C(scl=Pin(22), sda=Pin(21), freq=10000)
# ESP8266 - Pin assignment
#i2c = I2C(scl=Pin(5), sda=Pin(4), freq=10000)


def send(lora):
    counter = 0
    print("LoRa Sender")
    #display = Display()
    while True:
        bme = BME280.BME280(i2c=i2c)
        temp = bme.temperature
        hum = bme.humidity
        pres = bme.pressure
        payload = 'Temp: {0}'.format(temp)
        payload2 = 'Hum: {0}'.format(hum)
        payload3 = 'Pres: {0}'.format(pres)
        print("Sending packet: \n{}\n".format(payload))
        #display.show_text_wrap("{0} RSSI: {1}".format(payload, lora.packet_rssi()))
        lora.println(payload)
        sleep(5)
        lora.println(payload2)
        sleep(5)
        lora.println(payload3)
        counter += 1
        sleep(5)



