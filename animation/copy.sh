#!/bin/bash

set -e
set -u

mkdir empty_dir
rsync -a --delete empty_dir thermcam
rsync -a --delete empty_dir webcam
rm -rf thermcam webcam empty_dir
mkdir thermcam webcam

base="*.jpg"

rsync --info=progress2 -aHXxv --numeric-ids --delete --progress -e "ssh -T -c arcfour -o Compression=no -x" ~/pomona-watcher/static/captures/${base} montage

# EOF

