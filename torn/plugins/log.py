#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Log consists of functions required to display a log on the terminal."""

from __future__ import print_function
from datetime import datetime
import torn.plugins.colors

def warning(message, code='WARNING'):
    """Display Warning.

    Method prints the warning message, message being given
    as an input.

    Arguments:
        message {string} -- The message to be displayed.
    """

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    output = now + ' [' + torn.plugins.colors.WARNING + \
            code + torn.plugins.colors.ENDC + '] \t' + \
            message
    print(output)

def info(message, code='INFO'):
    """Display Information.

    Method prints the information message, message being given
    as an input.

    Arguments:
        message {string} -- The message to be displayed.
    """

    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    output = now + ' [' + torn.plugins.colors.OKBLUE + \
            code + torn.plugins.colors.ENDC + '] \t' + \
            message
    print(output)

def error(message, code='ERROR'):
    """Display Error.

    Method prints the error message, message being given
    as an input.

    Arguments:
        message {string} -- The message to be displayed.
    """
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    output = now + ' [' + torn.plugins.colors.FAIL + \
            code + torn.plugins.colors.ENDC + '] \t' + \
            message
    print(output)
    