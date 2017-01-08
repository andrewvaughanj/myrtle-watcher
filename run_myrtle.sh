#!/bin/bash

env PATH=${HOME}/myrtle-watcher/myrtle-watcherenv/bin
cd ${HOME}/myrtle-watcher
exec uwsgi --ini myrtle.ini
