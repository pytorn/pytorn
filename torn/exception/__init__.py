#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Custom Exception module for Torn"""

import tornado.web

class TornException(tornado.web.HTTPError):
    """Torn parent exception class.
    It can be thrown for uncertain errors.

    raise TornException returns
    > TornException: Something seems torn!!!
    """
    def __init__(self, status_code):
        super(TornException, self).__init__(status_code=status_code, log_message="Something seems torn!") #damn


class TornNotFoundError(tornado.web.HTTPError):
    """Torn exception class for resource \
    not found exception.

    raise TornNotFoundError returns
    > TornNotFoundError: Response 404: Resource not found.
    """
    def __init__(self):
        super(TornNotFoundError, self).__init__(status_code=404, log_message="Response 404: Resource not found.")


class TornInternalError(tornado.web.HTTPError):
    """Torn exception class for Internal Server Error.

    raise TornInternalError returns
    > TornInternalError: Response 500: Internal Server Error.
    """
    def __init__(self):
        super(TornInternalError, self).__init__(status_code=500, log_message="Response 500: Internal Server Error.")


class TornMethodNotAllowed(tornado.web.HTTPError):
    """Torn exception class for Invalid Request method.

    raise TornMethodNotAllowed returns
    > TornMethodNotAllowed: Response 405: Method Not Allowed.
    """
    def __init__(self):
        super(TornMethodNotAllowed, self).__init__(status_code=405, log_message="Response 405: Method Not Allowed.")

class TornErrorHandler(tornado.web.RequestHandler):
    def initialize(self, status_code):
        self.status_code = status_code

    def write_error(self, status_code, **kwargs):
        if self.status_code in [403, 405, 404, 500, 503]:
            self.set_status(self.status_code)
            self.write('Error %s' % self.status_code)
        else:
            self.write('BOOM!')