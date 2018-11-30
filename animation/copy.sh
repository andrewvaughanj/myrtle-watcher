#!/bin/bash

set -e
set -u

mkdir empty_dir
rsync -a --delete empty_dir montage
rm -rf empty_dir montage
mkdir montage

base="*.jpg"

rsync --info=progress2 -aHXxv --numeric-ids --delete --progress -e "ssh -T -c arcfour -o Compression=no -x" ~/pomona-watcher/static/captures/${base} montage

# EOF

