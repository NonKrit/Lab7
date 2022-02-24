import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class PaintWindow(QWidget):
    def __init__(self, parent) -> None:
        QWidget.__init__(self, parent)
        self.setFixedSize(500, 250)
        self.setWindowTitle("A simple paint program")
        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

        self.draw = False
        self.bSize = 2
        self.bColor = Qt.black
        self.Point = QPoint()

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.draw = True
            self.Point = event.pos()


    def paintEvent(self, event):
        paint = QPainter(self)
        paint.drawImage(self.rect(), self.image, self.image.rect())


class SPP(QWidget):
    def __init__(self) -> None:
        QWidget.__init__(self, None)
        self.setFixedWidth(500)
        font = QFont("Poppins")
        font.setPixelSize(20)
        self.drawWindow = PaintWindow(self)
        label = QLabel(self)
        label.setText("Drag the mouse to draw")
        label.setAlignment(Qt.AlignCenter)
        label.setFont(font)
        label.setGeometry(0, 250, 500, 30)
        self.clear_bt = QPushButton(self)
        self.clear_bt.setText("Clear")
        self.clear_bt.setFont(font)
        self.clear_bt.setGeometry(0, 280, 500, 30)
        self.clear_bt.clicked.connect(self.drawWindow.clear)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    view = SPP()
    view.show()
    sys.exit(app.exec())