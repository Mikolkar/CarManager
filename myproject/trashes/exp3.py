import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pierwsze okno")
        self.setGeometry(100, 100, 400, 200)

        self.button = QPushButton("Otwórz drugie okno", self)
        self.button.clicked.connect(self.open_second_window)

        self.second_window = None  # Inicjalizacja referencji do drugiego okna

    def open_second_window(self):
        self.second_window = SecondWindow()
        self.second_window.show()

    def closeEvent(self, event):
        if self.second_window:
            self.second_window.close()

class SecondWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Drugie okno")
        self.setGeometry(200, 200, 400, 200)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
