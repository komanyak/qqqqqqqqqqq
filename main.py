from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QMainWindow
import sys
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.Flag = False
        self.pushButton.clicked.connect(self.ddd)

    def paintEvent(self, event):
        if self.Flag:
            self.q = QPainter()
            self.q.begin(self)
            self.draw(self.q)
            self.q.end()

    def draw(self, q):
        a = randint(0, 250)
        x = randint(0, 750)
        y = randint(0, 550)
        q.setBrush(QColor('yellow'))
        q.drawEllipse(x, y, a, a)

    def ddd(self):
        self.Flag = True
        self.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
