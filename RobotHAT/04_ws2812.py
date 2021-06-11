import time
from rpi_ws281x import *
import argparse
import RPi.GPIO as GPIO

# LED strip configuration:
LED_COUNT      = 3      # Number of LED pixels.
LED_PIN        = 12      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


parser = argparse.ArgumentParser()
parser.add_argument('-c', '--clear', action='store_true', help='clear the display on exit')
args = parser.parse_args()

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

# Define functions which animate LEDs in various ways.
def colorWipe( R, G, B):
    """Wipe color across display a pixel at a time."""
    color = Color(R,G,B)
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()

def run():
    strip.setPixelColor(0, Color(0, 0, 255))  # No. 1 light is blue.
    strip.setPixelColor(1, Color(0, 255, 0))  # No. 2 light is green.
    strip.setPixelColor(2, Color(255, 0, 0))  # No. 3 light is red.
    strip.show()
    time.sleep(2)
    colorWipe(0, 0, 0)  # All lights off.
    time.sleep(1)

if __name__ == '__main__':
    try:
      while True:
        run()
    except KeyboardInterrupt:
      colorWipe(0, 0, 0)


