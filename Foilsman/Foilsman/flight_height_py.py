# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'flight_height_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_flight_height(object):
    def setupUi(self, Form):
        self.flight_height_value = 1.12

        flight_height.setObjectName("flight_height")
        flight_height.resize(800, 800)


        self.label_flight_height = QtWidgets.QLabel(Form)
        self.label_flight_height.setGeometry(QtCore.QRect(200, 330, 391, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(18)
        self.label_flight_height.setFont(font)
        self.label_flight_height.setObjectName("flight_height")

        self.fh_nb = QtWidgets.QLCDNumber(flight_height)
        self.fh_nb.setGeometry(QtCore.QRect(400, 330, 131, 61))
        self.fh_nb.setFrameShadow(QtWidgets.QFrame.Plain)
        self.fh_nb.setLineWidth(2)
        self.fh_nb.setProperty("value", self.flight_height_value)
        self.fh_nb.setProperty("intValue", abs(self.flight_height_value))
        self.fh_nb.setObjectName("fh_nb")

        #m pour mètres text edit
        self.m = QtWidgets.QLabel(Form)
        self.m.setGeometry(QtCore.QRect(540, 340, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(20)
        self.m.setFont(font)
        self.m.setObjectName("m")

        self.retranslateUi(flight_height)
        QtCore.QMetaObject.connectSlotsByName(flight_height)

    def retranslateUi(self, flight_height):
        _translate = QtCore.QCoreApplication.translate
        flight_height.setWindowTitle(_translate("flight_height", "Form"))
        self.label_flight_height.setText(_translate("Form", "Flight Height:"))
        self.m.setText(_translate("Form", "m"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    flight_height = QtWidgets.QWidget()
    ui = Ui_flight_height()
    ui.setupUi(flight_height)
    flight_height.show()
    sys.exit(app.exec_())
