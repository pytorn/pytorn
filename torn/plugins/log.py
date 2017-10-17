#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .colors import BColors
from datetime import datetime

def warning(message):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print (now + ' [' + BColors.WARNING + 'WARNING' + BColors.ENDC + '] '+ message)

def info(message):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print (now + ' [' + BColors.OKBLUE + 'INFO' + BColors.ENDC + '] '+ message)

def error(message):
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print (now + ' [' + BColors.FAIL + 'ERROR' + BColors.ENDC + '] '+ message)

if __name__ == '__main__':
    error("You need to do something")