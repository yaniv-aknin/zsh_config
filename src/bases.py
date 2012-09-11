#!/usr/bin/env python

import sys

if 'hex' in sys.argv[0]:
    base = 10
    fmt = '%x'
elif 'dec' in sys.argv[0]:
    base = 16
    fmt = '%d'
else:
    print("invoke me as 'hex' or 'dec', not %r" % (sys.argv[0],))
    sys.exit(2)

if len(sys.argv) == 1:
    src = sys.stdin
else:
    src = sys.argv[1:]
for string in src:
    print(fmt % (int(string.strip(), base),))
