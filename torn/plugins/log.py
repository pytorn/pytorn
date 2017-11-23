#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Log consists of functions required to display a log on the terminal."""

from __future__ import print_function
from datetime import datetime
import torn.plugins.colors

def warning(message):
    """Display Warning.

    Method prints the warning message, message being given
    as an input.

    Arguments:
        message {string} -- The message to be displayed.
    """

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print((now + ' [' + torn.plugins.colors.WARNING)
          ('WARNING' + torn.plugins.colors.ENDC + '] ')
          (message))

def info(message):
    """Display Information.

    Method prints the information message, message being given
    as an input.

    Arguments:
        message {string} -- The message to be displayed.
    """

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print((now + ' [' + torn.plugins.colors.OKBLUE)
          ('INFO' + torn.plugins.colors.ENDC + '] ')
          (message))

def error(message):
    """Display Error.

    Method prints the error message, message being given
    as an input.

    Arguments:
        message {string} -- The message to be displayed.
    """
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print((now + ' [' + torn.plugins.colors.FAIL)
          ('ERROR' + torn.plugins.colors.ENDC + '] ')
          (message))
    