#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, sys
import tornado.web
import tornado.ioloop
import tornado.httpserver
from torn.api.route import Routing, Router
from ..plugins import app

class Application:
    # the application class, to initialize the server
    # The settings will be read from 
    def __init__(self):
        self.root_dir = os.getcwd()
        # gonna read settings from Config/config.json
        self = app.settings(self)


    # method to execute the application
    def run(self, routes):
        application = tornado.web.Application()
        router = Router(application, routes)
        http_server = tornado.httpserver.HTTPServer(router)
        http_server.listen(self.port)
        tornado.ioloop.IOLoop.current().start()


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
    def handle(self, request):
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

