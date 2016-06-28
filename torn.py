#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2016 Shubhodeep Mukherjee
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import sys
from argparse import ArgumentParser, RawDescriptionHelpFormatter

__version__ = '0.0.1'
description = ('Torn is tool for managing tornado web client.')
epilog = ('The commands are:\n'
		  '\tnew\t\tCreate a Tornado Application\n'
		  '\trun\t\trun the app and start a Web server for development\n'
		  '\tapi\t\tcreate an API tornado application')

def torn():
	print description+'\n'
	arguments = ArgumentParser(prog="torn",formatter_class=RawDescriptionHelpFormatter,epilog=epilog,usage='%(prog)s command [arguments]')
	arguments.add_argument("command", type=str,nargs='+', help="Specify what command to proceed")
	args = arguments.parse_args()
	if args.command:
		print args.command


def main():
	try:
		torn()
	except KeyboardInterrupt:
		print '\nTerminating process'

if __name__ == '__main__':
	main()