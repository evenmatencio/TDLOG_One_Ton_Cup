import os
import sys
import pandas
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *


try:
    import UiMainWindow
    import Crewmates
    import UpdatingSignal

except Exception as e:
    print(e)



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
        self.helm.ui_helmsman.gite_button.clicked.connect(self.helm.gite_display_and_update)
        # Gestion de l'actualisation des valeurs
        self.helm.updating_value.value_changed.connect(self.handle_value_updated)

        
    def handle_value_updated(self, i):
        self. helm.gite_update(i)
        QtWidgets.QApplication.processEvents()



def main():
    
    dataframe = pandas.read_csv(os.getcwd() + '/Random_data.csv', delimiter=',', header=0)
    app = QtWidgets.QApplication(sys.argv)
    gui = OneTonCupGui(dataframe)
    gui.show()
    sys.exit(app.exec_())



main()



