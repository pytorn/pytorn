"""Torn module comprises of command line, and library to use the torn
MVC framework, which is based on tornado."""
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2016 Shubhodeep Mukherjee
# All Rights Reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from __future__ import print_function
import torn

__version__ = "0.0.4"

def main():
    """The executable for torn command line, that checks
    through everything."""
    try:
        torn.cli()
    except KeyboardInterrupt:
        print('\nTerminating process')

if __name__ == '__main__':
    main()
