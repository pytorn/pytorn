#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import inspect
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape
from torn.exception import TornMethodNotAllowed

# class Controller will be an abstract class with implemented methods for implemented Controller
class Controller(tornado.web.RequestHandler):

    def __init__(self, application, request, **kwargs):
        super(Controller, self).__init__(application, request, **kwargs)
        
    def render(self, template, **data):
        """Renders the template using Jinja2 with given data arguments.

        """
        if(type(template) != str):
            raise TypeError("String expected")
        
        env = Environment(
            loader=FileSystemLoader(os.getcwd() + '/View'),
            autoescape=select_autoescape()
        )

        template = env.get_template(template)
        return self.finish(template.render(data))

    def get(self):
        raise TornMethodNotAllowed

    def post(self):
        raise TornMethodNotAllowed

    def delete(self):
        raise TornMethodNotAllowed

    def put(self):
        raise TornMethodNotAllowed

    def patch(self):
        raise TornMethodNotAllowed

    def head(self):
        raise TornMethodNotAllowed

    def options(self):
        raise TornMethodNotAllowed