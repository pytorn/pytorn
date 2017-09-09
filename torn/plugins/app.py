#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

def settings(object):
	with open(object.root_dir + '/Config/config.json') as config:
		config = json.load(config)
		object.name = config['name']
		object.port = config['port']
		object.mode = config['devmode']