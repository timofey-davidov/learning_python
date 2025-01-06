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

my_car = Car('audi', "a4", 2024)
print(my_car.get_descriptive_name())
my_car.read_odometer()
my_car.update_odometer(23)
my_car.read_odometer()
my_car.update_odometer(10)
my_old_car = Car('subaru', 'outback', 2019)
print(my_old_car.get_descriptive_name())
my_old_car.update_odometer(23_500)
my_old_car.read_odometer()
my_old_car.increment_odometer(100)
my_old_car.read_odometer()