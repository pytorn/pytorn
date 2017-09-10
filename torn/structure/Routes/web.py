#!/usr/bin/env python
# -*- coding: utf-8 -*-

from torn.api.route import Routing
import sys
sys.path.append("..")
from Controller import *

route = Routing()

route.get('/', MainController)
route.get('/404', NotFoundController)