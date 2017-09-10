#!/usr/bin/env python
# -*- coding: utf-8 -*-

from torn.api.route import Routing
from ..Controller import *

route = Routing()

route.add('/', MainController.index)