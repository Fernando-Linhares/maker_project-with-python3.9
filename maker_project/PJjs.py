from metapjc import MetaPj
import sys
import os

class PJjs(metaclass=MetaPj):
	
	def __init__(self):
		pass
	@staticmethod
	def createproject(name):
		os.mkdir(name)
		directory =  name+"/test.html"
		with open(directory, "w") as file:
			file.write("<scritp>\ndocument.write(\"hello world\")</scritp> ")
