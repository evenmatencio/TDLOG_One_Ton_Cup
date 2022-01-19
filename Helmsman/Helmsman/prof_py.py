# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'prof_widget.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Depth(object):
    def setupUi(self, Form, value):
        #Widget prof
        Form.setObjectName("prof")
        Form.resize(800, 800)
        Form.setContextMenuPolicy(QtCore.Qt.NoContextMenu)

        #Image prof_boat dans label
        self.prof_boat = QtWidgets.QLabel(Form)
        self.prof_boat.setGeometry(QtCore.QRect(70, 110, 641, 531))
        self.prof_boat.setText("")
        self.prof_boat.setPixmap(QtGui.QPixmap("prof.png"))
        self.prof_boat.setObjectName("prof_boat")
        
        self.prof_nb = QtWidgets.QLCDNumber(Form)
        self.prof_nb.setGeometry(QtCore.QRect(390, 420, 101, 51))
        self.prof_nb.setFrameShape(QtWidgets.QFrame.Box)
        self.prof_nb.setFrameShadow(QtWidgets.QFrame.Plain)
        self.prof_nb.setLineWidth(4)
        self.prof_nb.setMidLineWidth(0)
        self.prof_nb.setProperty("value", value)
        self.prof_nb.setObjectName("prof_nb")

        #m pour mètres text edit
        self.m = QtWidgets.QTextEdit(Form)
        self.m.setGeometry(QtCore.QRect(495, 428, 41, 51))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(18)
        self.m.setFont(font)
        self.m.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.m.setReadOnly(True)
        self.m.setTabStopWidth(84)
        self.m.setObjectName("m")


        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, prof):
        _translate = QtCore.QCoreApplication.translate
        prof.setWindowTitle(_translate("prof", "Form"))
        self.m.setHtml(_translate("prof", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Yu Gothic Light\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'MS Shell Dlg 2\';\">m</span></p></body></html>"))

    def update(self, new_prof):
        self.prof_nb.setProperty("value", new_prof)
        self.prof_nb.setProperty("intValue", int(new_prof))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = Ui_Depth()
    ui.setupUi(window, 0.)
    window.show()
    sys.exit(app.exec_())
