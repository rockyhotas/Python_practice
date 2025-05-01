#!/usr/bin/python3

# Copyright (C) 2025 Rocky Hotas
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# 
# As regards GPLv3: https://www.gnu.org/licenses/gpl-3.0.html

import time
import argparse
import subprocess
import os
import sys
import platform
from playsound import playsound


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Provide seconds and/or minutes to count down. Example: -m 3 -s 40")
    parser.add_argument("-s", "--seconds", nargs='?', type=int, const=0, default=0, help="Specify the number of seconds.")
    parser.add_argument("-m", "--minutes", nargs='?', type=int, const=0, default=0, help="Specify the number of minutes.")
    parser.add_argument("-r", "--print-start-date", help="Print the time and date when timer starts.", action="store_true")
    parser.add_argument("-p", "--print-end-date", help="Print the time and date when time is over.", action="store_true")
    parser.add_argument("-o", "--play-sound", help="Play a sound when time is over.", action="store_true")
    parser.add_argument("-a", "--display-notification", help="Show a system notification when time is over.", action="store_true")
    args = parser.parse_args()

    if args.print_start_date:
        now = time.strftime("%c")
        print("%s\tTimer starts." %now)

    start_time = time.time()
    target_time = start_time + (args.minutes)*60 + args.seconds

    while target_time > time.time():

        mins, secs = divmod(int(target_time - time.time()), 60)
        to_print = '{:02d}:{:02d}'.format(mins, secs)
        print(to_print, end="\r", flush=True)
        time.sleep(0.5)

    if args.print_end_date:
        now = time.strftime("%c")
        print ("%s\tTime has expired." %now)
    else:
        print("Time has expired.")

    host1 = 'hostname1'
    host3 = 'hostname2'
    if platform.node() == host1:
        path_prefix = '/home/' + 'user1' + '/'
        image_prefix = path_prefix + 'Pictures_path_1/'
    elif platform.node() == host3:
        path_prefix = '/home/' + 'user2' + '/'
        image_prefix = path_prefix + 'Pictures_path_2/'
    else:
        print("Could not determine system hostname.")
        sys.exit(2)
    
    cur_platform = 'linux'
    desktop_env = 'plasma'

    if args.play_sound:
        fpath = path_prefix + 'Downloads/ringtone_1.wav'
        if os.path.exists(fpath):
            file_size = os.path.getsize(fpath)
            if file_size != 0:
                try:
                    playsound(fpath)
                except:
                    print("Could not play sound.")
        else:
            print("Sound file not present or empty.")

    if args.display_notification:
        if sys.platform == cur_platform and os.environ.get('DESKTOP_SESSION') == desktop_env and os.environ.get('KDE_FULL_SESSION'):
            myicon = '--icon=' + image_prefix + 'Icons/icon_1.png'
            try:
                subprocess.Popen(["notify-send", "--expire-time=0", "--app-name=Timer", myicon, "Time has expired"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            except:
                print("Could not show notification.")
        else:
            print("This seems not to be a KDE Plasma session, so the notification can not be created.")

