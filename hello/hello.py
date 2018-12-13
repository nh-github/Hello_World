#! /usr/bin/env python2
"""
Sample Hello World program with a main guard

This version demonstrates a function version of a hello world program using a
main guard (if '__main__' ...) to run the function only when the program is
itself run (and not when imported as a library/module.

Copyright (C) 2018 Noah Hafner
    This program is free software: you can redistribute it and/or
    modify it under the terms of the GNU General Public License as
    published by the Free Software Foundation, either version 3 of
    the License, or (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public
    License along with this program.  If not, see
    <https://www.gnu.org/licenses/>.
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
