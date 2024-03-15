import os
import sys
from myproject.gui.scenes.scene_1 import Scene1
from myproject.gui.scenes.scene_2 import Scene2
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QStackedWidget,
)

file = os.path.abspath("../graphic")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(1530, 792)
        self.showNormal()

        self.stacked_wiget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_wiget)

        self.scene_1 = Scene1()
        self.scene_2 = Scene2()

        self.stacked_wiget.addWidget(self.scene_1)
        self.stacked_wiget.addWidget(self.scene_2)

        # if car_button is clicked
        self.scene_1.car_button.clicked.connect(self.switch_to_scene_2)

        # if back_button is cliked
        self.scene_2.back_button.clicked.connect(self.switch_to_scene_1)

    def switch_to_scene_1(self):
        self.stacked_wiget.setCurrentWidget(self.scene_1)

    def switch_to_scene_2(self):
        file = os.path.abspath("../graphic")
        print(file)
        self.stacked_wiget.setCurrentWidget(self.scene_2)

    def closeEvent(self, event):
        if self.scene_1.mini_win:
            self.scene_1.mini_win.close()


def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())


main()
