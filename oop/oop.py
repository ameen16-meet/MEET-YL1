class animal:
	def __init__(self,name,age,color,size,):
		self.name=name
		self.age=age
		self.color=color
		self.size=size
		
	def print_all(self):
		print(self.name, self.age, self.color, self.size)
	def eat(self,food): 
		print("the animal" , self.name , "is eating" , food)
	def sleep(self, time,dreamtopic):
		
		print("the animal", self.name, "is sleeping for", time, " hours and is dreaming about", dreamtopic)
	
dog = animal("Sadek",22,"yellow","tiny")
lion= animal("fufu",5,"black", "huge")

#dog.print_all()
#lion.print_all()
lion.eat("you")
dog.sleep(2, "pizza")
