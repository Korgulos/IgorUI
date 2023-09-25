import random
import sys
from Colors import colors
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QSizePolicy, QLabel
from PySide6.QtCore import Qt


def button_clicked(a, r):
    if r == a:
        print(f"Button is {colors[a-1].color_name} and is equal to {colors[r-1].color_name}")
        # Closing application function from docks.
        QApplication.instance().quit()

    else:
        print(f"Button is {colors[a-1].color_name} and is not equal to {colors[r-1].color_name}")


class RocWidget(QWidget):

    def __init__(self, rando):
        super().__init__()
        self.rando = rando

        self.setWindowTitle("RockWidget")

        v = QVBoxLayout()
        h = QHBoxLayout()
        hl = QHBoxLayout()

        for color in colors:
            button = QPushButton(color.color_name)
            button.setStyleSheet(f"{color.color_color}; font: bold 34px; border-color: rgb(50, 50, 50);"
                                 f" border: 1px solid;")
            if color.color_name == "Crna" or color.color_name == "Plava":
                button.setStyleSheet(f"{color.color_color}; "
                                     f"font: bold 34px; border-color: rgb(200, 200, 200);"
                                     f" border: 1px solid; color: rgb(200, 200, 200);")
            button.pressed.connect(
                lambda val=color.color_id: button_clicked(self.button_pressed(val), self.rando)
            )
            button.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
            h.addWidget(button)

        self.label = QLabel(f"{colors[self.rando-1].color_name}")
        self.label.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.label.setStyleSheet("font: bold 55px;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        hl.addWidget(self.label)
        v.addLayout(hl, 1)
        v.addLayout(h, 3)
        self.setLayout(v)

    def button_pressed(self, n):
        self.label.setText(f"Boja {colors[n-1].color_name} nije boja {colors[self.rando-1].color_name}")
        return n


if __name__ == "__main__":

    rand_int = random.randint(1, 8)
    app = QApplication(sys.argv)
    window = RocWidget(rand_int)
    window.showMaximized()
    window.setWindowFlag(Qt.FramelessWindowHint, True)
    window.setWindowFlag(Qt.WindowStaysOnTopHint, True)
    window.show()
    app.exec()
