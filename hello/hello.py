#! /usr/bin/env python3
"""
Sample Hello World program

This version includes some testing, accessible with unittest.
unittest command line:
    python3 -m unittest hello/hello.py

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
import unittest
from unittest.mock import patch, call


class Testing(unittest.TestCase):
    @patch('builtins.print')
    def test_printing(self, mocked_print):
        print_greeting()

        assert mocked_print.mock_calls == [call('Hello World')]
        return

    def test_test(self):
        assert 1
        return


def print_greeting():
    print("Hello World")


def main():
    print_greeting()
    #test_thing = Testing()
    #test_thing.test_printing()


if '__main__' == __name__:
    try:
        sys.exit(main())
    except KeyboardInterrupt as e:
        print("break, %s".format(str(e)))
