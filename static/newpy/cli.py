#!/usr/bin/env python

from __future__ import print_function

import sys
import argparse

def parse_arguments(argv):
    parser = argparse.ArgumentParser()
    options = parser.parse_args(argv[1:])
    return options

def main(options):
    print(options)

if __name__ == '__main__':
    main(parse_arguments(sys.argv))
