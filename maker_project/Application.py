from PJpython import PJpython
from PJphp import PJphp
from PJjs import PJjs

from time import sleep

class Application:
	@staticmethod
	def start():
		promote = Pro("Please what project language want you?\n(javascriptc - js), (php), (python)\n")
		promote.doquestion()
		promote.resolve()

class Pro:
	def __init__(self,question):
		self.question = question
		self.res = None

	def doquestion(self):
		self.res = input(self.question)

	def resolve(self):
		if "python" in self.res:
			print("start creating python project..")
			print("please wait..")
			name = input("write the name project\n")
			PJpython.createproject(name)
			sleep(1)
			print(f"project {self.res} create sucessfuly")

		elif "php" in self.res:
			print(f"start creating {self.res} project..")
			print("please wait..")
			name = input("write the name project")

			PJphp.createproject(name)

			sleep(1)
			print(f"project {self.res} create sucessfuly")

		elif "javascript" in self.res  or "js" in self.res:

			print(f"start creating {self.res} project..")
			print("please wait..")
			name = input("write the name project")

			PJjs.createproject(name)

			sleep(1)
			print(f"project {self.res} create sucessfuly")

		else:
			print(f"the project {self.res} is not valid\nplease select an project of list\n(javascript), (php), (python)")