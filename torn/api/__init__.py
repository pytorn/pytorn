#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import inspect

class GetResource(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller

    def get(self, path):
        if(inspect.isclass(self.controller)):
            controller = self.controller()
            body = controller.get()
        elif(inspect.isfunction(self.controller)):
            body = controller()
        else:
            raise TypeError

        self.finish(body)

class PostResource(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller

    def post(self, path):
        if(inspect.isclass(self.controller)):
            controller = self.controller()
            body = controller.post()
        elif(inspect.isfunction(self.controller)):
            body = controller()
        else:
            raise TypeError

        self.finish(body)

class PutResource(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller
        
    def put(self, path):
        if(inspect.isclass(self.controller)):
            controller = self.controller()
            body = controller.put()
        elif(inspect.isfunction(self.controller)):
            body = controller()
        else:
            raise TypeError

        self.finish(body)

class PatchResource(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller
        
    def patch(self, path):
        if(inspect.isclass(self.controller)):
            controller = self.controller()
            body = controller.patch()
        elif(inspect.isfunction(self.controller)):
            body = controller()
        else:
            raise TypeError

        self.finish(body)

class DeleteResource(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller
        
    def delete(self, path):
        if(inspect.isclass(self.controller)):
            controller = self.controller()
            body = controller.delete()
        elif(inspect.isfunction(self.controller)):
            body = controller()
        else:
            raise TypeError

        self.finish(body)

