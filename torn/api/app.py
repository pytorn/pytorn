#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
from .route import Routing
from ..plugins import app

class Application:
	# the application class, to initialize the server
	# The settings will be read from 
	def __init__(self):
		self.root_dir = os.getcwd()
		# gonna read settings from Config/config.json
		self = app.settings(self)

	def run(self):
		print (self.name + ' ' + str(self.port))