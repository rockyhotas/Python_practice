Python script to run a timer, which prints the remaining time in the CLI and which can optionally create a pop-up notification in KDE Plasma and play a sound, when the timer expires. It can also print the time and date when the timer starts and/or when it ends.

If options `-a` and/or `-o` are used, the script **must be adapted**: it can not immediately run as it is here. In fact, the existence of two different machines where the script can be run is contemplated, each one with its own path for images and ringtones. If this is not required, simply be sure to define `path_prefix` and `image_prefix` before the block `if args.play_sound:`. Also, the image to be used in the notification and the ringtone must be specified.

If no GUI is available, the whole code after `print("Time has expired.")` can be discarded, as well as options `-a` and `-o`.

As regards

    parser.add_argument("-s", "--seconds", nargs='?', type=int, const=0, default=0, help="Specify the number of seconds.")

* `type=int` performs a check on the input and generates an error if a non-integer value (for example, `1.2`) is provided.
* `nargs='?'` implies that one argument will be consumed from the command line if possible. If no command-line argument is present, the value specified as `default=` will be produced. If the option string `-s` is present but not followed by an argument, the value specified as `const=` will be produced.
* Moreover, with this configuration, the presence of the option `-s` is not mandatory.
* This way, if the script is run with no options at all, it will be assumed the default value `1` for args.seconds. See [https://docs.python.org/3/library/argparse.html#nargs](https://docs.python.org/3/library/argparse.html#nargs) and also [https://docs.python.org/3/library/argparse.html#dest](https://docs.python.org/3/library/argparse.html#dest) for the conventions used to create the name of the `variable` in `args.variable` corresponding to a specific argument.

This script doesn't use `sleep()` to determine the countdown duration, because it is is not precise: its actual duration depends on the CPU occupation and other possibly random factors. `sleep()` is only used inside the `while` loop to save some CPU resources. The countdown is performed as suggested [here](https://stackoverflow.com/a/36591332), but with `target_time > time.time()` (it was probably a typo). Its precision is considered enough for a human user, but it can be improved for other applications.

Some other references:

* [To get the hostname](https://www.scaler.com/topics/python-get-hostname/)
* [To determine the current OS](https://stackoverflow.com/a/58071295)
* [Behaviour of the parser arguments](https://stackoverflow.com/a/31243133)
* [Print time and date](https://www.cyberciti.biz/faq/howto-get-current-date-time-in-python/)
* [Print a tab character](https://medium.com/python-basics-beyond/how-to-print-a-tab-in-python-a6c7df39c2ca)
