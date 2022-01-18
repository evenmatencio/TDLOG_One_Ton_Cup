# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cap.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 600)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, -70, 541, 591))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("roeventcap.jpg"))
        self.label.setObjectName("label")
        self.dial = QtWidgets.QDial(Form)
        self.dial.setGeometry(QtCore.QRect(270, 140, 281, 161))
        self.dial.setMaximum(360)
        self.dial.setWrapping(True)
        self.dial.setNotchesVisible(True)
        self.dial.setObjectName("dial")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(140, 430, 251, 101))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(24)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(150, 480, 321, 101))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(390, 470, 64, 23))
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber_2 = QtWidgets.QLCDNumber(Form)
        self.lcdNumber_2.setGeometry(QtCore.QRect(450, 520, 64, 23))
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(460, 450, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(24)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(520, 500, 31, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(24)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "True direction"))
        self.label_3.setText(_translate("Form", "Deviation from the course:"))
        self.label_4.setText(_translate("Form", "°"))
        self.label_5.setText(_translate("Form", "°"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
