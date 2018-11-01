#doesnt include full code. Just parts to insert.

import random
from random import shuffle
GPIO.setup(18,GPIO.OUT)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

def green_light():
    GPIO.output(12, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(11,GPIO.LOW)
    time.sleep(0.5)

def blue_light():
    GPIO.output(11, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(11,GPIO.LOW)
    time.sleep(0.5)

def yellow_light():
    GPIO.output(10, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(10,GPIO.LOW)
    time.sleep(0.5)

def red_light():
    GPIO.output(15, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(15,GPIO.LOW)
    time.sleep(0.5)

def light_display():
	light_list = [green_light, blue_light, yellow_light, red_light]
	random.shuffle(light_list)
	for light_function in light_list:
		light_function()

light_display()

