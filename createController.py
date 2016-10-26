import os
from colors import bcolors
def createControllerFunction(method):
	
	'''Check if method is GET or POST, or PREPARE, create content for them separately,
	else a generic function content will be created
	'''
	
	if(method.upper() == "GET"):		
		controllerContent = """\n\tdef get(self):\n\t\tself.write('Hello World')"""
	elif (method.upper() == "POST"):
		jsonContent = {
			'message':'Hello World',
			'method':'POST'
		}
		controllerContent = "\n\tdef post(self):\n\t\tself.write(tornado.escape.json_encode("+ str(jsonContent) + "))"
	elif(method.upper() == "PREPARE"):
		controllerContent = """\n\tdef prepare(self):\n\t\tif self.request.headers["Content-Type"].startswith("application/json"):\n\t\t\tself.json_args = json.loads(self.request.body)\n\t\telse:\n\t\t\tself.json_args = None"""
	else:
		controllerContent = "\n\tdef "+method.lower()+"(self):\n\t\t#Your code here..."
	
	return controllerContent

class createNewController():
	NAME = ''
	def __init__(self,arguments):
		self.NAME = arguments[2]+'.py'
		self.ACTIONS =  []
		for action in arguments[3:]:
			self.ACTIONS.append(action)
		self.create()


	def create(self):
		CURRENT_DIR = os.getcwd()
		#For apis and webapps, controller directory is set to controllers
		path = CURRENT_DIR+'/controllers/'
		os.chdir(path)

		#Check if the controller already exists or not.
		if not os.path.isfile(self.NAME):
			controllerName = self.NAME[:len(self.NAME)-3]
			'''
			Initialised controllerData, that will help in creating preset data
			like importing modules etc
			self.NAME[:len(self.NAME)-3] is used to remove the extension .py from the file
			while printing the message on command line.
			'''
			controllerData = []

			#Collect all actions and methods
			for method in self.ACTIONS:
				controllerData.append(createControllerFunction(method))
			className = controllerName.lower().replace('controller','')

			#Write controller Data

			controllerClassData = "class "+ className +"(tornado.web.RequestHandler):\n"
			conf = open(self.NAME,'w')
			conf.write(controllerClassData)
			conf.close()
			with open(self.NAME, "a") as controllerFile:
				for methodData in controllerData:
					controllerFile.write(methodData)

			print(className +' Controller created.')
			
			routeName = className
			
			'''Add route for the created controller in routes/routes.py'''
			
			routeContent = '[\n\t\t(\n\t\t\tr"/'+ routeName +'",\n\t\t\t'+ controllerName +'.' + routeName +'\n\t\t),\n'
			
			routesDirectory = CURRENT_DIR+'/routes/'
			
			with open(routesDirectory +"routes.py","r") as routesFile:
				routesFileContent = routesFile.read()
			if(routeName in routesFileContent):
				print ('Sorry, this route already exists.')
			else:
				routesFileContent = routesFileContent.replace("[",routeContent)
				with open(routesDirectory+"routes.py", "w") as routesFile:
					routesFile.write(routesFileContent)
		else:
			print ('Sorry, this controller already exists. Try renaming your Controller.')
