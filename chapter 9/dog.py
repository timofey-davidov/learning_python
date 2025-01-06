class Dog:
	"""Простая модель собаки"""
	def __init__(self, name, age):
		"""Инициализируем атрибуты name, age"""
		self.name = name
		self.age = age

	def bark(self):
		print("Wof-Wof")

	def sit(self):
		"""Имитирует, как собака садится по команде"""
		print(f"{self.name} is now sitting")

	def roll_over(self):
		"""Имитирует, как собака перекатываентся по команде"""
		print(f"{self.name} rolled over!")

my_dog = Dog('Willie', 6)
your_dog = Dog('Lucy', 3)
my_dog.sit()
my_dog.roll_over()
your_dog.sit()
your_dog.roll_over()