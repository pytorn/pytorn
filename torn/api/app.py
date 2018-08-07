#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os
import tornado.web
import tornado.ioloop
import tornado.httpserver
import torn.api.route
from torn.plugins import app
import pkgutil
import inspect
import logging
import torn.plugins.log
from jinja2 import Environment, FileSystemLoader, select_autoescape

class Application:
    # the application class, to initialize the server
    # The settings will be read from
    def __init__(self):
        self.root_dir = os.getcwd()
        # gonna read settings from Config/config.json
        self = app.settings(self)
        logging.getLogger('tornado.access').disabled = True


    # method to execute the application
    def run(self, routes, autoreload = False):
        try:
            application = tornado.web.Application(autoreload=autoreload)
            router = torn.api.route.Router(application, routes)
            http_server = tornado.httpserver.HTTPServer(router)
            http_server.listen(self.port)
            torn.plugins.log.info("Server initiated. Visit " + self.host + ":" + str(self.port))
            tornado.ioloop.IOLoop.current().start()
        except KeyboardInterrupt:
            print()
            torn.plugins.log.info("Stopping all services ...")
            tornado.ioloop.IOLoop.current().stop()
            torn.plugins.log.info("Stopped. Exiting. Cya!")


# class Middleware that can be extended to put features
class Middleware:

    def __init__(self):
        # Add to __exceptions if you don't want middlewares \
        # to operate on specific urls.
        self._exceptions = []

        # Add 'name' : Class of middleware in this list of \
        # dictionary. Eg: [{'csrf' : VerifyCsrfToken}]
        self._middlwares = []


    # Write the logic to handle the Request
    # Output Response
    def handle(self, request, next):
        # When you extend, remember to call in_exceptions and \
        # other functions if exists
        pass


    def in_exceptions(request):
        # traverse the array and check if the url exists \
        # if does, then terminate the process
        for excepts in self._exceptions:
            if excepts == request.path:
                return True

        # Else return False
        return False

# class Controller will be an abstract class with implemented methods for implemented Controller
class Controller:

    def __init__(self, url_for = None):
        # using reverse url for Get Handler
        if url_for:
            self.url_for = url_for

    # index method will be implemented on get method
    def get(self, request):
        raise NotImplementedError

    # post method will be implemented on post method
    def post(self, request):
        raise NotImplementedError
    
    # put method will be implemented on put method
    def put(self, request):
        raise NotImplementedError

    # patch method will be implemented on patch method
    def patch(self, request):
        raise NotImplementedError

    # delete method will be implemented on delete method
    def delete(self, request):
        raise NotImplementedError

    def render(self, template, **data):
        if(type(template) != str):
            raise TypeError("String expected")
        
        env = Environment(
            loader=FileSystemLoader(os.getcwd() + '/View'),
            autoescape=select_autoescape()
        )
        # define url_for function for jinja
        env.globals['url_for'] = self.url_for

        template = env.get_template(template)
        return template.render(data)

def load_controllers(path):
    output = []
    for loader, name, is_pkg in pkgutil.walk_packages(path):
        module = loader.find_module(name).load_module(name)

        for name, value in inspect.getmembers(module):
            if name.startswith('__'):
                continue

            globals()[name] = value
            output.append(name)

    return output
