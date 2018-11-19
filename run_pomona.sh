#!/bin/bash

env PATH=${HOME}/pomona-watcher/pomona-watcherenv/bin
cd ${HOME}/pomona-watcher
exec uwsgi --ini pomona.ini
