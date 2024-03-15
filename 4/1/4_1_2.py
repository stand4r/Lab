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

# Демонстрационная программа:
if __name__ == "__main__":
    try:
        time1 = Time(23, 59, 30)
        print(time1)
        time1.add_seconds(45)  # Добавляем секунды, что приводит к изменению минут и часов
        print(time1)
        
        time2 = Time(12, 30, 0)
        print(time2)
        time2.add_hours(12)  # Добавляем часы
        print(time2)
        
        # Пример с недопустимым значением
        time3 = Time(-1, 66, 30)
    except ValueError as e:
        print(f"Ошибка: {e}")
