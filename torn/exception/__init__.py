#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TornException(Exception):
	def __init__(self):
		Exception.__init__(self, "Something seems torn!!!") #Damn !!!!
