from machine import Pin
import time
Touch_pad = machine.Pin(17,Pin.IN,Pin.PULL_UP)
led = Pin(15,Pin.OUT)
Relay = Pin(28,Pin.OUT)
while True:
    if Touch_pad.value()==1:
        print("Touched")
        Relay.toggle()
        led.toggle()
        time.sleep(0.5)