#! /usr/bin/env python2
"""
Sample Hello World program with a main guard

This version demonstrates a function version of a hello
world program using a main guard (if '__main__' ...) to
run the function only when the program is itself run (and
not when imported as a library/module.
"""

__version__ = 0.1

import sys


def main():
    print("hello world")


if '__main__' == __name__:
    try:
        sys.exit(main())
    except KeyboardInterrupt, e:
        print "break, %s" % str(e)
