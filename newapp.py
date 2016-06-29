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
 |-lastupdate.tmp
 |-server.go
"""

import os
from colors import bcolors

"""
The Controller to create a new app
"""
class NewController():
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
		print self.INFO+' directory changed to '+bcolors.OKBLUE+self.NAME
		dirlist = ["conf","controllers","routes","views","static","models"]
		for dirs in dirlist:
			os.makedirs(path+'/'+dirs)
			print self.INFO+' '+dirs+' directory created'
		subdirs = ["css","js","fonts"]
		for dirs in subdirs:
			os.makedirs(path+'/static/'+dirs)
			print self.INFO+' static/'+dirs+' directory created'
		print self.SUCCESS+' Directories created'


