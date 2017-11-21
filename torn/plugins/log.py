"""Log consists of functions required to display a log on the terminal."""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from datetime import datetime
import torn.plugins.colors

def warning(message):
    """Definition for displaying a warning."""
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print((now + ' [' + torn.plugins.colors.WARNING)
          ('WARNING' + torn.plugins.colors.ENDC + '] ')
          (message))

def info(message):
    """Definition for displaying an information."""
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print((now + ' [' + torn.plugins.colors.OKBLUE)
          ('INFO' + torn.plugins.colors.ENDC + '] ')
          (message))

def error(message):
    """Definition for displaying an error."""
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print((now + ' [' + torn.plugins.colors.FAIL)
          ('ERROR' + torn.plugins.colors.ENDC + '] ')
          (message))

if __name__ == '__main__':
    error("You need to do something")
    