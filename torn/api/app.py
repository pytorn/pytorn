#!/usr/bin/env python
# -*- coding: utf-8 -*-
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
import webbrowser

class Application:
    # the application class, to initialize the server
    # The settings will be read from
    def __init__(self):
        self.root_dir = os.getcwd()
        # gonna read settings from Config/config.json
        self = app.settings(self)
        logging.getLogger('tornado.access').disabled = True


    # method to execute the application
    def run(self, routes, autoreload=True):
        try:
            application = tornado.web.Application(autoreload=autoreload)
            router = torn.api.route.Router(application, routes)
            http_server = tornado.httpserver.HTTPServer(router)
            http_server.listen(self.port)
            torn.plugins.log.info("Server initiated. Visit " + self.host + ":" + str(self.port))
            webbrowser.open(self.host + ":" + str(self.port))
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


    def in_exceptions(self, request):
        # traverse the array and check if the url exists \
        # if does, then terminate the process
        for excepts in self._exceptions:
            if excepts == request.path:
                return True

        # Else return False
        return False


def load_controllers(path: str):
    output = []
    for loader, name, is_pkg in pkgutil.walk_packages(path):
        module = loader.find_module(name).load_module(name)

        for name, value in inspect.getmembers(module):
            if name.startswith('__'):
                continue

            globals()[name] = value
            output.append(name)

    return output
