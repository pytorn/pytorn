#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.routing
from torn.api import *
import torn.plugins.app
from torn.exception import TornErrorHandler
import tornado.web

class Routing:
    def __init__(self):
        self.routes = {}

    def _add(self, method, uri, name, controller, defaults={}, regex={}):
        # replace variables with regex if exists or with default regex
        uri = torn.plugins.app.uri_creator(uri, regex, defaults)
        self.routes[name] = {
            'path'          : uri['uri'],
            'variables'     : uri['variables'],
            'defaults'      : defaults,
            'controller'    : controller
        }
        if 'method' in self.routes[name]:
            self.routes[name]['method'].append(method)
        else:
            self.routes[name]['method'] = [method]

    def get(self, uri, name, controller, defaults={}, regex={}):
        self._add('GET', uri, name, controller, defaults={}, regex={})

    def post(self, uri, name, controller, defaults={}, regex={}):
        self._add('POST', uri, name, controller, defaults={}, regex={})

    def put(self, uri, name, controller, defaults={}, regex={}):
        self._add('PUT', uri, name, controller, defaults={}, regex={})

    def patch(self, uri, name, controller, defaults={}, regex={}):
        self._add('PATCH', uri, name, controller, defaults={}, regex={})

    def delete(self, uri, name, controller, defaults={}, regex={}):
        self._add('DELETE', uri, name, controller, defaults={}, regex={})

    def getRouteCollection(self):
        return self.routes

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
        self.routes = route.getRouteCollection()

    def find_handler(self, request, **kwargs):
        try:
            handler = self.map_handlers[request.method]
            route_data = torn.plugins.app.routing(self.routes, request=request)
            return self.app.get_handler_delegate(request, handler, path_kwargs=route_data['kwargs'], target_kwargs=dict(controller=route_data['controller']))
        except tornado.web.HTTPError as e:
            print e.status_code
            return self.app.get_handler_delegate(request, TornErrorHandler, target_kwargs=dict(status_code=e.status_code))
