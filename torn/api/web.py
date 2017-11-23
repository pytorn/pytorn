#!/usr/bin/env python
# -*- coding: utf-8 -*-

from tornado.httpclient import HTTPRequest, HTTPResponse

class Request(HTTPRequest):
    """Request class inherits tornado.httpclient.HTTPRequest class."""
    pass
class Response(HTTPResponse):
    """Request class inherits tornado.httpclient.HTTPResponse class."""
    pass
