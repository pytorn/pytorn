#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Plugin app helper module."""

import json
from torn.exception import TornInternalError, TornNotFoundError

def settings(instance):
    """Definition to set settings from config file to the app instance."""
    with open(instance.root_dir + '/Config/config.json') as config:
        config = json.load(config)
        instance.name = config['name']
        instance.port = config['port']
        instance.mode = config['devmode']
    return instance

def routing(routes, request):
    """Definition for route matching : helper"""

    path = request.path
    method = request.method
    if path in routes:
        if method in routes[path]['method']:
            return routes[path]['controller']
        else:
            raise TornMethodNotAllowed
    else:
        raise TornNotFoundError

