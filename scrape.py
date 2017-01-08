#!/usr/bin/env python

import os
import time

CAPTURES_DIR = "static/captures/"
CURRENT_CAPTURE = CAPTURES_DIR + "current.jpg"
INTERVAL = 5


def get_image():

    return False, None

# Get and print an OpenCV property


def get_property(property, property_id):
    print "{}: {}".format(property, camera.get(property_id))

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

                # Store the image in the history and copy over the 'current'
                # view
                # FILE IS:
                #    CAPTURES_DIR + curr_time + ".jpg", camera_capture
                # shutil.copyfile(CAPTURES_DIR + curr_time +
                #                ".jpg", CURRENT_CAPTURE)

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
