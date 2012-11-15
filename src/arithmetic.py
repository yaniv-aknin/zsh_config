#!/usr/bin/env python

from __future__ import print_function

import os
import sys
from functools import partial

printerr = partial(print, file=sys.stderr)

commands = {}
def command(func):
    commands[func.__name__] = func

def yield_stdin_floats():
    for offset, line in enumerate(sys.stdin):
        try:
            yield offset, float(line.strip())
        except ValueError:
            printerr("bad input on line %d: %r can't be casted to float" % (offset, line,))
            sys.exit(1)

@command
def total():
    print(sum(number for offset, number in yield_stdin_floats()))

@command
def avg():
    total = 0
    for count, number in yield_stdin_floats():
        total += number
    try:
        print
        print(total / (count + 1))
    except NameError:
        printerr("no input")
        sys.exit(1)

def main(options):
    print(options)

if __name__ == '__main__':
    basename = os.path.basename(sys.argv[0])
    if basename not in commands:
        printerr('invoke me as one of "%s", not %r' % (", ".join(commands), basename))
        sys.exit(2)
    commands[basename]()
