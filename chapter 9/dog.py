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

# my_dog = Dog('Willie', 6)
# your_dog = Dog('Lucy', 3)
# my_dog.sit()
# my_dog.roll_over()
# your_dog.sit()
# your_dog.roll_over()

# class Vector:
# 	def __init__(self, *args):
# 		self.values = [i for i in args if isinstance(i, int)]
# 		self.values.sort()
# 	def __str__(self):
# 		return f'Вектор({",".join(map(str, self.values))})' if len(self.values) > 0 else 'Пустой вектор'
# 	def __add__(self, item):
# 		if isinstance(item, int):
# 			return Vector(*[i + item for i in self.values])
# 		elif isinstance(item, Vector):
# 			if len(item.values) != len(self.values):
# 				return f"Сложение векторов разной длины недопустимо"
# 			else:
# 				return Vector(*list(map(lambda x,y: x+y, self.values, item.values)))
# 		else:
# 			print( f"Вектор нельзя сложить с {item}")
# 	def __mul__(self, item):
# 		if isinstance(item, int):
# 			return Vector(*[i * item for i in self.values])
# 		elif isinstance(item, Vector):
# 			if len(item.values) != len(self.values):
# 				return f"Умножение векторов разной длины недопустимо"
# 			else:
# 				return Vector(*list(map(lambda x,y: x*y, self.values, item.values)))
# 		else:
# 			print( f"Вектор нельзя умножать с {item}")
#
#
# class Book:
# 	def __init__(self, title, pages):
# 		self.title = title
# 		self.pages = pages
#
#
# class Library:
# 	def __init__(self):
# 		self.books = []
#
# 	def add_book(self, book):
# 		self.books.extend(book.pages)
#
# 	def __iter__(self):
# 		return LibraryIterator(self)  # тут определите, что будете передавать итератору
#
#
# class LibraryIterator:
# 	def __init__(self, obj):
# 		self.pages = obj.books
# 		self.index = 0
# 	def __iter__(self):
# 		return self
#
# 	def __next__(self):
# 		if self.index < len(self.pages):
# 			result = self.pages[self.index]
# 			self.index += 1
# 			return result
# 		else:
# 			raise StopIteration
#
#
# # Пример использования
# book1 = Book("Book 1", ["Page 1", "Page 2", "Page 3", "Page 4"])
# book2 = Book("Book 2", ["Page A", "Page B", "Page C"])
# book3 = Book("Book 3", ["Chapter 1", "Chapter 2"])
#
# library = Library()
# library.add_book(book1)
# library.add_book(book2)
# library.add_book(book3)
#
# # Используем вложенный итератор для обхода страниц в библиотеке
# for page in library:
# 	print(page)
#
# s = 'qwerty123'
# print(s[4:7:-1])
# print("---")
# print(s[7:4:-1])
# print("---")
# print(s[::-2])
# print("---")
# print(s[-2::-2])
# print("---")
# print(s[2::-1])
# print("---")

# from functools import singledispatchmethod
# from datetime import date, datetime, timedelta
# class BirthInfo:
# 	@singledispatchmethod
# 	def __init__(self, birth_date):
# 		raise TypeError("Аргумент переданного типа не поддерживается")
#
# 	@__init__.register(date)
# 	def _from_date(self, birth_date):
# 		self.birth_date = birth_date
#
# 	@__init__.register(str)
# 	def _from_ISO(self, birth_date):
# 		try:
# 			self.birth_date = datetime.fromisoformat(birth_date).date()
# 		except:
# 			raise TypeError("Аргумент переданного типа не поддерживается")
#
# 	@__init__.register(list)
# 	@__init__.register(tuple)
# 	def _from_list_tuple(self, birth_date):
# 		if len(birth_date) != 3:
# 			raise TypeError("Аргумент переданного типа не поддерживается")
# 		else:
# 			try:
# 				self.birth_date = date(*birth_date)
# 			except:
# 				raise TypeError("Аргумент переданного типа не поддерживается")
#
#
# 	@property
# 	def age(self):
# 		today = date.today()
# 		age = today.year - self.birth_date.year
# 		if (today.month, today.day) < (self.birth_date.month, self.birth_date.day):
# 			age -= 1
# 		return age
# try:
# 	today = date.today()
# 	for day in range(10):
# 		birthday = (today + timedelta(days=day)).replace(year=2000)
# 		birthinfo = BirthInfo(birthday)
#
# except TypeError as e:
# 	print(e)

# class Color:
# 	def __init__(self, color):
# 		self.__hexcode = color
# 		self.r = int(color[:2], 16)
# 		self.g = int(color[2:4], 16)
# 		self.b = int(color[4:], 16)
#
# 	@property
# 	def hexcode(self):
# 		return self.__hexcode
#
# 	@hexcode.setter
# 	def hexcode(self, new_value):
# 		self.__init__(new_value)
#
#
# color = Color('0000FF')
#
# color.hexcode = 'A782E3'
# print(color.hexcode)
# print(color.r)
# print(color.g)
# print(color.b)

class Pet:
	pets_list = []
	def __init__(self, name):
		self.name = name
		self.pets_list.append(self)

	@classmethod
	def first_pet(cls):
		if len(cls.pets_list) > 0:
			return cls.pets_list[0]
		return None

	@classmethod
	def last_pet(cls):
		if len(cls.pets_list) > 0:
			return cls.pets_list[-1]
		return None

	@classmethod
	def num_of_pets(cls):
		return len(cls.pets_list)

pet1 = Pet('Ratchet')
pet2 = Pet('Clank')
pet3 = Pet('Rivet')

print(Pet.first_pet().name)
print(Pet.last_pet().name)
print(Pet.num_of_pets())