class Car:
    """Простая моедль автомобиля"""
    def __init__(self, make, model, year):
        """Инициализирует атрибуты описания автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Возвращает отформатированное описание"""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Выводит данные о пробеге машины в милях"""
        print(f"This car has {self.odometer_reading} miles on it")

    def update_odometer(self, mileage):
        """Устанавливает заданное значение на одометре
        При попытке обратной прокрутки изменение отколняется
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an oddometer!")
        self.odometer_reading = mileage

    def increment_odometer(self, miles):
        """Увеличивает показания одометра с заданным приращением"""
        self.odometer_reading += miles

class ElectricCar(Car):
    """Представляет аспекты машины, специфические для электромобилей."""
    def __init__(self, make, model, year):
        """
        Инициализирует атрибуты класса-родителя
        Затем инициализирует атрибуты, специфические для электромобиля."""
        super().__init__(make, model, year)
        self.battery_size = 40

    def describe_battery(self):
        """Выводит информацию о мощности аккумулятора."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def fill_gas_tank(self):
        """У электромобиля нет бензобака."""
        print("This car doesn't have a gas tank")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
my_leaf.describe_battery()
my_leaf.fill_gas_tank()

class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def calculate_coefficients(self, other):
        k = (other.y - self.y) / (other.x - self.x)
        b = (self.y * other.x - self.x * other.y) / (other.x - self.x)
        return f"Коэффициент k = {k}, коэффициент b = {b}"

a = Point(-1, 3)
b = Point(0, 9)
print(a.calculate_coefficients(b))

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(n):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator

@repeat(3)
def power(x, y=2):
    return x ** y

print(power(2))
print(power(3,3))

import csv

# Данные, которые мы хотим записать в CSV
data = [['Name', 'Age', 'City'],
        ['Наташа', 30, 'New York'],
        ['Никита', 25, 'Los Angeles'],
        ['Александр', 35, 'Chicago']]

with open('output.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    # Записываем все строки в CSV
    writer.writerows(data)