#!/bin/bash

sudo uvcdynctrl -s 'LED1 Mode' 0

cd /home/pi/mytrle-watcher
python ./scrape.py
