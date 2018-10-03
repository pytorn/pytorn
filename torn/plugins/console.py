"""Module handles torn_cli actions and does the needful"""
import os
import requests
import zipfile
__version__ = "0.0.4"

def handler(args):
    if args.action[0] == 'run':
        runHandler()
    elif args.action[0].lower() == 'new':
        runNew_cmd()
    elif args.action[0].lower() == 'version':
        runVersion_cmd()                   

def runHandler():
    try:
        from subprocess import call
        if 'app.py' in os.listdir('.') and 'Config' in os.listdir('.'):
            call(["python", "app.py"])
        else:
            raise Exception
    except Exception as e:
        print 'Not a torn app'

def runNew_cmd():
    #  for new app , cloning form main repository
    print('creating new app...')
    url = 'https://github.com/pytorn/app/archive/master.zip'
    r = requests.get(url , allow_redirects=True)
    open('app.zip' , 'wb').write(r.content)
    zip = zipfile.ZipFile("app.zip")
    zip.extractall()
    zip.close()
    os.rename("app-master" , "app")
    os.remove("app.zip")

def runVersion_cmd():
    print(__version__)