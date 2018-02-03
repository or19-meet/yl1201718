class Animal(object):
	def __init__(self,sound,name,age,favourite_colour):
		self.sound = sound
		self.name = name
		self.age = age
		self.favourite_colour = favourite_colour
	def eat(self,food):
		print("Yummy!" + self.name + "is eating" + food)
	def description(self):
			print(self.name + "is" + self.age +"years old and loves the colour"+self.favourite_colour)
j = Animal("woof", "jesus ", 4, "blue")
j.eat(" sushi")
	