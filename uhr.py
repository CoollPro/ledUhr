import time
from rpi_ws281x import *
import argparse
import ledwrapper

# LED strip configuration:
LED_COUNT      = 256      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 10     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()
wrapper=ledwrapper.Wrapper(strip)
wrapper.setHelligkeit(0.0)
wrapper.setAllSaturation(1)
wrapper.setAllColour(0.84)
wrapper.zahl_speichern(5,0,0.5) #zahlen müssen im geraden Bereich sein
wrapper.zahl_speichern(6,6,0.5)
wrapper.zahl_speichern(7,12,0.5)
wrapper.zahl_speichern(8,18,0.5)
wrapper.zahl_speichern(9,24,0.5)


wrapper.ausgeben()
    