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
from colors import bcolors
from newapp import NewController
from apiapp import APIController
import os

#Check whether Tornado is installed or not
try:
	import tornado
except ImportError:
	raise SystemExit('Tornado not installed, pip install tornado')

__version__ = '0.0.3'
description = ('Torn is tool for managing tornado web client.\n'
			   '---------------------------------------------')
epilog = ('The commands are:\n'
		  '\tnew\t\tCreate a Tornado Application\n'
		  '\trun\t\trun the app and start a Web server for development\n'
		  '\tapi\t\tcreate an API tornado application\n'
		  '\tversion\t\treturns the current version of torn')

def Port():
	f = open('conf/app.conf','r').read()
	return int(f.split('\n')[1].split('=')[1].strip())

def Debug():
	f = open('conf/app.conf','r').read()
	print(bcolors.OKBLUE+'INFO:'+bcolors.ENDC+' reading configuration file for DEBUG and PORT values')
	return f.split('\n')[2].split('=')[1].strip() == 'True'

#to check if directory is application or not
def AppExist():
	try:
		f = open('conf/app.conf','r').read()
		return f.split('\n')[0].split('=')[0].strip() == 'name'
	except:
		return False

def torn():
	print(description)
	if len(sys.argv) == 1:
		sys.argv.append('-h')
	arguments = ArgumentParser(prog="torn",formatter_class=RawDescriptionHelpFormatter,
							   epilog=epilog,usage='%(prog)s command [arguments]')
	arguments.add_argument("command", type=str,nargs='+',
						  	help="Specify what command to proceed.")
	options = arguments.parse_args()
	if isinstance(options, tuple):
		args = options[0]
	else:
		args = options
	del options
	CommandController(args.command)
	
def CommandController(command):
	error = bcolors.FAIL+'Error:'+bcolors.ENDC
	if command[0] == 'version':
		raise SystemExit('Current version: '+__version__)
	elif command[0] == 'new':
		if len(command) == 1:
			raise SystemExit(error+' Kindly specify name of the app.')
		elif len(command) > 2:
			raise SystemExit(error+' App names with spaces not allowed.')
		NewController(command[1])
	elif command[0] == 'run':
		if not AppExist():
			raise SystemExit(error+' not an app directory, try $ cd <app-dest>')
		print(bcolors.OKBLUE+'INFO:'+bcolors.ENDC+' web server running at '+str(Port()))
		print(bcolors.OKBLUE+'INFO:'+bcolors.ENDC+' Use Ctrl-C to exit')
		from subprocess import call
		call(["python", "server.py"])
	elif command[0] == 'api':
		if len(command) == 1:
			raise SystemExit(error+' Kindly specify name of the api.')
		elif len(command) > 2:
			raise SystemExit(error+' API names with spaces not allowed.')
		APIController(command[1])
	else:
		raise SystemExit(error+' Enter valid command')

def main():
	try:
		torn()
	except KeyboardInterrupt:
		print('\nTerminating process')

if __name__ == '__main__':
	main()