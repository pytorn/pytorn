#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tornado.web
import inspect
import os
from jinja2 import Environment, FileSystemLoader, select_autoescape

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