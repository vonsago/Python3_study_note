class Parent():
	def __init__(self,name,color):
		print("Parent constructor called")
		self.last_name = name
		self.eye_color = color
	def show_info(self):
		print("last_name - "+self.last_name)
		print("eye_color - "+self.eye_color)


class Child(Parent):
	def __init__(self,name,color,number_of_toys):
		print("Child constructor called")
		Parent.__init__(self,name,color)
		self.number_of_toys=number_of_toys

	def show_info(self):
		print("last_name-"+self.last_name)
		print("eye_color-"+self.eye_color)
		print("number_of_toys-"+str(self.number_of_toys))

billy_cyrus = Parent("Cyrus","blue")
#print(billy_cyrus.last_name)
billy_cyrus.show_info()
miley_cyrus = Child("Cyrus","green",5)
miley_cyrus.show_info()