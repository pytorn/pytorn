#!/usr/bin/env python
# -*- coding: utf-8 -*-

from torn.api.app import Routing

route = Routing()

route.add('/', MainController)