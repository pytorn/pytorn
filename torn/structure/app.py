#!/usr/bin/env python
# -*- coding: utf-8 -*-

from torn.api.app import Application

def run():
	app = Application(port = 8080)
	app.run()

if __name__ == '__main__':
	run()