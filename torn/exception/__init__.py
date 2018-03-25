#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Custom Exception module for Torn"""

import tornado.httpclient

class TornException(tornado.httpclient.HTTPError):
    """Torn parent exception class.
    It can be thrown for uncertain errors.

    raise TornException returns
    > TornException: Something seems torn!!!
    """
    def __init__(self, status_code, response=None):
        super(TornException, self).__init__(code=status_code, response=response, message="Something seems torn!") #damn


class TornNotFoundError(tornado.httpclient.HTTPError):
    """Torn exception class for resource \
    not found exception.

    raise TornNotFoundError returns
    > TornNotFoundError: Response 404: Resource not found.
    """
    def __init__(self, response):
        super(TornNotFoundError, self).__init__(code=404, response=response, message="Response 404: Resource not found.")


class TornInternalError(tornado.httpclient.HTTPError):
    """Torn exception class for Internal Server Error.

    raise TornInternalError returns
    > TornInternalError: Response 500: Internal Server Error.
    """
    def __init__(self):
        super(TornInternalError, self).__init__(code=500, response=response, message="Response 500: Internal Server Error.")


class TornMethodNotAllowed(tornado.httpclient.HTTPError):
    """Torn exception class for Invalid Request method.

    raise TornMethodNotAllowed returns
    > TornMethodNotAllowed: Response 405: Method Not Allowed.
    """
    def __init__(self):
        super(TornMethodNotAllowed, self).__init__(code=405, response=response, message="Response 405: Method Not Allowed.")
