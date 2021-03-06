# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cowin.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(548, 536)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        Form.setMinimumSize(QtCore.QSize(20, 22))
        Form.setMaximumSize(QtCore.QSize(720, 738))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setStyleSheet("background: rgb(0, 0, 0);\n"
"border-radius:30px;")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_btns = QtWidgets.QFrame(self.frame)
        self.frame_btns.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_btns.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.frame_btns.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_btns.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_btns.setObjectName("frame_btns")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_btns)
        self.horizontalLayout_7.setContentsMargins(9, 3, 36, 5)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btn_minimize_5 = QtWidgets.QPushButton(self.frame_btns)
        self.btn_minimize_5.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_minimize_5.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_minimize_5.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;        \n"
"    background-color: rgb(255, 170, 0);\n"
"}\n"
"QPushButton:hover {    \n"
"    background-color: rgba(255, 170, 0, 150);\n"
"}")
        self.btn_minimize_5.setText("")
        self.btn_minimize_5.setObjectName("btn_minimize_5")
        self.horizontalLayout_7.addWidget(self.btn_minimize_5)
        self.btn_close_5 = QtWidgets.QPushButton(self.frame_btns)
        self.btn_close_5.setMinimumSize(QtCore.QSize(16, 16))
        self.btn_close_5.setMaximumSize(QtCore.QSize(17, 17))
        self.btn_close_5.setStyleSheet("QPushButton {\n"
"    border: none;\n"
"    border-radius: 8px;        \n"
"    background-color: rgb(255, 0, 0);\n"
"}\n"
"QPushButton:hover {        \n"
"    background-color: rgba(255, 0, 0, 150);\n"
"}")
        self.btn_close_5.setText("")
        self.btn_close_5.setObjectName("btn_close_5")
        self.horizontalLayout_7.addWidget(self.btn_close_5)
        self.verticalLayout.addWidget(self.frame_btns)
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setStyleSheet("background: rgba(255, 255, 255, 0);")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_3.setObjectName("gridLayout_3")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem1, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/resources/icons/Covid-anim-1.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 51, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout_3.addItem(spacerItem2, 1, 1, 1, 1)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        self.frame_3.setStyleSheet("background: rgb(0, 0, 0);\n"
"border-radius:30px;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(113, 60))
        self.pushButton.setMaximumSize(QtCore.QSize(16777215, 200))
        self.pushButton.setStyleSheet("background: rgb(51, 88, 255);\n"
"color: rgb(255, 255, 127);\n"
"border-radius:30px;\n"
"font-size:30px;")
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.frame_3)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.btn_minimize_5.setToolTip(_translate("Form", "Minimize"))
        self.btn_close_5.setToolTip(_translate("Form", "Close"))
        self.pushButton.setText(_translate("Form", "GO"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
