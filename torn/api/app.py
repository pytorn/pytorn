#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
from .route import Routing

class Application:
	# the application class, to initialize the server
	# The settings will be read from 
	def __init__(self):
		self.root_dir = os.getcwd()
		# print (os.getcwd())