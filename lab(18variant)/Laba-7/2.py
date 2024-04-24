# Вариант 3

from abc import ABC, abstractmethod

class Person(ABC):
    def constructor(self, name, age):
        self.name = name
        self.age = age
    
    @abstractmethod
    def get_details(self):
        pass

class OwnerOfCar(Person):
    def constructor(self, name, age, car):
        super().constructor(name, age)
        self.car = car
    
    def get_details(self):
        return f"Владелец: {self.name}, Возраст: {self.age}, Машина: {self.car.model}"

class Car:
    def constructor(self, model, owner=None):
        self.model = model
        self.owner = owner
    
    def assign_owner(self, owner):
        self.owner = owner

class Parking:
    def constructor(self):
        self.cars = []
    
    def add_car(self, car):
        self.cars.append(car)
    
    def remove_car(self, car):
        if car in self.cars:
            self.cars.remove(car)
        else:
            print("Машины нету на парковке.")


parking = Parking()

while True:
    print("\n1.Добавить машину на парковку")
    print("2. Убрать машину с парковки")
    print("3. Вывести информацию о машинах на парковке")
    print("4. Выход")

    choice = input("Введите свой выбор: ")

    if choice == '1':
        model = input("Введите модель машины: ")
        owner_name = input("Введите имя владельца: ")
        owner_age = input("Введите возраст владельца ")
        owner = OwnerOfCar(owner_name, owner_age, None)
        car = Car(model, owner)
        owner.car = car
        parking.add_car(car)
        print("Машина добавлена на парковку.")

    elif choice == '2':
        model = input("Введите модель машины  для удаления: ")
        for car in parking.cars:
            if car.model == model:
                parking.remove_car(car)
                print(f"Машина '{model}' удалена из парковки.")
                break
        else:
            print(f"Машина '{model}' не найдена на парковке.")

    elif choice == '3':
        print("\nПодробная информация об машинах на парковке:")
        for car in parking.cars:
            print(car.owner.get_details())

    elif choice == '4':
        print("Выход из меню.")
        break

    else:
        print("Неверный вариант.Повторите свой выбор")
