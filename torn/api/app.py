#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import tornado.web
import tornado.ioloop
import tornado.httpserver
from .route import Routing, Router
from ..plugins import app

class Application:
	# the application class, to initialize the server
	# The settings will be read from 
	def __init__(self, route = Routing()):
		self.root_dir = os.getcwd()
		# gonna read settings from Config/config.json
		self = app.settings(self)
		self.routes = route.routes


	def run(self):
		application = tornado.web.Application()
		router = Router(application, self.routes)
		http_server = tornado.httpserver.HTTPServer(router)
		http_server.listen(self.port)
		tornado.ioloop.IOLoop.current().start()
