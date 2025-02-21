#!/usr/bin/python3
# File name   : LED.py
# Description : WS_2812
# Website     : based on the code from https://github.com/rpi-ws281x/rpi-ws281x-python/blob/master/examples/strandtest.py
# E-mail      : support@adeept.com
# Author      : original code by Tony DiCola (tony@tonydicola.com)
# Date        : 2018/10/12
import time
from rpi_ws281x import *
import argparse

# LED strip configuration:
LED_COUNT      = 16      # Number of LED pixels.
LED_PIN        = 12      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 10     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

BREATH = 1
color = 'yellow'
FRE_TIME = 50
DELY = 0.1

class LED:
    def __init__(self):
        self.LED_COUNT      = 16      # Number of LED pixels.
        self.LED_PIN        = 12      # GPIO pin connected to the pixels (18 uses PWM!).
        self.LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
        self.LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
        self.LED_BRIGHTNESS = 10      # Set to 0 for darkest and 255 for brightest
        self.LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
        self.LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53
        parser = argparse.ArgumentParser()
        parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
        args = parser.parse_args()

        # Create NeoPixel object with appropriate configuration.
        self.strip = Adafruit_NeoPixel(self.LED_COUNT, self.LED_PIN, self.LED_FREQ_HZ, self.LED_DMA, self.LED_INVERT, self.LED_BRIGHTNESS, self.LED_CHANNEL)
        # Intialize the library (must be called once before other functions).
        self.strip.begin()

    # Define functions which animate LEDs in various ways.
    def colorWipe(self, color, wait_ms=0):
        """Wipe color across display a pixel at a time."""
        for i in range(self.strip.numPixels()):
            self.strip.setPixelColor(i, color)
            self.strip.show()
            #time.sleep(wait_ms/1000.0)


    def breath_status_set(self, status):
        global BREATH
        BREATH = status


    def breath_color_set(self, invar):
        global color
        color = invar


    def breath_frequency_set(self, frequency_input):
        global FRE_TIME
        FRE_TIME = frequency_input


    def breath(self, brightness):
        while 1:
            if BREATH:
                if color == 'red':
                    for a in range(0, brightness, FRE_TIME):
                        if not BREATH:
                            break
                        else:
                            self.colorWipe(Color(a,0,0))
                            time.sleep(DELY)
                    for b in range(0, brightness, FRE_TIME):
                        if not BREATH:
                            break
                        else:
                            self.colorWipe(Color(((brightness-1)-b),0,0))
                            time.sleep(DELY)
                elif color == 'green':
                    for a in range(0, brightness, FRE_TIME):
                        if not BREATH:
                            break
                        else:
                            self.colorWipe(Color(0,a,0))
                            time.sleep(DELY)
                    for b in range(0, brightness, FRE_TIME):
                        if not BREATH:
                            break
                        else:
                            self.colorWipe(Color(0,((brightness-1)-b),0))
                            time.sleep(DELY)
                elif color == 'yellow':
                    for a in range(0, brightness, FRE_TIME):
                        if not BREATH:
                            break
                        else:
                            self.colorWipe(Color(a,a,0))
                            time.sleep(DELY)
                    for b in range(0, brightness, FRE_TIME):
                        if not BREATH:
                            break
                        else:
                            self.colorWipe(Color(((brightness-1)-b),((brightness-1)-b),0))
                            time.sleep(DELY)
                elif color == 'blue':
                    for a in range(0, brightness, FRE_TIME):
                        if not BREATH:
                            break
                        else:
                            self.colorWipe(Color(0,a,a))
                            time.sleep(DELY)
                    for b in range(0, brightness, FRE_TIME):
                        if not BREATH:
                            break
                        else:
                            self.colorWipe(Color(0,((brightness-1)-b),((brightness-1)-b)))
                            time.sleep(DELY)
            else:
                time.sleep(0.2)

#led=LED()
#led.breath(255)
#led.colorWipe(Color(0,0,0))

if __name__ == '__main__':
    led = LED()
    try:
        while True:
            print("Red")
            led.colorWipe(Color(255, 0, 0))  # red
            time.sleep(1)
            print("Green")
            led.colorWipe(Color(0, 255, 0))  # green
            time.sleep(1)
            print("Blue")
            led.colorWipe(Color(0, 0, 255))  # blue
            time.sleep(1) 
    except:  
        led.colorWipe(Color(0,0,0))  # Lights out