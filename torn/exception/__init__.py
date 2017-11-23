#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Custom Exception module for Torn"""

class TornException(Exception):
    """Torn parent exception class.
    It can be thrown for uncertain errors.

    raise TornException returns
    > TornException: Something seems torn!!!
    """
    def __init__(self, status_code=None):
        response_code = ""
        if status_code and isinstance(status_code, int):
            response_code = "Response " + status_code + ": " 
        Exception.__init__(self, response_code + "Something seems torn!!!") #Damn !!!!


class TornNotFoundError(Exception):
    """Torn exception class for resource \
    not found exception.

    raise TornNotFoundError returns
    > TornNotFoundError: Resource not found.
    """
    def __init__(self):
        Exception.__init__(self, "Resource not found.")
    