#!/usr/bin/env python
# -*- coding: utf-8 -*-

from torn.api.app import Application
from Routes import web

def run():
	app = Application(route = web.route)
	app.run()

if __name__ == '__main__':
	run()