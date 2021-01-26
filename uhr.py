import time
from rpi_ws281x import *
import argparse
import ledwrapper
from datetime import datetime
import mqttinit
import pytz

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

wrapper.setpixel(((9*8)),0.64,1,0.2)
wrapper.setpixel((21*8),0.64,1,0.2)

mqtt=mqttinit.MQTT_Handler(wrapper.lichtEinstellen,wrapper.setFlag)

tz = pytz.timezone('Europe/Berlin')


while True:
    
    currentTime=datetime.now(tz)

    if currentTime.second==0 and currentTime.hour>19 and currentTime.minute==0 and currentTime.hour<23:
        wrapper.automaticBrightness(False)
        wrapper.doubledot(9*8)
    elif currentTime.second==0 and currentTime.hour>6 and currentTime.minute==0 and currentTime.hour<10:
        wrapper.automaticBrightness(True)
        wrapper.doubledot(21*8)

    wrapper.doppelte_zahl_speichern(currentTime.hour,0,wrapper.farbeStunde_Miute)
    wrapper.doppelte_zahl_speichern(currentTime.minute,12,wrapper.farbeStunde_Miute)
    wrapper.doppelte_zahl_speichern(currentTime.second,23,wrapper.farbeSekunde)
    wrapper.ausgeben()
    time.sleep(60/1000)