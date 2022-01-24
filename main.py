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
        
        # Signals and slots handling
        #--------------------------------------------------------------------------------------
        # Boutons du menu principal
        self.helmsman_button.clicked.connect(self.helm.main_window_helmsman.show)
        # Boutons des widgets
        self.helm.ui_helmsman.depth_button.clicked.connect(self.helm.depth_display_and_update)
        self.helm.ui_helmsman.wind_speed_button.clicked.connect(self.helm.windspeed_display_and_update)
        # Gestion de l'actualisation des valeurs
        # self.helm.updating_value.value_changed.connect(self.handle_value_updated)
        self.helm.updating_value.value_changed.connect(self.handle_value_updated)

        

        
    def handle_value_updated(self, i):

        if (self.helm.depth_window.isVisible()):
            self. helm.depth_update(i)
        # The other update functions are not yet  defined, so I invented a name for them.
        
        # elif (self.helm.wind_angles_window.isVisible()): 
        #     self. helm.wind_angles_update(i) Widget des angles au vent
        
        # elif (self.helm.wind_speed_window.isVisible):
        #     self.update.wind_speed_update(i) Widget de la vitesse du vent
            
        # elif (self.helm.boat_speed_window.isVisible()):
        #     self.update.boat_speed_window_update(i) Widget de la VMG

        # if(sum(window.isVisible() for window in self.helm.displayed_widget) == 1) :
        #     self.helm.correct_slot(i)
        self.helm.correct_slot(i)
        # else :
        # print("c'est la sauce")
        # self.helm.correct_slot(i)   

        QtWidgets.QApplication.processEvents()




def main():
    
    dataframe = pandas.read_csv(os.getcwd() + '/Random_data.csv', delimiter=',', header=0)
    app = QtWidgets.QApplication(sys.argv)
    gui = OneTonCupGui(dataframe)
    gui.show()
    sys.exit(app.exec_())



main()



