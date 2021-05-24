from machine import Pin #importing Pin class from Machine module
import time#importing time module
Touch_pad = machine.Pin(17,Pin.IN,Pin.PULL_UP)#creating an object(Touch_pad) and assigning the Pin 17 to as an INPUT.
led = Pin(15,Pin.OUT)#creating an object(led) and assigning the Pin 15 to as an OUTPUT.
Relay=Pin(28,Pin.OUT)#creating an object(Relay) and assigning the Pin 28 to as an OUTPUT.
while True:
    if Touch_pad.value()==1:#condition checking/if thouchpad value is equal to 1
        print("Touched")# printing the string on shell area
        Relay.toggle()#changing the relay states(ON to OFF or OFF to ON)
        led.toggle()#changing the led states(ON to OFF or OFF to ON)
        time.sleep(0.5)# providing a delay time 0.5 second.
