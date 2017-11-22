# tt_warp
a simple puredata vinylizer and OLED visualizer for the terminal tedium

You don’t need an OLED for this to work. OLED options may be omitted

Copy tt-warp.pd and tt-warp.py to your terminal tedium patch folder.

in pdpd (the batch file that runs puredata - change the puredata execute command line to

sudo /home/pi/pd-0.46-7/bin/pd -nogui -rt /home/pi/pdpatch/tt-warp.pd |& python /home/pi/pdpatch/tt-warp.py

The six knobs are:

1: pops

2: craclkes

3: hiss

4: amplitude of pitch warble.  Warble is set to 33 1/3 rpm.  I like LP's.

5: bandpass center

6: bandpass Q


The bandpass is the stock puredata one - it can lead to distortion, ringing, etc.  I use it to thin the sound.

Help? Email me at logo64@gmail.com

OLED references:

Configuring i2c https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c

Adafruit installation instructions: https://learn.adafruit.com/adafruit-pioled-128x32-mini-oled-for-raspberry-pi/usage Note section on “Speeding up the display”

Search ebay for OLED 128 32 I2C, and find the 4-pins on the left side version.  These get cheaper every day.

eBay source for 128x32 OLED (USA seller) http://www.ebay.com/itm/0-91-128x32-I2C-IIC-OLED-LCD-White-Display-DIY-Module-3-3V-5V-For-PIC-Arduino/172683183086
