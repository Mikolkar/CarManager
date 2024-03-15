import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QDialog, QDialogButtonBox, QStackedWidget

class MiniWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Mini-okno")
        self.setGeometry(200, 200, 300, 150)

        layout = QVBoxLayout(self)

        button1 = QPushButton("Przycisk 1", self)
        button2 = QPushButton("Przycisk 2", self)

        button_box = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok | QDialogButtonBox.StandardButton.Cancel)
        button_box.accepted.connect(self.accept)
        button_box.rejected.connect(self.reject)

        layout.addWidget(button1)
        layout.addWidget(button2)
        layout.addWidget(button_box)
        self.setLayout(layout)

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Przykład PyQt6")
        self.setGeometry(100, 100, 400, 200)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.stacked_widget = QStackedWidget(self.central_widget)

        self.main_widget = QWidget()
        self.stacked_widget.addWidget(self.main_widget)

        self.button = QPushButton("Otwórz mini-okno", self.main_widget)
        self.button.clicked.connect(self.open_mini_window)

    def open_mini_window(self):
        self.mini_win = MiniWindow(parent=self)
        self.mini_win.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())
