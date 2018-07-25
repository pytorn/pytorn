#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Plugin app helper module."""

import json
import re
import tornado.web
from torn.exception import TornInternalError, TornNotFoundError, TornMethodNotAllowed

def settings(instance):
    """Definition to set settings from config file to the app instance."""
    with open(instance.root_dir + '/Config/config.json') as config:
        config = json.load(config)
        instance.name = config['name']
        instance.port = config['port']
        # default host
        instance.host = "http://localhost"
        if 'host' in config:
            instance.host = config['host']
        instance.mode = config['devmode']
    return instance

def routing(routes, request):
    """Definition for route matching : helper"""

    # strip trailing slashes from request path
    path = request.path.strip('/')

    # iterate through routes to match
    args = {}
    for name, route in routes.iteritems():
        if route['path'] == '^':
            # this section exists because regex doesn't work for null character as desired
            if path == '':
                match = [True]
            else:
                match = []
        else:
            match = re.findall(route['path'], path)
        
        if match:
            # found the matching url, iterate through variables to pass data
            # check if method exists
            if not request.method in route['method']:
                raise TornMethodNotAllowed
            
            values = match[0] # in form of tuples
            if type(values) != bool:
                for i in range(len(route['variables'])):
                    # if value is blank, check if default exists and pass it instead
                    if type(values) == str:
                        args[route['variables'][i]] = values
                    else:
                        if not values[i] and route['variables'][i] in route['defaults']:
                            values[i] = route['defaults'][route['variables'][i]]
                        args[route['variables'][i]] = values[i]
            
            # we have the variables we need, args, path, controller
            return {
                'kwargs'        : args,
                'controller'    : route['controller']
            }
    raise TornNotFoundError

def uri_creator(uri, regex, defaults):
    """Creates url and replaces regex and gives variables"""

    # strip trailing slash
    uri = uri.strip('/')

    # take out variables in uri
    matches = re.findall('{[a-zA-Z0-9\_]+}', uri)
    default_regex = '[a-zA-Z0-9]+'
    
    variables = []

    # iter through matches and replace it with user given regex \
    # if not present, then replace it with default regex
    for match in matches:
        variable = re.sub("{|}", "", match)

        # replace the variable with regex
        set_regex = default_regex
        if variable in regex:
            set_regex = regex[variable]
        
        # set default
        if variable in defaults:
            set_regex = set_regex + "|"

        variables.append(variable)
        
        uri = uri.replace(match, "(" + set_regex + ")")
        
    # debug, put a ^ starts with for exact matching
    uri = '^' + uri
    return {
        'variables' : variables,
        'uri'       : uri
    }

