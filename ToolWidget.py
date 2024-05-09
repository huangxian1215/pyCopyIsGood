from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QDialog, QApplication, QVBoxLayout, QPushButton
from widget import Widget

class ToolWidget(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(250,50)
        self.setWindowTitle('图像转文字--百度识别')

        btn = QPushButton(self)
        btn.setText('开始')
        # btn.setGeometry(20,20,50,20)
        btn.setMinimumHeight(40)
        btn.clicked.connect(self.startCut)
        vlay = QVBoxLayout(self)
        vlay.addWidget(btn)
        vlay.setContentsMargins(0,0,0,0)
    def startCut(self):
        print('startCut')
        self.hide()
        def fun():
            screen = QApplication.primaryScreen()
            img = screen.grabWindow(0)
            self.wnd = Widget()
            self.wnd.setToolWnd(self, img)
            self.wnd.show()

        QTimer.singleShot(200,lambda : fun())
