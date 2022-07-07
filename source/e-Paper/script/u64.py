#!/usr/bin/python
# -*- coding:utf-8 -*-

# https://www.waveshare.com/wiki/2.13inch_e-Paper_HAT_(B)

import sys
import os
picdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'pic')
libdir = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'lib')
if os.path.exists(libdir):
    sys.path.append(libdir)

import logging
from waveshare_epd import epd2in13bc
import time
from PIL import Image,ImageDraw,ImageFont
import traceback

logging.basicConfig(level=logging.DEBUG)

try:
    logging.info("Starting e-Paper")

    epd = epd2in13bc.EPD()
    logging.info("init and Clear")
    epd.init()
    epd.Clear()

    # Drawing on the image
    logging.info("Loading fonts")
    font64 = ImageFont.truetype(os.path.join(picdir, 'c64.ttf'), 8)
    
    logging.info("loading bmp files")
    HBlackimage = Image.open(os.path.join(picdir, 'c_black.bmp'))
    HRYimage = Image.open(os.path.join(picdir, 'c_red.bmp'))
    # epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))

    # Drawing on the Horizontal image
    
    logging.info("Drawing text on image")
    #HBlackimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126
    #HRYimage = Image.new('1', (epd.height, epd.width), 255)  # 298*126  ryimage: red or yellow image
    drawblack = ImageDraw.Draw(HBlackimage)
    drawry = ImageDraw.Draw(HRYimage)
    drawblack.text((10, 0), 'https://opensource64.com/', font = font64, fill = 0)
    drawblack.text((10, 16), 'DevOps64 demo', font = font64, fill = 0)
    drawry.text((40, 96), '(O) Berry de Jager', font = font64, fill = 0)
    logging.info("Outputting images to display")
    epd.display(epd.getbuffer(HBlackimage), epd.getbuffer(HRYimage))
    logging.info("done")

except IOError as e:
    logging.info(e)

except KeyboardInterrupt:
    logging.info("ctrl + c:")
    epd2in13bc.epdconfig.module_exit()
    exit()
