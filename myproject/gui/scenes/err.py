import os
import sys

from PyQt6 import QtGui
from PyQt6.QtWidgets import (
    QWidget,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QVBoxLayout,
    QPushButton,
    QScrollArea,
)
from PyQt6.QtCore import QDate, Qt, QEvent
from PyQt6.QtGui import QIcon, QPixmap, QColor, QImage


class Scene2(QWidget):
    def __init__(self):
        super().__init__()
        self.x_ind = 0
        self.y_ind = 0

        self.list_ind = 0
        self.car_buttons = []

        layout = QVBoxLayout(self)
        top_bar = QHBoxLayout()

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        content = QWidget()
        scroll_area.setWidget(content)
        self.layout_scroll = QGridLayout(content)

        self.setting_adding_button(self.x_ind, self.y_ind)

        self.add_buttons()
        top_bar.addWidget(self.back_button)
        top_bar.addWidget(self.button)
        layout.addLayout(top_bar)
        layout.addWidget(scroll_area)
        top_bar.addStretch()

        self.setLayout(layout)
        self.setStyleSheet(open("myproject/gui/styles.css").read())

    def mousePressEvent(self, event):
        # self.layout_scroll.removeWidget(self.label)

        self.x_ind += 1
        if self.x_ind == 5:
            self.x_ind = 0
            self.y_ind += 1

        self.setting_adding_button(self.x_ind, self.y_ind)

    def setting_adding_button(self, x_ind, y_ind):
        size = 290
        car_button = QPushButton("")

        car_button.setIcon(QIcon("myproject/graphic/img_icon.png"))
        car_button.setStyleSheet("background-color: red;")
        car_button.setFixedSize(size, size)
        car_button.setIconSize(car_button.size())

        self.car_buttons.append(car_button)
        self.list_ind += 1
        self.layout_scroll.addWidget(self.car_buttons[self.list_ind - 1], y_ind, x_ind)

    def add_buttons(self):
        # back button
        self.back_button = QPushButton("wróć")
        self.back_button.setFixedWidth(74)
        self.back_button.setStyleSheet("font-size: 18px;")

        # add button
        self.button = QPushButton("")
        self.button.setFixedSize(50, 50)
        self.button.setIcon(QIcon("myproject/graphic/add_icon.png"))
        self.button.setIconSize(self.button.size())
        self.button.setObjectName("default_button")
        self.button.clicked.connect(self.mousePressEvent)
