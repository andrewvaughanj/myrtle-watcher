#!/bin/bash

cd ${HOME}/myrtle-watcher

rm -rf "static/temp"
mkdir "static/temp"
cd "static/temp"
for f in `ls -rt ../captures/2*.jpg`
do
    # get the index in 0000 format
    printf -v counts "%04d" $count

    # check if the file exists
    if [ -s "$f" ]
    then
        # if it does, copy it and link it
        cp $f "frame_$counts.jpg"
        # increment counter
        count=`expr $count + 1`
    fi
    done
cd ../..

/home/pi/myrtle-watcher/animate.py

rm -rf "static/temp"