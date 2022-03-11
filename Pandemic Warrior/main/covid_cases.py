# importing libraries
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from bs4 import BeautifulSoup as BS
import requests
import sys
from PyQt5 import QtCore, QtGui, QtWidgets


class Window(QMainWindow):

    def __init__(self):
        super().__init__()

        # setting title
        self.setWindowTitle("Python ")

        # setting geometry
        self.setGeometry(100, 100, 400, 500)

        self.resize(460, 469)
        self.setStyleSheet("")



        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # calling method
        self.UiComponents()

        # showing all the widgets
        self.show()

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

    # method for widgets
    def UiComponents(self):
        self.setObjectName("MainWindow")
        self.resize(460, 469)
        self.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(self)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setStyleSheet("QFrame{background: rgb(36, 31, 49);\n"
                                 "border-radius:30px;}\n"
                                 "\n"
                                 "/* VERTICAL SCROLLBAR */\n"
                                 " QScrollBar:vertical {\n"
                                 "    border: none;  \n"
                                 "    background-color: rgb(209, 209, 209);\n"
                                 "    width: 14px;\n"
                                 "    margin: 15px 0 15px 0;\n"
                                 "    border-radius: 0px;\n"
                                 " }\n"
                                 "\n"
                                 "/*  HANDLE BAR VERTICAL */\n"
                                 "QScrollBar::handle:vertical {    \n"
                                 "    background-color: rgb(119, 118, 123);\n"
                                 "    min-height: 30px;\n"
                                 "    border-radius: 7px;\n"
                                 "}\n"
                                 "QScrollBar::handle:vertical:hover{    \n"
                                 "     \n"
                                 "    background-color: rgb(100, 100, 100);\n"
                                 "}\n"
                                 "QScrollBar::handle:vertical:pressed {    \n"
                                 "     \n"
                                 "    background-color: rgb(100, 100, 100);\n"
                                 "}\n"
                                 "\n"
                                 "/* BTN TOP - SCROLLBAR */\n"
                                 "QScrollBar::sub-line:vertical {\n"
                                 "    border: none;\n"
                                 "    background-color: rgb(119, 118, 123);    \n"
                                 "    height: 15px;\n"
                                 "    border-top-left-radius: 7px;\n"
                                 "    border-top-right-radius: 7px;\n"
                                 "    subcontrol-position: top;\n"
                                 "    subcontrol-origin: margin;\n"
                                 "}\n"
                                 "QScrollBar::sub-line:vertical:hover {    \n"
                                 "    background-color: rgb(100, 100, 100);\n"
                                 "}\n"
                                 "QScrollBar::sub-line:vertical:pressed {    \n"
                                 "    background-color: rgb(100, 100, 100);\n"
                                 "}\n"
                                 "\n"
                                 "/* BTN BOTTOM - SCROLLBAR */\n"
                                 "QScrollBar::add-line:vertical {\n"
                                 "    border: none;\n"
                                 "    background-color: rgb(119, 118, 123);\n"
                                 "    height: 15px;\n"
                                 "    border-bottom-left-radius: 7px;\n"
                                 "    border-bottom-right-radius: 7px;\n"
                                 "    subcontrol-position: bottom;\n"
                                 "    subcontrol-origin: margin;\n"
                                 "}\n"
                                 "QScrollBar::add-line:vertical:hover {    \n"
                                 "    background-color: rgb(100, 100, 100);\n"
                                 "}\n"
                                 "QScrollBar::add-line:vertical:pressed {    \n"
                                 "    background-color: rgb(100, 100, 100);\n"
                                 "}\n"
                                 "\n"
                                 "/* RESET ARROW */\n"
                                 "QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {\n"
                                 "    background: none;\n"
                                 "}\n"
                                 "QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {\n"
                                 "    background: none;\n"
                                 "}\n"
                                 "\n"
                                 "")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_4 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setStyleSheet("background: rgba(191, 64, 64, 0);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_3.setContentsMargins(10, 0, 11, 5)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(1, 3, 5, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_minimize_3 = QtWidgets.QPushButton(self.frame_4)
        self.btn_minimize_3.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_minimize_3.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_minimize_3.setStyleSheet("QPushButton {\n"
                                          "    border: none;\n"
                                          "    border-radius: 8px;        \n"
                                          "    background-color: rgb(255, 170, 0);\n"
                                          "}\n"
                                          "QPushButton:hover {    \n"
                                          "    background-color: rgba(255, 170, 0, 150);\n"
                                          "}")
        self.btn_minimize_3.setText("")
        self.btn_minimize_3.setObjectName("btn_minimize_3")
        self.horizontalLayout.addWidget(self.btn_minimize_3)
        self.btn_close_3 = QtWidgets.QPushButton(self.frame_4)
        self.btn_close_3.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_close_3.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_close_3.setStyleSheet("QPushButton {\n"
                                       "    border: none;\n"
                                       "    border-radius: 8px;        \n"
                                       "    background-color: rgb(255, 0, 0);\n"
                                       "}\n"
                                       "QPushButton:hover {        \n"
                                       "    background-color: rgba(255, 0, 0, 150);\n"
                                       "}")
        self.btn_close_3.setText("")
        self.btn_close_3.setObjectName("btn_close_3")
        self.horizontalLayout.addWidget(self.btn_close_3)
        self.gridLayout_3.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_4)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 71))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 89))
        self.frame_2.setStyleSheet("background: rgba(191, 64, 64, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox.setStyleSheet("background: #fcff98;\n"
                                    "color: rgb(99, 69, 44);font-size:25px;border-radius:0px;")
        self.comboBox.setObjectName("comboBox")
        self.gridLayout_2.addWidget(self.comboBox, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(56, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem1, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(54, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        self.verticalLayout_2.addWidget(self.frame_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 55, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem3)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("background: rgba(191, 64, 64, 0);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout.setSpacing(17)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setStyleSheet("border: 3px dashed rgb(252, 255, 164);\n"
                                   "color: rgb(255, 254, 129);\n"
                                   "background: rgba(191, 64, 64, 0);\n"
                                   "border-radius:15px;font-size:20px")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        self.label_3.setStyleSheet("border: 3px dashed rgb(252, 255, 164);\n"
                                   "color: rgb(255, 254, 129);\n"
                                   "background: rgba(191, 64, 64, 0);\n"
                                   "border-radius:15px;font-size:20px")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(self.frame_3)
        self.label_4.setStyleSheet("border: 3px dashed rgb(252, 255, 164);\n"
                                   "color: rgb(255, 254, 129);\n"
                                   "background: rgba(191, 64, 64, 0);\n"
                                   "border-radius:15px;font-size:20px")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.verticalLayout_2.addWidget(self.frame_3)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        self.setCentralWidget(self.centralwidget)
        # countries list // user can add other countries as well
        self.country = ["india", "us", "spain", "china", "russia",
                        "pakistan", "nepal", "italy", "spain",
                        "uk", "brazil"]

        for i in self.country:
            i = i.upper()
            self.comboBox.addItem(i)

        # adding action to the combo box
        self.comboBox.activated.connect(self.get_cases)


        self.label_2.setAlignment(Qt.AlignCenter)

        self.label_3.setAlignment(Qt.AlignCenter)

        self.label_4.setAlignment(Qt.AlignCenter)

        self.btn_minimize_3.clicked.connect(self.hideWindow)

        self.btn_close_3.clicked.connect(self.close)


    # method called by push
    def get_cases(self):
        # getting country name
        index = self.comboBox.currentIndex()
        country_name = self.country[index]

        # creating url using country name
        url = "https://www.worldometers.info/coronavirus/country/" + country_name + "/"

        # getting the request from url
        data = requests.get(url)

        # converting the text
        soup = BS(data.text, 'html.parser')

        # finding meta info for cases
        cases = soup.find_all("div", class_="maincounter-number")

        # getting total cases number
        total = cases[0].text

        # filtering it
        total = total[1: len(total) - 2]

        # getting recovered cases number
        recovered = cases[2].text

        # filtering it
        recovered = recovered[1: len(recovered) - 1]

        # getting death cases number
        deaths = cases[1].text

        # filtering it
        deaths = deaths[1: len(deaths) - 1]

        # show data through labels
        self.label_2.setText("Total Cases : " + total)
        self.label_3.setText("Recovered Cases : " + recovered)
        self.label_4.setText("Total Deaths : " + deaths)



# create pyqt5 app
App = QApplication(sys.argv)

# create the instance of our Window
window = Window()

window.show()

# start the app
sys.exit(App.exec())