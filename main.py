import sys

from random import randint
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication

class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.setWindowTitle('Git и желтые окружности')
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_ellipse(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        x, y = 175, 250
        r = randint(0, 300)
        qp.drawEllipse(x - (r / 2), y - (r / 2), r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())