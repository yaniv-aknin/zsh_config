#!/usr/bin/env python

from __future__ import print_function

from argparse import ArgumentParser as _ArgumentParser
import os
import sys
from functools import wraps

class ArgumentParser(_ArgumentParser):
  def add_argument(self, *args, **kwargs):
    _ArgumentParser.add_argument(self, *args, **kwargs)
    return self

multiple_files = (ArgumentParser()
  .add_argument('file1')
  .add_argument('file2')
  .add_argument('files', nargs='*')
  .add_argument('-s', '--strip', action='store_true', default=False)
)
two_files = (ArgumentParser()
  .add_argument('file1')
  .add_argument('file2')
  .add_argument('-s', '--strip', action='store_true', default=False)
)

def stripper(iterable):
  for datum in iterable:
    yield datum.strip() + '\n'

commands = {}
def command(parser):
  def decor(func):
    @wraps(func)
    def inner(argv):
      options = parser.parse_args(argv)
      filenames = [options.file1, options.file2]
      filenames.extend(getattr(options, 'files', []))
      try:
        options.iterables = [open(filename) for filename in filenames]
      except IOError, error:
        raise SystemExit('%s: %s' % (error.filename, error.strerror))
      if options.strip:
        options.iterables = [stripper(iterable) for iterable
                             in options.iterables]
      return func(options)
    commands[inner.__name__] = inner
    return inner
  return decor

def yield_from_iterables(iterables):
  offset = 0
  while iterables:
    iterable = iterables[offset % len(iterables)]
    try:
      yield iterable, iterable.next()
    except StopIteration:
      iterables.remove(iterable)
    offset += 1

@command(multiple_files)
def union(options):
  seen = set()
  for iterable, datum in yield_from_iterables(options.iterables):
    if datum not in seen:
      sys.stdout.write(datum)
    seen.add(datum)

@command(multiple_files)
def intersect(options):
  original_length = len(options.iterables)
  seen = {}
  for iterable, datum in yield_from_iterables(options.iterables):
    seen.setdefault(datum, set()).add(iterable)
    if len(seen[datum]) == original_length:
      sys.stdout.write(datum)
      seen[datum].add(None)

@command(two_files)
def difference(options):
  iterable1, iterable2 = options.iterables
  sys.stdout.write("".join(set(iterable1).difference(set(iterable2))))

if __name__ == '__main__':
    basename = os.path.basename(sys.argv[0])
    if basename not in commands:
      raise SystemExit('invoke me as one of "%s", not %r' %
                       (", ".join(commands), basename))
    commands[basename](sys.argv[1:])
