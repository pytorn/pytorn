#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.routing
import torn.plugins.app
import torn.api
from torn.exception import TornErrorHandler, TornNotFoundError, TornUrlNameNotFound
import tornado.web
import torn.plugins
import re
import os



class Route:

    def __init__(self, uri: str, controller: torn.api.Controller):
        self.uri = uri
        self.controller = controller
        self.uri_vars = torn.plugins.app.get_uri_variables(uri)
        self.params = {}
        self.default_vals = {}
        self.__name = None

    def __make_params(self, params):
        DEFAULT_REGEX = '[a-zA-Z0-9]+';
        for var in self.uri_vars:
            if var not in params:
                params[var] = DEFAULT_REGEX
        return params

    def args(self, params):
        self.params = self.__make_params(params)
        return self

    def defaults(self, value):
        self.default_vals = value
        return self

    def name(self, value):
        self.__name = value
        return self

    def get_name(self):
        return self.__name

    def get_controller(self):
        return self.controller

    def __get_regex(self, path: str):
        uri = torn.plugins.app.uri_creator(self.uri, self.params, self.default_vals)
        path = path.strip('/')
        if uri == '^$' and path == '':
            match = [True]
        else:
            match = re.findall(uri, path)

        return match

    def matches(self, request):
        match = self.__get_regex(request.path)
        return bool(match)

    def get_args(self, request):
        match = self.__get_regex(request.path)
        values = match[0]
        uri_vars = self.uri_vars

        args = {}
        if type(values) != bool:
            for i in range(len(uri_vars)):
                # if value is blank, check if default exists and pass it instead
                uri_var = uri_vars[i]
                if type(values) != str:
                    value = values[i]
                else: 
                    value = values
                exact_matches = re.findall(self.params[uri_var], value)
                if len(exact_matches) > 0:
                    args[uri_var] = exact_matches[0]
                else:
                    args[uri_var] = self.__get_default_value(uri_var)
        return args

    def __get_default_value(self, uri_var: str):
        return self.default_vals[uri_var]

class RouteCollection:

    def __init__(self):
        self.routes = []
        self.named_routes = {}

    def add_route(self, route: Route):
        self.routes.append(route)

    def match(self, request):
        for route in self.routes:
            if route.matches(request):
                return route
        
        raise TornNotFoundError

    def map_names(self):
        for route in self.routes:
            name = route.get_name()
            if route.get_name():
                self.named_routes[route.get_name()] = route

    def get_route_by_name(self, name: str):
        if name in self.named_routes:
            return self.named_routes[name]
        raise TornUrlNameNotFound

class Routing:
    def __init__(self):
        self.routes = RouteCollection()

    def add(self, uri: str, contoller: torn.api.Controller):
        route = Route(uri, contoller)
        self.routes.add_route(route)
        return route


    def getRouteCollection(self):
        self.routes.map_names()
        return self.routes

class Router(tornado.routing.Router):
    def __init__(self, app: tornado.web.Application, route = Routing()):
        self.app = app
        self.routes = route.getRouteCollection()

    def url_for(self, name, kwargs=dict()):
        try:
            route = self.routes.get_route_by_name(name)
            uri = route.uri
            for variable in route.uri_vars:
                uri = uri.replace("{" + variable + "}", kwargs[variable])
            return uri
        except Exception as e:
            return ""

    def find_handler(self, request, **kwargs):
        # logging to be done here
        try:
            if torn.plugins.app.is_static(request.path):
                # to serve static files
                return self.app.get_handler_delegate(request, tornado.web.StaticFileHandler, target_kwargs=dict(path=os.getcwd() + "/Assets"), path_kwargs=dict(path=request.path.strip('/')))
            else:
                route = self.routes.match(request)
                torn.plugins.log.info(request.method + "\t" + request.path, code=str(200))
                return self.app.get_handler_delegate(request, route.get_controller(), path_kwargs=route.get_args(request))
        except tornado.web.HTTPError as e:
            torn.plugins.log.warning(request.method + "\t" + request.path, code=str(e.status_code))
            return self.app.get_handler_delegate(request, TornErrorHandler, target_kwargs=dict(status_code=e.status_code))

