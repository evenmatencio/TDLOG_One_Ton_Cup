import os
import sys
import pandas
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import UiMainWindow
import Crewmates
import UpdatingSignal





class OneTonCupGui(QtWidgets.QMainWindow, UiMainWindow.Ui_MainWindow):
    
    def __init__(self, dataframe):
        
        # Initialisation 
        #--------------------------------------------------------------------------------------
        # Constructeur de la classe QtGui.QMainWindow
        QtWidgets.QMainWindow.__init__(self)
        # Appel a la methode setupUi de notre Ui_MainWindow
        self.setupUi(self)
        
        # Crewmates managment 
        # -------------------------------------------------------------------------------------
        self.helm = Crewmates.Helmsman( 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.helm.from_pandas(dataframe)
        self.foil = Crewmates.Foilsman(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
        self.foil.from_pandas(dataframe)
        
        
        # Signals and slots handling
        #--------------------------------------------------------------------------------------
        # Boutons du menu principal
        self.helmsman_button.clicked.connect(self.helm.main_window_helmsman.show)
        self.foilsman_button.clicked.connect(self.foil.main_window_foilsman.show)
        # Boutons des widgets
        # Helsmamn
        self.helm.ui_helmsman.depth_button.clicked.connect(self.helm.depth_display_and_update)
        self.helm.ui_helmsman.wind_speed_button.clicked.connect(self.helm.windspeed_display_and_update)
        self.helm.ui_helmsman.cap_button.clicked.connect(self.helm.cap_display_and_update)
        self.helm.ui_helmsman.wind_angles_button.clicked.connect(self.helm.wind_angles_display_and_update)
        # Foilsman
        self.foil.ui_foilsman.depth_button.clicked.connect(self.foil.depth_display_and_update)
        self.foil.ui_foilsman.gite_button.clicked.connect(self.foil.boat_angles_display_and_update)
        # Gestion de l'actualisation des valeurs
        self.helm.updating_value.value_changed.connect(self.handle_value_updated)
        self.foil.updating_value.value_changed.connect(self.handle_value_updated)

        

        
    def handle_value_updated(self, i):
        if(self.foil.main_window_foilsman.isVisible()) :
            self.foil.correct_slot(i)
        if(self.helm.main_window_helmsman.isVisible()) :
            self.helm.correct_slot(i)
        QtWidgets.QApplication.processEvents()




def main():
    
    # dataframe = pandas.read_csv(os.getcwd() + '/Random_data.csv', delimiter=',', header=0)
    dataframe = pandas.read_csv(os.getcwd() + '/Random_data_72.csv', delimiter=',', header=0)
    app = QtWidgets.QApplication(sys.argv)
    gui = OneTonCupGui(dataframe)
    gui.show()
    sys.exit(app.exec_())



main()



