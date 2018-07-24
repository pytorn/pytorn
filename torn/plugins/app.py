#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Plugin app helper module."""

import json
import re
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

def uri_creater(uri, regex, defaults):
    """Creates url and replaces regex and gives variables"""

    # take out variables in uri
    matches = re.findall('{[a-zA-Z0-9\_]+}', uri)
    default_regex = '[a-zA-Z0-9]+'
    # iter through matches and replace it with user given regex \
    # if not present, then replace it with default regex
    variables = []
    for match in matches:
        variable = re.sub("{|}", "", l)
        variables.append(variable)

        # replace the variable with regex
        set_regex = default_regex
        if variable in regex:
            set_regex = regex[variable]
        
        # set default
        if variable in defaults:
            if variable == False:
                defaults[variable] = ""
            set_regex = "(" + set_regex + "|" + defaults[variable] + ")"
        
        uri = uri.replace(variable, set_regex)
        
    return {
        'variables' : variables,
        'uri'       : uri
    }

