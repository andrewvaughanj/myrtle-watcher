#!/usr/bin/env python

import os
import datetime
import shutil

MYRTLE_WATCHER_DIR = os.path.expandvars("${HOME}/myrtle-watcher")
CAPTURES_DIR = MYRTLE_WATCHER_DIR + "/static/captures"
VIDEOS_DIR = MYRTLE_WATCHER_DIR + "/static/videos"

if not os.path.exists(VIDEOS_DIR):
    os.makedirs(VIDEOS_DIR)

try:

    # Create .gif for Myrtle Watcher
    # os.system("ffmpeg -y -framerate 10 -pattern_type glob -i '{}/2*.jpg' -pix_fmt rgb8 -ignore_loop 0 -s 576x384 {}/animated.gif".format(CAPTURES_DIR, CAPTURES_DIR))

    # Create .mp4 for YouTube
    os.system("ffmpeg -y -framerate 10 -pattern_type glob -i '{}/2*.jpg' -vcodec mpeg4 -q:v 10 {}/animated.mp4".format(CAPTURES_DIR, CAPTURES_DIR))

    # Copy the mp4 to the back-up location
    curr_time = datetime.datetime.now().isoformat().replace(".", "_").replace(":", "_")
    curr_mp4_path = os.path.join(VIDEOS_DIR, curr_time, ".mp4")
    shutil.copyfile(curr_mp4_path, CURRENT_CAPTURE)

    # YouTube details
    filename = "animated.mp4"
    desc = "Myrtle Watcher"
    category = "15"   # Pets & Animals YouTube category ID
    title = "Myrtle - {}".format((datetime.date.today() - datetime.timedelta(1)
                                  ).strftime('%A %-e %B %Y'))  # Yesterday's date

    # Upload to YouTube
    os.system("python {}/upload_video.py --noauth_local_webserver --file='{}/{}' --title='{}' --description='{}' --category={}".format(
        MYRTLE_WATCHER_DIR, CAPTURES_DIR, filename, title, desc, category))

except KeyboardInterrupt:
    print "Quitting ..."

# EOF
