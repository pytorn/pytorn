import os
from colors import bcolors
class createNewController():
	NAME = ''
	def __init__(self,name):
		self.NAME = name+'.py'
		self.create()

	def create(self):
		CURRENT_DIR = os.getcwd()
		#For apis and webapps, controller directory is set to controllers
		path = CURRENT_DIR+'/controllers/'
		os.chdir(path)
		'''
		Initialised controllerData, that will help in creating preset data
		like importing modules etc
		self.NAME[:len(self.NAME)-3] is used to remove the extension .py from the file
		while printing the message on command line.
		'''
		controllerData = "#"+self.NAME[:len(self.NAME)-3]+" Controller created"
		conf = open(self.NAME,'w')
		conf.write(controllerData)
		print(self.NAME[:len(self.NAME)-3]+' Controller created.')
