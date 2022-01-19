from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GiteWidget(object):
    
    
    def setupUi(self, Form, value):
        Form.setObjectName("Form")
        Form.resize(800, 800)
        # self.label = QtWidgets.QLabel(Form)
        # self.label.setGeometry(QtCore.QRect(-250, 100, 1041, 571))
        # self.label.setText("")
        # self.label.setPixmap(QtGui.QPixmap("../../../Downloads/gite.png"))
        # self.label.setObjectName("label")
        self.lcdNumber = QtWidgets.QLCDNumber(Form)
        self.lcdNumber.setGeometry(QtCore.QRect(160, 230, 101, 51))
        self.lcdNumber.setFrameShadow(QtWidgets.QFrame.Plain)
        self.lcdNumber.setLineWidth(2)
        self.lcdNumber.setMidLineWidth(0)
        self.lcdNumber.setProperty("intValue", int(value))
        self.lcdNumber.setObjectName("lcdNumber")
        self.textEdit = QtWidgets.QTextEdit(Form)
        self.textEdit.setGeometry(QtCore.QRect(262, 230, 104, 87))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(22)
        self.textEdit.setFont(font)
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        
    

