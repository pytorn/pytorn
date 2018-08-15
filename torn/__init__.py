"""This module initiates the command line for torn"""

#!/usr/bin/env python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser, RawDescriptionHelpFormatter
import sys
from torn.plugins import console

def cli():
    """Function for cli"""
    epilog = ('The actions are:\n'
            '\tnew\t\tCreate a new torn app\n'
            '\trun\t\tRun the app and start a Web server for development\n'
            '\tcontroller\tCreate a new controller\n'
            '\tversion\t\treturns the current version of torn\n')
    parser = ArgumentParser(prog='torn',
                            description='A full fledged MVC framework based on Tornado and Jinja2 templating',
                            formatter_class=RawDescriptionHelpFormatter,
                            epilog=epilog,
                            usage='%(prog)s [action [arguments]]')

    parser.add_argument('action',
                        nargs='+',
                        choices=['new', 'run', 'controller','version'],
                        help='Action to be performed with the application')
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()
    console.handler(args)
