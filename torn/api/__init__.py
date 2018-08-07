#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import inspect

class GetResource(tornado.web.RequestHandler):
    def initialize(self, controller, url_for):
        self.controller = controller
        self.url_for = url_for

    def get(self, **kwargs):
        if(inspect.isclass(self.controller)):
            controller = self.controller(self.url_for) # pass RequestHandlers Reverse Url
            body = controller.get(self, **kwargs)
        elif(inspect.isfunction(self.controller)):
            body = controller(self, **kwargs)
        else:
            raise TypeError

        self.finish(body)

class PostResource(tornado.web.RequestHandler):
    def initialize(self, controller, url_for):
        self.controller = controller
        self.url_for = url_for

    def post(self, **kwargs):
        if(inspect.isclass(self.controller)):
            controller = self.controller()
            body = controller.post(self, **kwargs)
        elif(inspect.isfunction(self.controller)):
            body = controller(self, **kwargs)
        else:
            raise TypeError

        self.finish(body)

class PutResource(tornado.web.RequestHandler):
    def initialize(self, controller, url_for):
        self.controller = controller
        self.url_for = url_for
        
    def put(self, **kwargs):
        if(inspect.isclass(self.controller)):
            controller = self.controller()
            body = controller.put(self, **kwargs)
        elif(inspect.isfunction(self.controller)):
            body = controller(self, **kwargs)
        else:
            raise TypeError

        self.finish(body)

class PatchResource(tornado.web.RequestHandler):
    def initialize(self, controller, url_for):
        self.controller = controller
        self.url_for = url_for
        
    def patch(self, **kwargs):
        if(inspect.isclass(self.controller)):
            controller = self.controller()
            body = controller.patch(self, **kwargs)
        elif(inspect.isfunction(self.controller)):
            body = controller(self, **kwargs)
        else:
            raise TypeError

        self.finish(body)

class DeleteResource(tornado.web.RequestHandler):
    def initialize(self, controller, url_for):
        self.controller = controller
        self.url_for = url_for
        
    def delete(self, **kwargs):
        if(inspect.isclass(self.controller)):
            controller = self.controller()
            body = controller.delete(self, **kwargs)
        elif(inspect.isfunction(self.controller)):
            body = controller(self, **kwargs)
        else:
            raise TypeError

        self.finish(body)

