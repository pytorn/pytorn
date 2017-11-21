"""Log consists of functions required to display a log on the terminal."""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from datetime import datetime
from .colors import BColors

def warning(message):
    """Definition for displaying a warning."""
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(now + ' [' + BColors.WARNING + 'WARNING' + BColors.ENDC + '] '+ message)

def info(message):
    """Definition for displaying an information."""
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(now + ' [' + BColors.OKBLUE + 'INFO' + BColors.ENDC + '] '+ message)

def error(message):
    """Definition for displaying an error."""
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(now + ' [' + BColors.FAIL + 'ERROR' + BColors.ENDC + '] '+ message)

if __name__ == '__main__':
    error("You need to do something")
    