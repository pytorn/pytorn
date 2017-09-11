#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.routing
from torn.api import *
import torn.plugins.app

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

class Router(tornado.routing.Router):
    def __init__(self, app, route = Routing()):
        self.app = app
        self.map_handlers = {
            'GET'       : GetResource,
            'POST'      : PostResource,
            'PUT'       : PutResource,
            'PATCH'     : PatchResource,
            'DELETE'    : DeleteResource
        }
        self.routes = route.routes

    def find_handler(self, request, **kwargs):
        handler = self.map_handlers[request.method]
        controller = torn.plugins.app.routing(self.routes, method=request.method, path=request.path)
        return self.app.get_handler_delegate(request, handler, path_args=[request.path], target_kwargs=dict(controller=controller))
