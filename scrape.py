#!/usr/bin/env python

import os
import time
import requests
import datetime
import shutil
import yaml
import traceback

CAPTURES_DIR = "static/captures"
CURRENT_CAPTURE = os.path.join(CAPTURES_DIR, "current.jpg")
INTERVAL = 30
document = open("config.yml").read()
config = (yaml.load(document))
ROOM = config["ROOM"]
HOST = config["HOST"]
PATH = config["PATH"]
USER = config["USER"]
PASS = config["PASS"]

#
# The port number previously ended with a 1 -- the latest cat-cam details have
# this ending with a 4
#
PORT = "2{ROOM:02d}4".format(ROOM=ROOM)

URL = "http://{USER}:{PASS}@{HOST}:{PORT}/{PATH}".format(
    USER=USER, PASS=PASS, HOST=HOST, PORT=PORT, PATH=PATH)


def get_image():
    try:
        response = requests.get(URL)
        if response.status_code == 200:
            return True, response.content
    except:
        print "HTTP Failure ..."
        traceback.print_exc()
        return False, None

    return False, None

if __name__ == "__main__":

    print("Capturing images ...")

    if not os.path.exists(CAPTURES_DIR):
        os.makedirs(CAPTURES_DIR)

    try:
        while 1:
            # Grab the image
            result, camera_capture = get_image()

            if result:

                try:
                    # Use the current time as the filename
                    curr_time = datetime.datetime.now().isoformat().replace(".", "_").replace(":", "_")
                    curr_img_path = os.path.join(
                        CAPTURES_DIR, curr_time + ".jpg")

                    with open(curr_img_path, "w") as curr_img:
                        curr_img.write(camera_capture)

                    shutil.copyfile(curr_img_path, CURRENT_CAPTURE)
                except:
                    print "File failure ..."
                    traceback.print_exc()

            else:
                curr_time = datetime.datetime.now().isoformat().replace(".", "_").replace(":", "_")
                print "Failed: " + curr_time

            # Delete if any images older than a day
            for fn in sorted(os.listdir(CAPTURES_DIR)):
                fp = os.path.join(CAPTURES_DIR, fn)
                if os.stat(fp).st_mtime < time.time() - 86400:
                    if os.path.isfile(fp):
                        os.remove(fp)

                # The files are ordered by filename (by age) so stop if a young
                # file is found
                else:
                    break

            try:
                time.sleep(INTERVAL)
            except:
                print "Sleep failure ..."
                traceback.print_exc()

    except KeyboardInterrupt:
        print "\nQuitting ..."

# EOF
