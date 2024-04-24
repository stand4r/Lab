# Вариант 3

from abc import ABC, abstractmethod

class IMovable(ABC):
    @abstractmethod
    def move_up(self):
        pass
    
    @abstractmethod
    def move_down(self):
        pass
    
    @abstractmethod
    def move_right(self):
        pass
    
    @abstractmethod
    def move_left(self):
        pass

class Cursor(IMovable):
    def constructor(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
    
    def move_up(self):
        self.position_y += 1
    
    def move_down(self):
        self.position_y -= 1
    
    def move_right(self):
        self.position_x += 1
    
    def move_left(self):
        self.position_x -= 1
    
    @property
    def position(self):
        return (self.position_x, self.position_y)

class Box(IMovable):
    def constructor(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
    
    def move_up(self):
        self.position_y += 1
    
    def move_down(self):
        self.position_y -= 1
    
    def move_right(self):
        self.position_x += 1
    
    def move_left(self):
        self.position_x -= 1
    
    @property
    def position(self):
        return (self.position_x, self.position_y)


cursor = Cursor(0, 0)
box = Box(3, 3)

print("Начальное положение курсора:", cursor.position)
print("Начальное положение коробки:", box.position)

while True:
    print("\n1. Переместить курсор вверх")
    print("2. Переместить курсор вниз")
    print("3. Переместить курсор вправо")
    print("4. Переместить курсор влево")
    print("5. Выход")

    choice = input("Введите свой выбор: ")

    if choice == '1':
        cursor.move_up()
        print("Переместить курсор вверх.")

    elif choice == '2':
        cursor.move_down()
        print("Переместить курсор вниз.")

    elif choice == '3':
        cursor.move_right()
        print("Переместить курсор вправо.")

    elif choice == '4':
        cursor.move_left()
        print("Переместить курсор влево.")

    elif choice == '5':
        print("Выход из программы.")
        break

    else:
        print("Неверной выбор. Повторите выбор")

    print("Текущее положение курсора:", cursor.position)
    print("Текущее положение коробки:", box.position)
