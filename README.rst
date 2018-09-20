.. image:: https://raw.githubusercontent.com/andeladenaro/torn/master/resources/Banner.png

Torn     
====

Torn, also known as PyTorn, is a full fledged Tornado MVC framework.

.. image:: https://travis-ci.org/pytorn/torn.svg?branch=master
    	 :target: https://travis-ci.org/pytorn/torn


Versions
--------

torn-cli works with Python 2.4-3.5


Installation [UPDATED]
-------------------------

::

	pip install git+https://github.com/shubhodeep9/torn.git


Usage [UPDATED]
------------------

::

    $ torn                 
    usage: torn [action [arguments]]

    A full fledged MVC framework based on Tornado and Jinja2 templating

    positional arguments:
    {new,run,controller,version}	Action to be performed with the application
    optional arguments:
    -h, --help            show this help message and exit
    
    The actions are:
    new             Create a new torn app
    run             Run the app and start a Web server for development
    controller      Create a new controller
    version         returns the current version of torn
    
    
::

    $ torn run
    
Gives:

.. image:: https://raw.githubusercontent.com/pytorn/torn/master/resources/torn.png
