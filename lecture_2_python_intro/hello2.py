#!/usr/bin/env python


import sys

if len(sys.argv) >= 2:
    name = sys.argv[1]
else:
    name = "world"

print "hello %s" % name


