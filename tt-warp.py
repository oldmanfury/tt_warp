# Copyright (c) 2017 Adafruit Industries
# Author: Tony DiCola & James DeVito
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
import time
import sys
import Adafruit_GPIO.SPI as SPI
import Adafruit_SSD1306

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont

import subprocess

# Raspberry Pi pin configuration:
RST = None     # on the PiOLED this pin isnt used
# Note the following are only used with SPI:
DC = 23
SPI_PORT = 0
SPI_DEVICE = 0
knob1 = 0
knob2 = 0
knob3 = 0
knob4 = 0
knob5 = 0
fx1 = 0
fx2 = 0
fx3 = 0
fx4 = 0
#then = time.time()
#print then
line1 = str()
line2 = str()
line3 = str()
line4 = str()
data = str()
#data = "0: 16 15 15 16 16 15 16 15 16 16 15 16"
#data = data[3: ]
plotdata = list()
#plotdata = [int(x) for x in data.split(" ")]
#print data
#print plotdata

# 128x32 display with hardware I2C:
disp = Adafruit_SSD1306.SSD1306_128_32(rst=RST)

# Initialize library.
disp.begin()

# Clear display.
disp.clear()
disp.display()

# Create blank image for drawing.
# Make sure to create image with mode '1' for 1-bit color.
width = disp.width
height = disp.height
image = Image.new('1', (width, height))

# Get drawing object to draw on image.
draw = ImageDraw.Draw(image)

# Draw a black filled box to clear the image.
draw.rectangle((0,0,width,height), outline=0, fill=0)

# Draw some shapes.
# First define some constants to allow easy resizing of shapes.
padding = -2
top = padding
bottom = height-padding
# Move left to right keeping track of the current x position for drawing shapes.
x = 0


# Load default font.
font = ImageFont.load_default()

# Alternatively load a TTF font.  Make sure the .ttf font file is in the same directory as the python script!
# Some other nice fonts to try: http://www.dafont.com/bitmap.php
# font = ImageFont.truetype('Minecraftia.ttf', 8)
font2 = ImageFont.truetype("/usr/share/fonts/truetype/roboto/Roboto-Bold.ttf",14)
font3 = ImageFont.truetype("/usr/share/fonts/truetype/roboto/Roboto-Bold.ttf",28)

draw.rectangle((0,0,width,height), outline=0, fill=255)
draw.text((x, top+1),"  tt-warp",  font=font3, fill=0)
disp.image(image)
disp.display()

time.sleep(2)

sys.stdin.flush()
TT = sys.stdin.readline()
TT.strip()

while True:
    then = time.time()

#    Draw a black filled box to clear the image.
    draw.rectangle((0,0,width,height), outline=0, fill=0)
#    now = time.time()
#    print now
#    while ((now-then) < 0.01):        
    sys.stdin.flush()
    TT = sys.stdin.readline()
    TT.strip()
#    print TT
    if (TT[0:8] == "print: 1"):
        line1 = TT[8: ]
        draw.rectangle((0,0,width,height), outline=0, fill=255)
        draw.text((x, top+8),    str(line1),  font=font2, fill=0)
	disp.image(image)
        disp.display()
    elif (TT[0:8] == "print: 2"):
        line2 = TT[8: ]
        draw.rectangle((0,0,width,height), outline=0, fill=255)
        draw.text((x, top+1),    str(line2),  font=font3, fill=0)
#        time.sleep(2)
	disp.image(image)
        disp.display()
    elif (TT[0:8] == 'print: 3'):
        line3 = TT[8: ]
    elif (TT[0:8] == 'print: 4'):
        line4 = TT[8: ]
    elif ((TT[0:8] == 'print: Z') or (TT[0:8] == 'print: X')):
        data = TT[10: ]
        data = data.split(' ')
        plotdata = [int(k) for k in data]
#        for k in data.split(" "):
#            try:
#                k = int(k)
#                plotdata.append(k)
#	    except ValueError:
#                print "found a string"
# Steven's fix for occasional string
        i = 0
        while (i < 100):
#		if (i < 99):
#		if (TT[0:8] == 'print: Z'):
#	                draw.line((i-1,plotdata[i-1],i,plotdata[i]), fill=255)
		if (TT[0:8] == 'print: X'):
	                draw.line((i-1,plotdata[i-1],i,plotdata[i]), fill=255)
		i += 1
	while (i <=127):
                draw.point((i,plotdata[i]), fill=255)
		i += 1
#            elif (i == 100):
#                knob1=31-plotdata[i]
#            elif (i == 101):
#                knob2=31-plotdata[i]
#            elif (i == 102):
#                knob3=31-plotdata[i]
#            elif (i == 103):
#                knob4=31-plotdata[i]
#            elif (i == 104):
#                knob5=31-plotdata[i]
#            elif (i == 105):
#                fx1=plotdata[i]
#            elif (i == 106):
#                fx2=plotdata[i]
#            elif (i == 107):
#                fx3=plotdata[i]
#            elif (i == 108):
#                fx4=plotdata[i]
#        draw.rectangle((101,31,102,knob1), outline=1, fill=255)
#        draw.rectangle((106,31,107,knob2), outline=1, fill=255)
#        draw.rectangle((111,31,112,knob3), outline=1, fill=255)
#        draw.rectangle((116,31,117,knob4), outline=1, fill=255)
#        draw.rectangle((121,31,122,knob5), outline=1, fill=255)
#        if (fx1):
#            draw.rectangle((126,30,127,25), outline=1, fill=255)
#        if (fx2):
#            draw.rectangle((126,22,127,17), outline=1, fill=255)
#        if (fx3):
#            draw.rectangle((126,15,127,10), outline=1, fill=255)
#        if (fx4):
#            draw.rectangle((126,7,127,2), outline=1, fill=255)
	disp.image(image)
        disp.display()
#        then = time.clock()
    time.sleep(.01)
#        print now, then, (now-then)
#    else:
#    sys.stdin.flush()
#    sys.stdout.flush()

    
