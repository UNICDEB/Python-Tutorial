# Create a class named Person, with firstname and lastname properties, and a printname method:



class Person():

	# Constructor
	# def __init__(self, name):
	# 	self.name = name

	# To get name
	def getName(name):
		# name= input("Enter name - ")
		name ="Ram"	
		return name

	# To check if this person is an employee
	def isEmployee(self):
		return False


# Inherited or Subclass (Note Person in bracket)
class Employee(Person):

	# Here we return true
	def isEmployee(self):
		return True


# Driver code
emp = Person() # An Object of Person
print(emp.getName(), emp.isEmployee())

emp1 = Employee() # An Object of Employee
print(emp1.getName(), emp1.isEmployee())
