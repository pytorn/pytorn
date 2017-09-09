#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tornado.routing.Router
import __init__ as api

class Routing(tornado.routing.Router):

    def __init__(self, app):
        self.app = app

    def _add(self, uri, controller):
        print (uri)

    def get(self, uri, controller):
        self._add('GET', uri, controller)

    def post(self, uri, controller):
        self._add('POST', uri, controller)