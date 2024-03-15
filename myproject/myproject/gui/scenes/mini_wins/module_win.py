from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QWidget
from PyQt6.QtWidgets import (
    QApplication,
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


class Module(QDialog):
    def __init__(self, pos_x, pos_y, size):
        super().__init__()

        # setting position of mini window
        self.set_pos_of_win(pos_x, pos_y, 360, 500, size)

        # setting style of window
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 10)

    def set_style_of_win(self):
        pixmap = QPixmap("myproject/graphic/white_square.png")
        icon = QIcon(pixmap)
        self.setWindowTitle(" ")
        self.setWindowIcon(icon)

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
        self.setGeometry(position_x, position_y, win_width, win_height)

        with open("myproject/gui/styles.css", "r") as css_file:
            self.setStyleSheet(css_file.read())

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
