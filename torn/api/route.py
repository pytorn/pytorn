#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.routing
from torn.api import *
import torn.plugins.app

class Routing:
    def __init__(self):
        self.routes = {}

    def _add(self, method, uri, name, controller, defaults=[], regex=[]):
        # replace variables with regex if exists or with default regex
        uri = torn.plugins.app.uri_creator(uri, regex, defaults)
        self.routes[name] = {
            'path'          : uri,
            'controller'    : controller
        }
        if('method' in self.routes[uri]):
            self.routes[uri]['method'].append(method)
        else:
            self.routes[uri]['method'] = [method]

    def get(self, uri, name, controller, defaults=[], regex=[]):
        self._add('GET', uri, name, controller, defaults=[], regex=[])

    def post(self, uri, name, controller, defaults=[], regex=[]):
        self._add('POST', uri, name, controller, defaults=[], regex=[])

    def put(self, uri, name, controller, defaults=[], regex=[]):
        self._add('PUT', uri, name, controller, defaults=[], regex=[])

    def patch(self, uri, name, controller, defaults=[], regex=[]):
        self._add('PATCH', uri, name, controller, defaults=[], regex=[])

    def delete(self, uri, name, controller, defaults=[], regex=[]):
        self._add('DELETE', uri, name, controller, defaults=[], regex=[])

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
        controller = torn.plugins.app.routing(self.routes, request=request)
        return self.app.get_handler_delegate(request, handler, path_args=[request.path], target_kwargs=dict(controller=controller))
