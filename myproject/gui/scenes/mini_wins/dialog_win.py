import os
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import (
    QDialog,
    QPushButton,
    QDialogButtonBox,
    QVBoxLayout,
    QTextEdit,
    QLineEdit,
    QFrame,
    QHBoxLayout,
    QMenu,
)
from PyQt6.QtGui import QIcon, QPixmap


class MiniWindow(QDialog):
    def __init__(self, pos_x, pos_y, size):
        super().__init__()
        # setting position of mini window
        self.set_pos_of_win(pos_x, pos_y, 360, 500, size)

        # setting style of window
        pixmap = QPixmap("myproject/graphic/white_square.png")
        icon = QIcon(pixmap)
        self.setWindowTitle(" ")
        self.setWindowIcon(icon)

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 10)

        mainTaskLine = QLineEdit()
        mainTaskLine.setPlaceholderText("Opis")
        mainTaskLine.setGeometry(0, 0, 500, 80)
        layout.addWidget(mainTaskLine)

        self.setting_buttons()

        layout.addWidget(self.butt_frame)

        self.setting_menu_button(layout)
        review = QTextEdit()
        layout.addWidget(review)

        self.setting_save_cancel_buttons(layout)

        self.setLayout(layout)

    def set_pos_of_win(self, pos_x, pos_y, win_width, win_height, screen_height):
        space_x = 40
        space_y = 40
        position_x = pos_x - int(win_width) - space_x
        position_y = pos_y - int(win_height * 0.2)

        if position_x < 0:
            position_x = pos_x + space_x
        if position_y + win_height > screen_height:
            diff = position_y + win_height - screen_height
            position_y -= diff
        if position_y < 40:
            position_y += 70
        # print("pozycje:", position_x, position_y)
        self.setGeometry(position_x, position_y, win_width, win_height)

        with open("myproject/gui/styles.css", "r") as css_file:
            self.setStyleSheet(css_file.read())

    def setting_buttons(self):
        self.butt_frame = QFrame()
        butt_layout = QHBoxLayout(self.butt_frame)
        lst = ["red", "blue", "green", "orange"]
        for i in range(4):
            color_button = QPushButton()
            butt_size = 50
            color_button.setFixedSize(butt_size, butt_size)
            color_button.setStyleSheet(f"background-color:{lst[i]};")
            butt_layout.addWidget(color_button)

    def setting_save_cancel_buttons(self, layout):
        save_butt = QPushButton("zapisz")
        cancel_butt = QPushButton("anuluj")

        button_box = QDialogButtonBox()
        button_box.addButton(save_butt, QDialogButtonBox.ButtonRole.AcceptRole)
        button_box.addButton(cancel_butt, QDialogButtonBox.ButtonRole.RejectRole)

        button_box.accepted.connect(self.action)
        button_box.rejected.connect(self.action)

        layout.addWidget(button_box)
        layout.setAlignment(button_box, Qt.AlignmentFlag.AlignHCenter)

    def action(self):
        return

    def setting_menu_button(self, layout):

        ##########################################
        # There will be reading data from database
        menu_button = QPushButton("Samochody")
        lst = ["Audi", "Mercedes", "Toyota", "BMW"]
        menu = QMenu(self)
        for i in range(len(lst)):
            menu.addAction(lst[i])

        menu_button.setMenu(menu)
        layout.addWidget(menu_button)
