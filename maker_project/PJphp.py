from metapjc import MetaPj
import sys
import os

class PJphp(metaclass=MetaPj):
	
	def __init__(self):
		pass 

	@staticmethod
	def createproject(name):
		path = "../"+name
		os.mkdir(path)
		directory =  path+"/index.php"

		with open(directory, "w") as file:
			file.write("<?php\necho \"hello world\"; ")
