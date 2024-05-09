from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QDialog, QToolButton, QApplication
from widget import Widget

class ToolWidget(QDialog):
    def __init__(self):
        super().__init__()
        self.resize(200,50)
        btn = QToolButton(self)
        btn.setText('开始')
        btn.setGeometry(20,20,50,20)
        btn.clicked.connect(self.startCut)
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
