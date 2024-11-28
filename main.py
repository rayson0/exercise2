from random import randint
import sys

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QWidget


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.is_can = False
        uic.loadUi('01.ui', self)
        self.initUI()

    def initUI(self):
        self.btn.clicked.connect(self.is_can_paint)

    def is_can_paint(self):
        self.is_can = True
        self.update()

    def paintEvent(self):
        qp = QPainter()
        qp.begin()
        self.draw(qp, randint(1, 3), randint(20, 120))
        qp.end()

    def draw(self, qp, cnt_ellipse, diam):
        qp.setBrush(QColor(255, 251, 0))
        for _ in range(cnt_ellipse):
            qp.drawEllipse(randint(1, 500), randint(1, 500), diam)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())