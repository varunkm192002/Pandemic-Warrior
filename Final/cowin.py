
import sys
from PyQt5.QtCore import (QRectF)
from PyQt5.QtGui import (QCursor, QPainterPath, QRegion)
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QMovie
import subprocess

from cowin_gui import Ui_Form




class Form(QtWidgets.QWidget, Ui_Form):


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_minimize_5.clicked.connect(self.hideWindow)

        self.btn_close_5.clicked.connect(self.close)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.movie = QMovie("icons/Covid-anim-1.gif")
        self.movie.setScaledSize(QSize().scaled(250, 250, Qt.KeepAspectRatio))
        self.label.setMovie(self.movie)
        self.pushButton.clicked.connect(self.fun)


        self.startAnimation()

    def startAnimation(self):
        self.movie.start()

    def fun(self):
        try:
            subprocess.Popen(['python', 'cowin2.py'])

        except(RuntimeError):
            pass





    def stopAnimation(self):
        self.movie.stop()


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







if __name__ == "__main__":


    app = QtWidgets.QApplication(sys.argv)
    widget = Form()
    widget.show()
    sys.exit(app.exec_())


