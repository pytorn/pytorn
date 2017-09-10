#!/usr/bin/env python
# -*- coding: utf-8 -*-

from torn.api.app import Application
import Routes.web

def run():
	app = Application()
	app.run(routes = Routes.web.route.routes)

if __name__ == '__main__':
	run()