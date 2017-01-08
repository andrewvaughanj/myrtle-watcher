#!/bin/bash

env PATH=/home/pi/mytrle-watcher/mytrle-watcherenv/bin
cd /home/pi/mytrle-watcher
exec uwsgi --ini mytrle.ini
