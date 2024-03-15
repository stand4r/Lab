from enum import Enum, auto
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton

class Property(Enum):
    """Перечисление для свойств кандидатов и фирм."""
    CONDITION_A = auto()
    CONDITION_B = auto()
    CONDITION_C = auto()
    # Добавьте оставшиеся свойства по аналогии

class Candidate:
    """Класс для представления кандидата."""
    def __init__(self, name, properties):
        self.name = name
        self.properties = properties  # список свойств из перечисления Property

class Firm:
    """Класс для представления фирмы."""
    def __init__(self, name, properties):
        self.name = name
        self.properties = properties  # список свойств из перечисления Property

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Работники и фирмы')
        self.setGeometry(100, 100, 800, 600)  # X, Y, Width, Height

        layout = QVBoxLayout()
        
        # Пример кнопки
        self.button = QPushButton('Рассчитать', self)
        layout.addWidget(self.button)
        
        self.setLayout(layout)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
