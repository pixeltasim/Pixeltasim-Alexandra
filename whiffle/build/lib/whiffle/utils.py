## A standard exception to indicate a type error in a function call.
class IntTypeError(Exception):
	def __init__(self, desc):
		self.desc = desc
	
	def __str__(self):
		return self.desc

## A standard Descriptor class to simplify and encapsulate class attributes.
class Descriptor(object):
	def __init__(self, get_func, set_func):
		self.get_func = get_func
		self.set_func = set_func
		
	def __get__(self, instance, owner):
		return self.get_func(instance)
		
	def __set__(self, instance, value):
		return self.set_func(instance, value)


