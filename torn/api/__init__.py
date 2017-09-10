#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web

class GetResource(tornado.web.RequestHandler):
	def initialize(self, controller):
		self.controller = controller

	def get(self, path):
		body = self.controller.index()
		self.finish(body)

class PostResource(tornado.web.RequestHandler):
	def post(self, path, routes):
		body = routes[path]['controller']()
		self.finish(body)

class PutResource(tornado.web.RequestHandler):
	def put(self, path, routes):
		body = routes[path]['controller']()
		self.finish(body)

class PatchResource(tornado.web.RequestHandler):
	def patch(self, path, routes):
		body = routes[path]['controller']()
		self.finish(body)

class DeleteResource(tornado.web.RequestHandler):
	def delete(self, path, routes):
		body = routes[path]['controller']()
		self.finish(body)

