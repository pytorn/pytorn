#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Module for Torn classes for Request and Response"""

from tornado.httpclient import HTTPRequest, HTTPResponse

class Request(HTTPRequest):
    """Request class inherits tornado.httpclient.HTTPRequest class."""
    pass
class Response(HTTPResponse):
    """Response class inherits tornado.httpclient.HTTPResponse class."""
    pass
