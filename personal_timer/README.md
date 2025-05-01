Python script to run a timer, which prints the remaining time in the CLI and which can optionally create a pop-up notification in KDE Plasma and play a sound, when the timer expires. It can also print the time and date when the timer starts and/or when it ends.

If options `-a` and/or `-o` are used, the script **must be adapted**: it can not immediately run as it is here. In fact, the existence of two different machines where the script can be run is contemplated, each one with its own path for images and ringtones. If this is not required, simply be sure to define `path_prefix` and `image_prefix` before the block `if args.play_sound:`. Also, the image to be used in the notification and the ringtone must be specified.

If no GUI is available, the whole code after `print("Time has expired.")` can be discarded, as well as options `-a` and `-o`.
