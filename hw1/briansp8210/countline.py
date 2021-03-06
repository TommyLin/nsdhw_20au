#!/usr/bin/env bash

"""true"
if which $PYTHON_BIN > /dev/null; then
  exec $PYTHON_BIN $0 $@
else
  echo "exec: $PYTHON_BIN: not found"
  exit 127
fi
"""

import sys
import os.path


if len(sys.argv) < 2:
    sys.stdout.write('missing file name\n')
elif len(sys.argv) > 2:
    sys.stdout.write('only one argument is allowed\n')
else:
    fname = sys.argv[1]
    if os.path.exists(fname):
        with open(fname) as fobj:
            lines = fobj.readlines()
        sys.stdout.write('{} lines in {}\n'.format(len(lines), fname))
    else:
        sys.stdout.write('{} not found\n'.format(fname))
