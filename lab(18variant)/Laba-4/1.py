
# Вариант 3
class Coordinates:
    def __init__(self, latitude, longitude, height):
        self.latitude = self.validate_coord(latitude, -90, 90)
        self.longitude = self.validate_coord(longitude, -180, 180)
        self.height = self.validate_coord(height, -10000, 10000)

    def validate_coord(self, coord, min_val, max_val):
        if min_val <= coord <= max_val:
            return coord
     

    def change_position(self, latitude, longitude, height):
        self.latitude = self.validate_coord(latitude, -90, 90)
        self.longitude = self.validate_coord(longitude, -180, 180)
        self.height = self.validate_coord(height, -10000, 10000)

    @staticmethod
    def decimal_to_degrees(decimal_degrees):
        degrees = int(decimal_degrees)
        minutes = int((decimal_degrees - degrees) * 60)
        seconds = ((decimal_degrees - degrees) * 60 - minutes) * 60
        return degrees, minutes, seconds

coordinates1 = Coordinates(55.755831, 37.617673, 0)
print("Координаты объекта 1 в градусах:", coordinates1.latitude, coordinates1.longitude, coordinates1.height)

degrees, minutes, seconds = Coordinates.decimal_to_degrees(coordinates1.latitude)
print("Широта объекта 1 в градусах, минутах и секундах:", degrees, minutes, seconds)

coordinates1.change_position(55.755831, 37.617673, 100)
print("Новые координаты объекта 1:", coordinates1.latitude, coordinates1.longitude, coordinates1.height)
