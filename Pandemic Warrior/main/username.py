from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import (Qt, QRectF)
from PyQt5.QtGui import (QCursor, QPainterPath, QRegion)
from PyQt5.QtWidgets import *
from username_r import Ui_Form


class LoadingScreen(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(68,68)
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.CustomizeWindowHint)
        self.label_animation=QLabel(self)
        self.movie=QMovie(r"loading.gif")
        self.label_animation.setMovie(self.movie)

        timer=QTimer(self)
        self.startAnimation()
        timer.singleShot(5000,self.stopAnimation)
        
        self.show()

    def startAnimation(self):
        self.movie.start()

    def stopAnimation(self):
        self.movie.stop()
        self.close()


class Qidget(QtWidgets.QWidget, Ui_Form):


    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_minimize_3.clicked.connect(self.hideWindow)

        self.btn_close_3.clicked.connect(self.close)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # Get the position of the mouse relative to the window
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # Change mouse icon

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # Change window position
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    def resizeEvent(self, event):
        path = QPainterPath()
        path.addRoundedRect(QRectF(self.rect()), 20, 20)
        reg = QRegion(path.toFillPolygon().toPolygon())
        self.setMask(reg)

    def hideWindow(self):
        self.showMinimized()






import sys
app = QtWidgets.QApplication(sys.argv)
Form = QtWidgets.QWidget()


if __name__ == "__main__":
    import sys
    widget = Qidget()
    widget.show()
    sys.exit(app.exec_())
