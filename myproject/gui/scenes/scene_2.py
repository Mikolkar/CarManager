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

        # UI Element Sizes
        self.car_button_size = 290

        # Button References
        self.back_button = None
        self.add_button = None

        # Internal State
        self.current_grid_x = 0
        self.current_grid_y = 0
        self.car_buttons = []

        self.setup_ui()

    def setup_ui(self):
        # Layout Structure
        layout = QVBoxLayout(self)
        top_bar = QHBoxLayout()
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        content = QWidget()
        scroll_area.setWidget(content)
        self.layout_scroll = QGridLayout(content)

        # Top Bar Buttons
        self.create_top_bar_buttons()

        # Add Top Bar and Scroll Area to Main Layout
        top_bar.addWidget(self.back_button)
        top_bar.addWidget(self.add_button)
        layout.addLayout(top_bar)
        layout.addWidget(scroll_area)
        top_bar.addStretch()

        self.setLayout(layout)
        self.setStyleSheet(open("myproject/gui/styles.css").read())

    def create_top_bar_buttons(self):
        # Back Button
        self.back_button = QPushButton("Wróć")
        self.back_button.setFixedWidth(74)
        self.back_button.setStyleSheet("font-size: 18px;")

        # Add Button
        self.add_button = QPushButton("")
        self.add_button.setFixedSize(50, 50)
        self.add_button.setIcon(QIcon("myproject/graphic/add_icon.png"))
        self.add_button.setIconSize(self.add_button.size())
        self.add_button.setObjectName("default_button")
        self.add_button.clicked.connect(self.handle_add_button_click)

    def handle_add_button_click(self):
        # This function is triggered when the "add" button is clicked
        # Add logic for adding a new car button here
        self.add_car_button()

    def add_car_button(self):
        car_button = QPushButton("")
        car_button.setIcon(QIcon("myproject/graphic/img_icon.png"))
        car_button.setStyleSheet("background-color: red;")
        car_button.setFixedSize(self.car_button_size, self.car_button_size)
        car_button.setIconSize(car_button.size())

        self.car_buttons.append(car_button)
        self.layout_scroll.addWidget(
            car_button, self.current_grid_y, self.current_grid_x
        )

        # Update grid position for the next button
        self.current_grid_x += 1
        if self.current_grid_x == 5:
            self.current_grid_x = 0
            self.current_grid_y += 1

    # ... other methods like adding_new_car and deleting_car can be defined here

    def scaled_pixmap(self, size, path):
        pixmap = QPixmap(path)
        scaled_pixmap = pixmap.scaled(size, size)
        return scaled_pixmap

    def adding_new_car(self):
        return

    def deleting_car(self):
        return
