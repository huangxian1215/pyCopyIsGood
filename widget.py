from PyQt5.QtGui import QKeyEvent, QMouseEvent, QPaintEvent, QPixmap, QPainter, QPen
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import Qt, QRect


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        # self.setGeometry(0,0,8000,5000)
        self.showMaximized()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.initPos()

    def initPos(self):
        self.x0 = self.y0 = self.x1 = self.y1 = 0
        self.rect = QRect(0,0,0,0)

    def setToolWnd(self, wnd, pix):
        self.tool = wnd
        self.pixmap = pix

    def closeEvent(self, event):
        self.tool.show()

    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key_Escape:
            self.close()

    def mousePressEvent(self, event: QMouseEvent) -> None:
        self.x0 = self.x1 = event.x()
        self.y0 = self.y1 = event.y()

    def mouseReleaseEvent(self, event: QMouseEvent) -> None:
        pix = self.grab(self.rect)
        pix.save('./1.png')
        self.initPos()
        self.close()


    def mouseMoveEvent(self, event: QMouseEvent) -> None:
        self.x1 = event.x()
        self.y1 = event.y()
        self.update()

    def paintEvent(self, event: QPaintEvent) -> None:
        super().paintEvent(event)
        rect = QRect(self.x0, self.y0, self.x1 - self.x0, self.y1 - self.y0)
        self.rect = rect
        # self.pixmap.file(Qt.transparent)
        # self.pixmap = QPixmap(self.file_path)
        painter = QPainter(self)
        painter.drawPixmap(0,0,self.width(),self.height(), self.pixmap)
        painter.setPen(QPen(Qt.blue, 1, Qt.SolidLine))
        painter.drawRect(rect)
