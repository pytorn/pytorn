"""Module handles torn_cli actions and does the needful"""
import os
import requests
import zipfile
__version__ = "0.0.4"

def handler(args):
    if args.action[0] == 'run':
        runHandler()
    elif args.action[0].lower() == 'new':
        newHandler(args.name)
    elif args.action[0].lower() == 'version':
        versionHandler()
    elif args.action[0].lower() == 'controller':
        controllerHandler(args.name)                       

def runHandler():
    try:
        from subprocess import call
        if 'app.py' in os.listdir('.') and 'Config' in os.listdir('.'):
            call(["python", "app.py"])
        else:
            raise Exception
    except Exception as e:
        print 'Not a torn app'

def newHandler(name=None):
    name = name or "app"
    #  for new app , cloning form main repository
    print('creating new app...')
    url = 'https://github.com/pytorn/app/archive/master.zip'
    r = requests.get(url , allow_redirects=True)
    open('app.zip' , 'wb').write(r.content)
    zip = zipfile.ZipFile("app.zip")
    zip.extractall()
    zip.close()
    os.rename("app-master" , name)
    os.remove("app.zip")

def versionHandler():
    print(__version__)


def controllerHandler(name = None):
    name = str(name) or "User"
    print('creating controller '+ name + '...' )
    s = "#!/usr/bin/env python\n# -*- coding: utf-8 -*-\nfrom torn.api import Controller\nclass "+ name +"Controller(Controller):\n\tdef get(self):\n\t\tpass"
    open(name + "Controller" , 'w').write(s)
