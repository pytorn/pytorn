#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import inspect

class GetResource(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller

    def get(self, **kwargs):
        if(inspect.isclass(self.controller)):
            controller = self.controller(self.reverse_url) # pass RequestHandlers Reverse Url
            body = controller.get(**kwargs)
        elif(inspect.isfunction(self.controller)):
            body = controller(**kwargs)
        else:
            raise TypeError

        self.finish(body)

class PostResource(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller

    def post(self, **kwargs):
        if(inspect.isclass(self.controller)):
            controller = self.controller()
            body = controller.post(**kwargs)
        elif(inspect.isfunction(self.controller)):
            body = controller(**kwargs)
        else:
            raise TypeError

        self.finish(body)

class PutResource(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller
        
    def put(self, **kwargs):
        if(inspect.isclass(self.controller)):
            controller = self.controller()
            body = controller.put(**kwargs)
        elif(inspect.isfunction(self.controller)):
            body = controller(**kwargs)
        else:
            raise TypeError

        self.finish(body)

class PatchResource(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller
        
    def patch(self, **kwargs):
        if(inspect.isclass(self.controller)):
            controller = self.controller()
            body = controller.patch(**kwargs)
        elif(inspect.isfunction(self.controller)):
            body = controller(**kwargs)
        else:
            raise TypeError

        self.finish(body)

class DeleteResource(tornado.web.RequestHandler):
    def initialize(self, controller):
        self.controller = controller
        
    def delete(self, **kwargs):
        if(inspect.isclass(self.controller)):
            controller = self.controller()
            body = controller.delete(**kwargs)
        elif(inspect.isfunction(self.controller)):
            body = controller(**kwargs)
        else:
            raise TypeError

        self.finish(body)

