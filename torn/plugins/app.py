"""Plugin app helper module."""
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

def settings(instance):
    """Definition to set settings from config file to the app instance."""
    with open(instance.root_dir + '/Config/config.json') as config:
        config = json.load(config)
        instance.name = config['name']
        instance.port = config['port']
        instance.mode = config['devmode']
    return instance

def routing(routes, method='GET', path=''):
    """Definition for route matching : helper"""
    if path in routes:
        if method in routes[path]['method']:
            return routes[path]['controller']
        else:
            return 500
    else:
        return routes['/404']['controller']
    