"""Module handles torn_cli actions and does the needful"""
import os
def handler(args):
    if args.action[0] == 'run':
        runHandler()

def runHandler():
    try:
        from subprocess import call
        if 'app.py' in os.listdir('.') and 'Config' in os.listdir('.'):
            call(["python", "app.py"])
        else:
            raise Exception
    except Exception as e:
        print 'Not a torn app'