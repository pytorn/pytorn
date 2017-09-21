#!/usr/bin/env python
# -*- coding: utf-8 -*-
from argparse import ArgumentParser, RawDescriptionHelpFormatter

def cli():
	epilog = ('The actions are:\n'
		'\tnew\t\tCreate a Tornado Application\n'
		'\trun\t\trun the app and start a Web server for development\n'
		'\tapi\t\tcreate an API tornado application\n'
		'\tversion\t\treturns the current version of torn\n')
	parser = ArgumentParser(prog = 'torn',
    						description='A full fledged Tornado MVC framework [In-progress]',
    						formatter_class=RawDescriptionHelpFormatter,
    						epilog = epilog,
    						usage='%(prog)s [action [arguments]]')
	parser.add_argument('action', nargs='*', default = ['new', 'api', 'run'] ,help='Action to be performed with the application')
	parser.parse_args()


