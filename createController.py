import os
from colors import bcolors
class createNewController():
	NAME = ''
	CURRENT_DIR = os.getcwd()
	INFO = bcolors.OKBLUE+'INFO:'+bcolors.ENDC
	SUCCESS = bcolors.OKGREEN+'SUCCESS:'+bcolors.ENDC
	def __init__(self,name):
		self.NAME = name+'.py'
		self.create()

	def create(self):
		path = self.CURRENT_DIR+'/controllers/'
		os.chdir(path)
		controllerData = "#"+self.NAME[:len(self.NAME)-3]+" Controller created"
		conf = open(self.NAME,'w')
		conf.write(controllerData)
		print(self.NAME[:len(self.NAME)-3]+' Controller created.')
