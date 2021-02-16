from metapjc import MetaPj
import sys
import os

class PJpython(metaclass=MetaPj):
	def __init__(self):
		pass

	@staticmethod
	def createproject(name):
		os.mkdir(name)
		directory =  name+"/test.py"
		with open(directory, "w") as file:
			file.write("\nprint(\"hello world\") ")

