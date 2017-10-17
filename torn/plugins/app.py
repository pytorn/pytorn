#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import tornado.web

def settings(object):
    with open(object.root_dir + '/Config/config.json') as config:
        config = json.load(config)
        object.name = config['name']
        object.port = config['port']
        object.mode = config['devmode']

def routing(routes, method = 'GET', path = ''):
    if path in routes:
        if method in routes[path]['method']:
            return routes[path]['controller']
        else:
            return (500)
    else:
        return routes['/404']['controller']