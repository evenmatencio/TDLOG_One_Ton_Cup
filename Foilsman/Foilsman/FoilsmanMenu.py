from PyQt5 import QtCore, QtGui, QtWidgets



class Ui_MainWindowFoilsman(object):


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("FoilsmanWindow")
        MainWindow.resize(846, 686)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(36)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setReadOnly(True)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.graphicsView = QtWidgets.QGraphicsView(self.frame)
        self.graphicsView.setObjectName("graphicsView")
        # self.initialize_view()
        self.verticalLayout_2.addWidget(self.graphicsView)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.frame_2)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        font.setPointSize(20)
        self.lineEdit.setFont(font)
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setReadOnly(True)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.scrollArea = QtWidgets.QScrollArea(self.frame_2)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 178, 523))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        #========Speed/VMG button=====
        self.speed_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.speed_button.sizePolicy().hasHeightForWidth())
        self.speed_button.setSizePolicy(sizePolicy)
        self.speed_button.setMinimumSize(QtCore.QSize(0, 100))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        self.speed_button.setFont(font)
        self.speed_button.setObjectName("speed_button")
        self.verticalLayout_3.addWidget(self.speed_button)

        #========Flight height button======
        self.flight_height_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.flight_height_button.sizePolicy().hasHeightForWidth())
        self.flight_height_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        self.flight_height_button.setFont(font)
        self.flight_height_button.setObjectName("flight_height_button")
        self.verticalLayout_3.addWidget(self.flight_height_button)

        #==============Depth button========
        self.depth_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.depth_button.sizePolicy().hasHeightForWidth())
        self.depth_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        self.depth_button.setFont(font)
        self.depth_button.setObjectName("depth_button")
        self.verticalLayout_3.addWidget(self.depth_button)

        #===========Wind angles button===============
        self.wind_angles_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wind_angles_button.sizePolicy().hasHeightForWidth())
        self.wind_angles_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        self.wind_angles_button.setFont(font)
        self.wind_angles_button.setObjectName("wind_angles_button")
        self.verticalLayout_3.addWidget(self.wind_angles_button)

        #===========Wind speed button===============
        self.wind_speed_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wind_speed_button.sizePolicy().hasHeightForWidth())
        self.wind_speed_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        self.wind_speed_button.setFont(font)
        self.wind_speed_button.setObjectName("wind_speed_button")
        self.verticalLayout_3.addWidget(self.wind_speed_button)

        #===========Gite&Tangage button===============
        self.gite_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.gite_button.sizePolicy().hasHeightForWidth())
        self.gite_button.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Yu Gothic Light")
        self.gite_button.setFont(font)
        self.gite_button.setObjectName("gite_button")
        self.verticalLayout_3.addWidget(self.gite_button)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout.addWidget(self.frame_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 846, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("FoilsmanWindow", "FoilsmanWindow"))
        self.lineEdit_2.setText(_translate("FoilsmanWindow", "Foilsman"))
        self.lineEdit.setText(_translate("FoilsmanWindow", "Menu"))
        self.speed_button.setText(_translate("FoilsmanWindow", "Speed"))
        self.flight_height_button.setText(_translate("FoilsmanWindow", "Flight Height"))
        self.depth_button.setText(_translate("FoilsmanWindow", "Depth"))
        self.wind_angles_button.setText(_translate("FoilsmanWindow", "Wind Angles"))
        self.wind_speed_button.setText(_translate("FoilsmanWindow", "Wind Speed"))
        self.gite_button.setText(_translate("FoilsmanWindow", "Gite&Tangage"))




    # def initialize_view(self):
    #      self.test_scene = QtWidgets.QGraphicsScene(0, 0, 100, 100)
    #      self.gite = Ui_GiteWidget()
    #      self.gite.setupUi(self.test_scene)
    #      self.graphicsView.setScene(self.test_scene)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindowFoilsman()
    ui.setupUi(MainWindow)
    MainWindow.show()

    #Signal managment
    #=================
    #Button "map-position"
    #ui.pushButton.clicked.connect(ui.show_gite_widget)
    #Button "depth"
    #ui.pushButton_2.clicked.connect(ui.show_wind_angle_widget)




    sys.exit(app.exec_())


