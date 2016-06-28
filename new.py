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

import os

"""
The Controller to create a new app
"""
class NewController():
	global CURRENT_DIR,NAME
	def __init__(self,name):
		NAME = name
		CURRENT_DIR = os.getcwd()
		if os.path.isdir(CURRENT_DIR+'/'+NAME):
			raise SystemExit("Directory named '"+NAME+"' already exists")

		#Creating the project directory
		os.makedirs(CURRENT_DIR+'/'+NAME)
