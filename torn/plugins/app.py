#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Plugin app helper module."""

import json
import re
import tornado.web
import yaml
from torn.exception import TornInternalError, TornNotFoundError, TornMethodNotAllowed

def settings(instance):
    """Definition to set settings from config file to the app instance."""
    with open(instance.root_dir + '/Config/config.yml') as config:
        config = yaml.load(config)
        instance.name = config['name']
        instance.port = config['web']['port']
        # default host
        instance.host = "http://localhost"
        if 'host' in config['web']:
            instance.host = config['web']['host']
        instance.debug = config['debug']
    return instance

def uri_creator(uri, params, defaults):
    """Creates url and replaces regex"""

    # strip trailing slash and if it already has any regex
    uri = uri.strip('/')

    # take out variables in uri
    matches = re.findall(r"\/{[a-zA-Z0-9\_]+}", uri)
    default_regex = '[a-zA-Z0-9]+'
    # iter through matches and replace it with user given regex \
    # if not present, then replace it with default regex
    for match in matches:
        var_match = match.strip("/")
        variable = re.sub("{|}", "", var_match)

        # replace the variable with regex
        set_regex = default_regex
        if variable in params:
            set_regex = params[variable]
        
        # set default
        if variable in defaults:
            set_regex = set_regex + "|"
        
        uri = uri.replace(match, "(\/" + set_regex + ")")
        
    # debug, put a ^ starts and $ ends with for exact matching
    uri = '^' + uri + '$'
    return uri

def get_uri_variables(uri):
    uri = uri.strip('/')

    # take out variables in uri
    matches = re.findall(r"\{[a-zA-Z0-9\_]+}", uri)

    variables = [re.sub("{|}", "", match) for match in matches]

    return variables

def is_static(file):
    static_extentions = re.findall(r".+(\.css|\.js|\.ttf|\.png|\.jpg|\.gif|\.ico|robots\.txt)$", file)
    return len(static_extentions)