"""Module handles torn_cli actions and does the needful"""
import os

__version__ = "0.0.4"

def handler(args):
    if args.action[0] == 'run':
        runHandler()
    elif args.action[0] == 'new':
        #  for new app , cloning form main repository
        os.system('git clone git@github.com:pytorn/app.git')
    elif args.action[0] == 'version':
        print(__version__)                    

def runHandler():
    try:
        from subprocess import call
        if 'app.py' in os.listdir('.') and 'Config' in os.listdir('.'):
            call(["python", "app.py"])
        else:
            raise Exception
    except Exception as e:
        print 'Not a torn app'