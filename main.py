import time
import random
import keyboard
import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication
from pyQt6UI import RocWidget
from datetime import datetime, timedelta

while True:
    if keyboard.is_pressed("q"):
        # Key was pressed
        break

    d = random.randint(1, 5)
    rand_int = random.randint(1, 8)

    dt = datetime.now()
    result = dt + timedelta(minutes=d)

    while True:
        time.sleep(10)
        if datetime.now() > result:
            break

    print(dt)  # 👉️ 2023-11-24 09:30:00.000123
    print(f"{result} more {d} seconds")

    now = datetime.now()

    if not QApplication.instance():
        app = QApplication(sys.argv)
    else:
        app = QApplication.instance()

    window = RocWidget(rand_int)
    window.showMaximized()
    window.setWindowFlag(Qt.FramelessWindowHint, True)
    window.setWindowFlag(Qt.WindowStaysOnTopHint, True)
    window.show()

    app.exec()
