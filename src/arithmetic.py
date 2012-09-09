#!/usr/bin/env python

from __future__ import print_function

import sys

total = 0
count = 0
for line in sys.stdin:
    count += 1
    try:
        number = float(line.strip())
    except ValueError:
        print("bad input on line %d: %r can't be casted to float" % (count, line,), file=sys.stderr)
        sys.exit(1)
    total += number

if not count:
    print(0) # special case no input
elif 'total' in sys.argv[0]:
    print(total)
elif 'avg' in sys.argv[0]:
    print(total / count)
else:
    print("invoke me as 'total' or 'avg', not %r" % (sys.argv[0],))
    sys.exit(2)
