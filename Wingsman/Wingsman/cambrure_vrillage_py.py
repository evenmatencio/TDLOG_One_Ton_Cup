# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'cambrure_vrillage_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_wing_angles(object):
    def setupUi(self, Form):
        self.cambrure_value = 32
        self.vrillage_value_1 = 12
        self.vrillage_value_2 = 14

        Form.setObjectName("Form")
        Form.resize(800, 800)


        self.label_twisting1 = QtWidgets.QLabel(Form)
        self.label_twisting1.setGeometry(QtCore.QRect(90, 200, 230, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(18)
        self.label_twisting1.setFont(font)
        self.label_twisting1.setObjectName("Twisting1")


        self.label_twisting2 = QtWidgets.QLabel(Form)
        self.label_twisting2.setGeometry(QtCore.QRect(90, 290, 230, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(18)
        self.label_twisting2.setFont(font)
        self.label_twisting2.setObjectName("Twisting2")

        self.twisting1_nb = QtWidgets.QLCDNumber(Form)
        self.twisting1_nb.setGeometry(QtCore.QRect(330, 200, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        self.twisting1_nb.setFont(font)
        self.twisting1_nb.setFrameShadow(QtWidgets.QFrame.Plain)
        self.twisting1_nb.setLineWidth(2)
        self.twisting1_nb.setObjectName("twisting1_nb")
        self.twisting1_nb.setProperty("intValue", self.vrillage_value_1)

        self.twisting2_nb = QtWidgets.QLCDNumber(Form)
        self.twisting2_nb.setGeometry(QtCore.QRect(330, 290, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        self.twisting2_nb.setFont(font)
        self.twisting2_nb.setFrameShadow(QtWidgets.QFrame.Plain)
        self.twisting2_nb.setLineWidth(2)
        self.twisting2_nb.setObjectName("twisting2_nb")
        self.twisting2_nb.setProperty("intValue", self.vrillage_value_2)


        self.label_camber = QtWidgets.QLabel(Form)
        self.label_camber.setGeometry(QtCore.QRect(90, 380, 230, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(18)
        self.label_camber.setFont(font)
        self.label_camber.setObjectName("Twisting2")


        self.camber_nb = QtWidgets.QLCDNumber(Form)
        self.camber_nb.setGeometry(QtCore.QRect(330, 380, 121, 61))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        self.camber_nb.setFont(font)
        self.camber_nb.setFrameShadow(QtWidgets.QFrame.Plain)
        self.camber_nb.setLineWidth(2)
        self.camber_nb.setObjectName("camber_nb")
        self.camber_nb.setProperty("intValue", self.cambrure_value)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_twisting1.setText(_translate("Form", "Vrillage angle 1:"))
        self.label_twisting2.setText(_translate("Form", "Vrillage angle 2:"))
        self.label_camber.setText(_translate("Form", "Cambrure angle:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_wing_angles()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())