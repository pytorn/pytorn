#!/usr/bin/env python
# -*- coding: utf-8 -*-

from torn.api.app import TornadoApp

def run():
	app = TornadoApp(port = 8080)
	app.run()

if __name__ == '__main__':
	run()