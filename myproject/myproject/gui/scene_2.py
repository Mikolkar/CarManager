import os
import sys

from PyQt6 import QtGui 
from PyQt6.QtWidgets import (
    QWidget,
    QApplication,
    QFrame,
    QGridLayout,
    QHBoxLayout,
    QVBoxLayout,
    QTextEdit,
    QLineEdit,
    QLabel,
    QPushButton,
    QMenu,
    QScrollArea,

)
from PyQt6.QtCore import QDate, Qt, QEvent
from PyQt6.QtGui import QIcon, QPixmap, QColor, QImage
from module import file
class Scene2(QWidget):
    def __init__(self):
        super().__init__()
        self.x_ind = 0
        self.y_ind = 0

        layout = QVBoxLayout(self)

        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)

        content = QWidget()
        self.layout_scroll = QGridLayout(content)

        self.setting_adding_button(self.x_ind, self.y_ind)
        self.label.mousePressEvent = self.mousePressEvent

        scroll_area.setWidget(content)

        self.back_button = QPushButton("cofnij")
        self.back_button.setFixedWidth(74)
        self.back_button.setStyleSheet("font-size: 18px;")
        layout.addWidget(self.back_button)
        layout.addWidget(scroll_area)
        # layout.addStretch()

        self.setLayout(layout)
        
    def mousePressEvent(self, event):
        # print(self.x_ind, self.y_ind)
        self.layout_scroll.removeWidget(self.label)
        label_2 = QLabel("""dupa
                         fdsf
                         fsdfsdf
                         dfsdf
                         dfsdf""")
        size = 290
        label_2.setFixedSize(size, size)
        self.layout_scroll.addWidget(label_2, self.y_ind, self.x_ind)

        self.x_ind += 1
        if self.x_ind == 5:
            self.x_ind =  0
            self.y_ind += 1

        
        self.setting_adding_button(self.x_ind, self.y_ind)

    def setting_adding_button(self, x_ind, y_ind):
        size = 290
        self.label = QLabel()

        pixmap = QPixmap(f"{file}\img_icon.png")
        scaled_pixmap = pixmap.scaled(size,size)

        self.label.setPixmap(scaled_pixmap)
        self.label.setStyleSheet("background-color: red;")
        self.label.setFixedSize(size,size)
        

        self.layout_scroll.addWidget(self.label, y_ind , x_ind)

    def adding_new_car(self):
        return
    
    def deleting_car(self):
        return
        

        
        