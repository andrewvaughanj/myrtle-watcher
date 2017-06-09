#!/usr/bin/env python

import os
import datetime
import shutil

MYRTLE_WATCHER_DIR = os.path.expandvars("${HOME}/myrtle-watcher")
CAPTURES_DIR = os.path.join(MYRTLE_WATCHER_DIR, "static/captures")
VIDEOS_DIR = os.path.join(MYRTLE_WATCHER_DIR, "static/videos")

if not os.path.exists(VIDEOS_DIR):
    os.makedirs(VIDEOS_DIR)

try:
    # Double of bunnies, because capturing at 30 seconds
    framerate = 20
    quality = 2

    """
    Kim's command
    """
    ffmpeg_command = "ffmpeg -y -i '{input:s}/frame_%04d.jpg' -framerate {framerate:d} -vcodec mpeg4 -q:v {quality:d} {output:s}/animated.mp4"
    """
    Andrew's commands
    """
    # ffmpeg_command = "ffmpeg -y -pattern_type glob -i '{input:s}/2*.jpg' -framerate {framerate:d} -vcodec libx264 -crf 25 -preset medium -pix_fmt yuv420p {output:s}/animated.mp4"
    # ffmpeg_command = "ffmpeg -y -pattern_type glob -i '{input:s}/2*.jpg' -framerate {framerate:d} -c:v libx264 -pix_fmt yuv420p -preset ultrafast -crf 28 {output:s}/animated.mp4"
    # ffmpeg_command = "ffmpeg -y -pattern_type glob -i '{input:s}/2*.jpg' -framerate {framerate:d} -c:v libx264 -flags:v '+cgop' -g 15 -bf 1 -coder ac -profile:v high -crf 21 -pix_fmt yuv420p -movflags faststart {output:s}/animated.mp4"
    TEMP_DIR = os.path.join(MYRTLE_WATCHER_DIR, "static/temp")
    ffmpeg_command = ffmpeg_command.format(
        input=TEMP_DIR, framerate=framerate, quality=quality, output=CAPTURES_DIR)
    os.system(ffmpeg_command)

    # Copy the mp4 to the back-up location
    curr_time = datetime.datetime.now().isoformat().replace(".", "_").replace(":", "_")
    curr_mp4_path = os.path.join(VIDEOS_DIR, curr_time + ".mp4")
    shutil.copyfile(os.path.join(CAPTURES_DIR, "animated.mp4"), curr_mp4_path)

    # YouTube details
    filename = "animated.mp4"
    desc = "Myrtle Watcher"
    category = "15"   # Pets & Animals YouTube category ID
    # Changing this to today's date as we're now uploading at 23:30!
    title = "Myrtle - {}".format(datetime.date.today().strftime('%A %-e %B %Y'))

    # Upload to YouTube
    os.system("python {}/upload_video.py --noauth_local_webserver --file='{}/{}' --title='{}' --description='{}' --category={}".format(
        MYRTLE_WATCHER_DIR, CAPTURES_DIR, filename, title, desc, category))

except KeyboardInterrupt:
    print "Quitting ..."

# EOF
