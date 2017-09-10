#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.routing.Router
from __init__ import *

class Router(tornado.routing.Router):
    def __init__(self, app, routes):
        self.app = app
        self.map_handlers = {
            'GET'       : GetResource,
            'POST'      : PostResource,
            'PUT'       : PutResource,
            'PATCH'     : PatchResource,
            'DELETE'    : DeleteResource
        }
        self.routes = routes

    def find_handler(self, request, **kwargs):
        try:
            handler = self.map_handlers[request.method]
        except:
            handler = MethodNotAllowedResource
        return self.app.get_handler_delegate(request, handler, path_args=[request.path, self.routes])

class Routing:
    def __init__(self):
        self.routes = {}

    def _add(self, method, uri, controller):
        self.routes[uri] = {
            'path'          : uri,
            'controller'    : controller
        }
        if('method' in self.routes[uri]):
            self.routes[uri]['method'].append(method)
        else:
            self.routes[uri]['method'] = [method]

    def get(self, uri, controller):
        self._add('GET', uri, controller)

    def post(self, uri, controller):
        self._add('POST', uri, controller)