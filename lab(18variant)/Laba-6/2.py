# Вариант 3 

class Plane:
    def __init__(self, destination, airline_code, flight_number, departure_time):
        self.__destination = destination
        self.__airline_code = airline_code
        self.__flight_number = flight_number
        self.__departure_time = departure_time

    @property
    def destination(self):
        return self.__destination

    @property
    def airline_code(self):
        return self.__airline_code

    @property
    def flight_number(self):
        return self.__flight_number

    @property
    def departure_time(self):
        return self.__departure_time


class Airport:
    def __init__(self):
        self.__planes = []

    def add_plane(self, plane):
        self.__planes.append(plane)

    def get_by_fli_num(self, flight_number):
        for plane in self.__planes:
            if plane.flight_number == flight_number:
                return plane
        return None

    def get_by_hour(self, input_time):
        planes_in_hour = []
        for plane in self.__planes:
            if input_time <= plane.departure_time <= input_time + 60:
                planes_in_hour.append(plane)
        return sorted(planes_in_hour, key=lambda x: x.departure_time)

    def get_by_dest(self, destination):
        planes_to_destination = []
        for plane in self.__planes:
            if plane.destination == destination:
                planes_to_destination.append(plane)
        return sorted(planes_to_destination, key=lambda x: x.departure_time)


plane1 = Plane("Москва", "MSK", 101, 4)
plane2 = Plane("Питер", "PT", 202, 1)
plane3 = Plane("Самара", "SM", 303, 16)

airport = Airport()
airport.add_plane(plane1)
airport.add_plane(plane2)
airport.add_plane(plane3)


while 1:
    print("\nКомманды:\n1)По номеру\n2)По пункту назначения\n3)По времени")
    n = int(input("> "))
    if n == 1:
        flight_number = int(input("Номер рейса: "))
        plane_info = airport.get_by_fli_num(flight_number)
        if plane_info:
            print("Информация о самолете с номером рейса", flight_number)
            print("Пункт назначения:", plane_info.destination)
            print("Код авиакомпании:", plane_info.airline_code)
            print("Время отправления:", plane_info.departure_time)
        else:
            print("Самолет с номером рейса", flight_number, "не найден")
    elif n == 2:
        destination = input("Пункт назначения: ")
        print("\nСамолеты, отправляющиеся в", destination)
        planes_to_destination = airport.get_by_dest(destination)
        for plane in planes_to_destination:
            print("Код авиакомпании:", plane.airline_code)
            print("Время отправления:", plane.departure_time)
    elif n == 3:
        input_time = int(input("Время: "))
        print("\nСамолеты, отправляющиеся в течение часа после", input_time)
        planes_in_hour = airport.get_by_hour(input_time)
        for plane in planes_in_hour:
            print("Пункт назначения:", plane.destination)
            print("Код авиакомпании:", plane.airline_code)
            print("Время отправления:", plane.departure_time)