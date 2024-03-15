import os
import sys

from PyQt6 import QtGui
from myproject.gui.scenes.mini_wins.dialog_win import MiniWindow
from PyQt6.QtWidgets import (
    QWidget,
    QApplication,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QVBoxLayout,
    QLabel,
    QPushButton,
    QMenu,
)
from PyQt6.QtCore import QDate, Qt, QEvent
from PyQt6.QtGui import QIcon, QPixmap
from myproject.gui.scenes.module import file


class Scene1(QWidget):
    def __init__(self):
        super().__init__()

        # self.showNormal()

        self.lst = self.Get_months()

        self.mini_win = None

        self.CreatingLayouts()
        self.setWindowTitle("Car manager")
        self.main_date = QDate.currentDate()
        self.Calendar_Layout.setSpacing(2)

        self.Calendar_lay(self.main_date)
        self.Main_Layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.Main_Layout)

        self.left_button.clicked.connect(lambda: self.Move_month(0))
        self.right_button.clicked.connect(lambda: self.Move_month(1))

        # Load style from css file
        with open("myproject/gui/styles.css", "r") as css_file:
            self.setStyleSheet(css_file.read())

    def clicked_day(self, event):
        curs_pos = QtGui.QCursor().pos()
        win_size = self.size()
        self.mini_win = MiniWindow(curs_pos.x(), curs_pos.y(), self.size().height())
        # print(curs_pos.x(), curs_pos.y())
        # print(self.size().height())
        # print(self.maximumHeight())
        self.mini_win.show()

    def Adding_days_of_week(self):
        for i in range(len(self.weeks)):
            frame = QFrame(self)
            label = QLabel(self.weeks[i], frame)
            label.setFixedHeight(20)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            self.Calendar_Layout.addWidget(label, 1, i)

    def Get_months(self):
        lst = []
        with open("myproject/gui/scenes/txt_files/months_2.txt", "r", encoding="utf-8") as plik:
            months = plik.read().split()
        for i in range(len(months)):
            lst.append(months[i].rstrip())
        return lst

    def Move_month(self, move):
        if move == 1:
            self.main_date = self.main_date.addMonths(1)
        else:
            self.main_date = self.main_date.addMonths(-1)
        self.Calendar_lay(self.main_date)

    def Calendar_lay(self, arg_date):
        self.weeks = [
            "Poniedziałek",
            "Wtorek",
            "Środa",
            "Czwartek",
            "Piątek",
            "Sobota",
            "Niedziela",
        ]
        current_date = arg_date
        first_day = QDate(current_date.year(), current_date.month(), 1)
        day_of_week = first_day.dayOfWeek()

        Mon_frame = QFrame(self)
        name = self.lst[arg_date.month() - 1]
        Mon_label = QLabel(
            self.weeks[current_date.dayOfWeek() - 1].lower()
            + ", "
            + str(current_date.day())
            + " "
            + name
            + " "
            + str(current_date.year()),
            Mon_frame,
        )
        Mon_label.setStyleSheet("font-size: 28px;")
        Mon_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        Mon_label.setFixedHeight(58)

        self.Calendar_Layout.addWidget(Mon_label, 0, 0, 1, 7)
        self.Adding_days_of_week()

        # Postioning arragement of days
        week = day_of_week
        date = first_day
        while week != 1:
            date = date.addDays(-1)
            week = date.dayOfWeek()

        # Displaying days
        for row in range(2, 8):
            for column in range(7):
                day = date.day()
                size_md = 27
                # Creating frames
                frame = QFrame(self)
                frame.setStyleSheet("background-color: white;")
                marked_day_frame = QFrame(frame)
                marked_day_frame.setFixedSize(size_md, size_md)
                # And labels
                marked_day_label = QLabel(f"{day}", marked_day_frame)
                marked_day_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
                marked_day_label.setFixedSize(size_md, size_md)

                tasks_label = QLabel()
                tasks_label.setObjectName("pickDay")
                tasks_label.setFixedHeight(18)
                tasks_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

                # Setting layout in frame
                day_layout = QVBoxLayout(frame)
                day_layout.setSpacing(0)
                day_layout.setContentsMargins(2, 2, 2, 2)
                day_layout.addWidget(marked_day_frame)

                if date.month() != current_date.month():
                    frame.setStyleSheet(
                        "background-color: #EBEBEB;" "color: lightgrey;"
                    )
                else:
                    frame.mousePressEvent = self.clicked_day

                    if current_date.day() == date.day():
                        marked_day_label.setStyleSheet(
                            "background-color: aqua;" "border-radius: 13.4px"
                        )
                day_layout.addStretch()
                self.Calendar_Layout.addWidget(frame, row, column)
                date = date.addDays(1)

    def CreatingLayouts(self):
        self.Main_Layout = QVBoxLayout()
        self.Bar = QHBoxLayout()
        self.Calendar_Layout = QGridLayout()
        self.Bottom_Box = QHBoxLayout()
        self.Bottom_Box.setContentsMargins(0, 10, 0, 20)
        self.Setting_Bar()

        self.Main_Layout.addLayout(self.Bar)
        self.Bottom_Box.addWidget(self.left_button)
        self.Bottom_Box.addLayout(self.Calendar_Layout)
        self.Bottom_Box.addWidget(self.right_button)
        self.Main_Layout.addLayout(self.Bottom_Box)

        self.Bottom_Box.setSpacing(1)

    def Setting_Bar(self):
        self.CreatingButtons()
        self.Bar.addWidget(self.OC_button)
        self.Bar.addWidget(self.review_button)
        self.Bar.addWidget(self.car_button)

    def CreatingButtons(self):
        # Creating buttons
        self.OC_button = QPushButton("OC", self)
        self.review_button = QPushButton("Przegląd", self)
        self.car_button = QPushButton("Samochody", self)

        # Left and right button
        self.left_button = QPushButton("", self)
        self.right_button = QPushButton("", self)

        # Menu buttons
        menu_oc = QMenu(self)
        self.sub_button_1 = menu_oc.addAction("Kazimierz")
        self.sub_button_2 = menu_oc.addAction("Eliasz")
        self.sub_button_3 = menu_oc.addAction("Wszystko")

        menu_review = QMenu(self)
        self.sub_button_r1 = menu_review.addAction("Kazimierz")
        self.sub_button_r2 = menu_review.addAction("Eliasz")
        self.sub_button_r3 = menu_review.addAction("Wszystko")
        self.OC_button.setMenu(menu_oc)
        self.review_button.setMenu(menu_review)

        # Pixmap
        pixmap = QPixmap(f"{file}\left_arrow_1.png")
        pixmap1 = QPixmap(f"{file}\left_arrow_1_.png")

        icon = QIcon(pixmap)
        icon1 = QIcon(pixmap1)

        self.left_button.setIcon(icon)
        self.right_button.setIcon(icon1)

        self.left_button.setObjectName("NextButton")
        self.right_button.setObjectName("NextButton")

        # Setting paramiters
        self.left_button.setFixedSize(40, 500)
        self.right_button.setFixedSize(40, 500)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = Scene1()
    main_window.show()
    sys.exit(app.exec())
