#!/usr/bin/env python

import os
import time
import requests

CAPTURES_DIR = "static/captures/"
CURRENT_CAPTURE = CAPTURES_DIR + "current.jpg"
INTERVAL = 5


def get_image():
    ROOM = 5  # TODO, THIS NEEDS CHANGING!
    HOST = ""
    PORT = "2{ROOM:02d}1".format(ROOM=ROOM)
    PATH = "Streaming/channels/1/picture?snapShotImageType=JPEG"
    USER = "cat"
    PASS = "cam"
    url = "http://{USER}:{PASS}@{HOST}:{PORT}/{PATH}".format(
        USER=USER, PASS=PASS, HOST=HOST, PORT=PORT, PATH=PATH)
    response = requests.get(url)
    if response.status_code == 200:
        return True, response.content

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

                # Use the current time as the filename
                curr_time = datetime.datetime.now().isoformat().replace(".", "_").replace(":", "_")
                curr_img_path = os.path.join(CAPTURES_DIR, curr_time, ".jpg")

                with open(curr_img_path) as curr_img:
                    curr_img.write(camera_capture)

                shutil.copyfile(curr_img_path, CURRENT_CAPTURE)

            else:
                print "Failure!"

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

            time.sleep(INTERVAL)

    except KeyboardInterrupt:
        print "\nQuitting ..."

# EOF
