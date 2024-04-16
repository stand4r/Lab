class Time:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = 0
        self.__minutes = 0
        self.__seconds = 0
        self.set_time(hours, minutes, seconds)
    
    def set_hours(self, hours):
        if 0 <= hours < 24:
            self.__hours = hours
        else:
            raise ValueError("Недопустимое значение часов")

    def set_minutes(self, minutes):
        if 0 <= minutes < 60:
            self.__minutes = minutes
        else:
            raise ValueError("Недопустимое значение минут")
    
    def set_seconds(self, seconds):
        if 0 <= seconds < 60:
            self.__seconds = seconds
        else:
            raise ValueError("Недопустимое значение секунд")
    
    def set_time(self, hours, minutes, seconds):
        self.set_hours(hours)
        self.set_minutes(minutes)
        self.set_seconds(seconds)
    
    def __str__(self):
        """Возвращает время в формате HH:MM:SS"""
        return f"{self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}"
    
    def add_seconds(self, seconds):
        total_seconds = self.__seconds + seconds
        self.__seconds = total_seconds % 60
        self.add_minutes(total_seconds // 60)
    
    def add_minutes(self, minutes):
        total_minutes = self.__minutes + minutes
        self.__minutes = total_minutes % 60
        self.add_hours(total_minutes // 60)
    
    def add_hours(self, hours):
        self.__hours = (self.__hours + hours) % 24

    def print(self):
        print( f"{self.__hours:02d}:{self.__minutes:02d}:{self.__seconds:02d}")

# Демонстрационная программа:
if __name__ == "__main__":
    try:
        time_p = input("Введите время: ").split(":")
        time = Time(int(time_p[0]), int(time_p[1]), int(time_p[2]))
        time.add_seconds(350)
        print(time)
    except ValueError:
        print("Недопустимое значение")
