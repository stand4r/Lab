class Position:
    def __init__(self, latitude, longitude, altitude):
        self.set_latitude(latitude)
        self.set_longitude(longitude)
        self.set_altitude(altitude)

    def set_latitude(self, value):
        if not -90 <= value <= 90:
            raise ValueError("Широта должна быть в пределах от -90 до 90 градусов.")
        self.__latitude = value

    def set_longitude(self, value):
        if not -180 <= value <= 180:
            raise ValueError("Долгота должна быть в пределах от -180 до 180 градусов.")
        self.__longitude = value

    def set_altitude(self, value):
        if not -10000 <= value <= 10000:
            raise ValueError("Высота должна быть в пределах от -10000 до 10000 метров.")
        self.__altitude = value

    @staticmethod
    def convert_to_dms(degree):
        d = int(degree)
        m = int((degree - d) * 60)
        s = (degree - d - m / 60) * 3600
        return d, m, s

    def get_coordinates(self):
        return self.__latitude, self.__longitude, self.__altitude

    def get_coordinates_dms(self):
        lat_d, lat_m, lat_s = self.convert_to_dms(abs(self.__latitude))
        lon_d, lon_m, lon_s = self.convert_to_dms(abs(self.__longitude))
        
        lat_dir = "N" if self.__latitude >= 0 else "S"
        lon_dir = "E" if self.__longitude >= 0 else "W"
        
        return f"{lat_d}°{lat_m}'{lat_s}\"{lat_dir}, {lon_d}°{lon_m}'{lon_s}\"{lon_dir}"


# Демонстрация использования класса
try:
    position1 = Position(55.755831, 37.617673, 200)
    print(position1.get_coordinates())
    print(position1.get_coordinates_dms())

    position2 = Position(-45.12345, 170.12345, -500)
    print(position2.get_coordinates())
    print(position2.get_coordinates_dms())

    # Пример, который вызовет ошибку из-за некорректных данных
    position3 = Position(100, -200, 12000)
except ValueError as e:
    print(e)
