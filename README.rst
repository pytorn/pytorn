torn
====

torn-cli : A command line application to easily create and run tornado applications.

Change log
----------
Fixed tornado missing issue.


Versions
--------

torn-cli works with Python 2.4-3.5


Installation
------------

::

	pip install torn

or

::

	pip install git+https://github.com/shubhodeep9/torn.git


Usage
-----

::

    $ torn -h                     
	Torn is tool for managing tornado web client.

	usage: torn command [arguments]

	positional arguments:
	  command     Specify what command to proceed

	optional arguments:
	  -h, --help  show this help message and exit

	The commands are:
		new		Create a Tornado Application
		run		run the app and start a Web server for development
		api		create an API tornado application
