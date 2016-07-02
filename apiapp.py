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

"""
Directory structure
<app-name>
 |-/conf
 |------|-app.conf
 |-/controllers
 |------|-__init__.py
 |------|-home.py
 |------|-modules.py
 |-/routes
 |------|-__init__.py
 |------|-routes.py
 |-/views
 |------|-home.html
 |-/static
 |------/css
 |------/js
 |------/fonts
 |-/models
 |------|-__init__.py
 |-server.go
"""

import os
from colors import bcolors

"""
The Controller to create a new app
"""
class APIController():
	NAME = ''
	CURRENT_DIR = os.getcwd()
	INFO = bcolors.OKBLUE+'INFO:'+bcolors.ENDC
	SUCCESS = bcolors.OKGREEN+'SUCCESS:'+bcolors.ENDC
	def __init__(self,name):
		self.NAME = name
		if os.path.isdir(self.CURRENT_DIR+'/'+self.NAME):
			raise SystemExit(bcolors.FAIL+"Error:"+bcolors.ENDC+" Directory named '"+self.NAME+"' already exists")

		#Creating the project directory
		os.makedirs(self.CURRENT_DIR+'/'+self.NAME)
		self.create()

	def create(self):
		path = self.CURRENT_DIR+'/'+self.NAME
		os.chdir(path)
		print(self.INFO+' directory changed to '+bcolors.OKBLUE+self.NAME)
		dirlist = ["conf","controllers","routes","models"]
		for dirs in dirlist:
			os.makedirs(path+'/'+dirs)
			print(self.INFO+' "'+dirs+'" directory created')
		print(self.SUCCESS+' Directories created')
		self.write()

	def write(self):
		writings = {
				"conf/app.conf":"name = "+self.NAME+"\nport = 8000\ndebug = True",
				"controllers/__init__.py":("""'''
The controller initialization script
Imports all the files in the folder directly
To import modules, kindly include them in modules.py in the current folder
'''

from os.path import dirname,basename, isfile
import glob
modules = glob.glob(dirname(__file__)+"/*.py")
__all__ = [basename(f)[:-3] for f in modules if isfile(f) and basename(f)!="__init__.py" and basename(f)!="modules.py"]

from . import *"""),
				"controllers/home.py":("""
'''
Preset controller by torn for / route
'''
from modules import *
class homeHandler(tornado.web.RequestHandler):
	def get(self):
		ob = {
			'status':'OK',
			'reponse':'Application running'
		}
		self.write(tornado.escape.json_encode(ob))
					"""),
				"controllers/modules.py":("""
'''
Middleware for controller to contain all the modules
'''
import tornado.web
import tornado.escape
					"""),
				"routes/__init__.py":"from routes import *",
				"routes/routes.py":("""
from controllers import *
route = [
		(
			r"/",
			home.homeHandler
		)
]
					"""),
				"server.py":("""
'''
The main server file
'''
from tornado.web import RequestHandler, Application
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
import os
import torn

from routes import *
settings = dict(
		debug=torn.Debug(),
	)

application = Application(route, **settings)

if __name__ == "__main__":
	server = HTTPServer(application)
	server.listen(torn.Port())
	IOLoop.current().start()

					""")
		}
		path = self.CURRENT_DIR+'/'+self.NAME
		os.chdir(path)
		for i in writings:
			conf = open(i,'w')
			conf.write(writings[i])
			print(self.INFO+' "'+i+'" file created and done.')
		print(self.SUCCESS+' API created')
		print("""
Directory structure
%s
 |-/conf
 |------|-app.conf
 |-/controllers
 |------|-__init__.py
 |------|-home.py
 |------|-modules.py
 |-/routes
 |------|-__init__.py
 |------|-routes.py
 |-/models
 |------|-__init__.py
 |-server.go
""" % (self.NAME))
		print(self.INFO+' USAGE: torn run (inside the app directory)')





