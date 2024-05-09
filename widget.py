from PyQt5.QtGui import QKeyEvent, QMouseEvent, QPaintEvent, QPixmap, QPainter, QPen
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QSpacerItem, QSizePolicy, \
    QPlainTextEdit, QApplication
from PyQt5.QtCore import Qt, QRect

from AipOcr import pic2txt


class Widget(QWidget):
    def __init__(self):
        super(Widget, self).__init__()
        # self.setGeometry(0,0,8000,5000)
        self.showMaximized()
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.initPos()
        self.setCursor(Qt.CrossCursor)

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
        self.setCursor(Qt.ArrowCursor)
        pix = self.grab(self.rect)
        pix.save('./tmp.png')
        self.initPos()
        self.close()
        self.showCurrent(pix)

    def showCurrent(self, pix:QPixmap):
        self.label = QLabel()
        self.label.setPixmap(pix)
        self.widget = QWidget()
        self.widget.setWindowTitle('图像转文字--百度识别')
        vlay = QVBoxLayout(self.widget)
        vlay.addWidget(self.label)
        self.widget.show()
        hlay = QHBoxLayout()
        self.btnReg = QPushButton(self.widget)
        self.btnReg.setText('识别')

        horizontalSpacer = QSpacerItem(40, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hlay.addItem(horizontalSpacer)
        hlay.addWidget(self.btnReg)
        vlay.addLayout(hlay)
        self.plaintext = QPlainTextEdit(self.widget)
        vlay.addWidget(self.plaintext)

        hlay1 = QHBoxLayout()
        self.btnCopy = QPushButton(self.widget)
        self.btnCopy.setText('复制')
        horizontalSpacer1 = QSpacerItem(40, 17, QSizePolicy.Expanding, QSizePolicy.Minimum)
        hlay1.addItem(horizontalSpacer1)
        hlay1.addWidget(self.btnCopy)
        vlay.addLayout(hlay1)
        vlay.setContentsMargins(0, 0, 0, 0)

        self.btnReg.clicked.connect(self.baiduPic2txt)
        self.btnCopy.clicked.connect(self.copyTxt)

    def baiduPic2txt(self):
        txt = pic2txt()
        self.plaintext.setPlainText(txt)

    def copyTxt(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(self.plaintext.toPlainText())

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
