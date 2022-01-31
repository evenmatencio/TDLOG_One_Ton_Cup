import os
import sys
import pandas
import PyQt5
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
import UiMainWindow
import Crewmates
import UpdatingSignal


"""
PLEASE, have a look at the README file before running the code.
"""



class OneTonCupGui(QtWidgets.QMainWindow, UiMainWindow.Ui_MainWindow):
    
    """
    The OneTonCupGui class defines the behavior of the implented GUI.
    The update of the values displayed is managed thanks to the UpdatingValue class, from UpdatingSignal module.
    """
    
    def __init__(self, dataframe):
        
        """
        The initialisation of the crewmates is done thanks to static methods which extract the data stored on a .csv file.
        The correct directory of the data file must be used in the main function.
        """
                
# Initialisation ==============================================================
        
        #============== Initialisationof the main window ======================
        QtWidgets.QMainWindow.__init__(self)
        self.setupUi(self)
        
        #============== Crewmates initialisation ==============================
        self.helm = Crewmates.Helmsman.init_from_pandas(dataframe)
        self.foil = Crewmates.Foilsman.init_from_pandas(dataframe)
        self.wing = Crewmates.Wingsman.init_from_pandas(dataframe)

    
              
# Signals and slots handling ==================================================

        #=============== Crewmates menu button =================================
        self.helmsman_button.clicked.connect(self.helm.main_window_helmsman.show)
        self.foilsman_button.clicked.connect(self.foil.main_window_foilsman.show)
        self.wingsman_button.clicked.connect(self.wing.main_window_wingsman.show)
        
        #=============== Widgets button =======================================
        # Helsmamn
        self.helm.ui_helmsman.depth_button.clicked.connect(self.helm.depth_display_and_update)
        self.helm.ui_helmsman.wind_speed_button.clicked.connect(self.helm.windspeed_display_and_update)
        self.helm.ui_helmsman.cap_button.clicked.connect(self.helm.cap_display_and_update)
        self.helm.ui_helmsman.wind_angles_button.clicked.connect(self.helm.wind_angles_display_and_update)
        self.helm.ui_helmsman.speed_button.clicked.connect(self.helm.boatspeed_display_and_update) 
        # Foilsman
        self.foil.ui_foilsman.wind_angles_button.clicked.connect(self.foil.wind_angles_display_and_update)
        self.foil.ui_foilsman.speed_button.clicked.connect(self.foil.boatspeed_display_and_update) 
        self.foil.ui_foilsman.wind_speed_button.clicked.connect(self.foil.windspeed_display_and_update)
        self.foil.ui_foilsman.depth_button.clicked.connect(self.foil.depth_display_and_update)
        self.foil.ui_foilsman.gite_button.clicked.connect(self.foil.boat_angles_display_and_update)
        self.foil.ui_foilsman.flight_height_button.clicked.connect(self.foil.flight_height_display_and_update)
        # Wingsman
        self.wing.ui_wingsman.wing_angles_button.clicked.connect(self.wing.wing_angles_display_and_update)
        self.wing.ui_wingsman.wind_speed_button.clicked.connect(self.wing.windspeed_display_and_update)
        self.wing.ui_wingsman.wind_angles_button.clicked.connect(self.wing.wind_angles_display_and_update)
        self.wing.ui_wingsman.speed_button.clicked.connect(self.wing.boatspeed_display_and_update) 
        #=============== Updating values callbacks ============================ 
        self.helm.updating_value.value_changed.connect(self.handle_value_updated)
        self.foil.updating_value.value_changed.connect(self.handle_value_updated)
        self.wing.updating_value.value_changed.connect(self.handle_value_updated)



# Slot for updating value =====================================================
        
    def handle_value_updated(self, i):
        if(self.foil.main_window_foilsman.isVisible()) :
            self.foil.correct_slot(i)
        elif(self.helm.main_window_helmsman.isVisible()) :
            self.helm.correct_slot(i)
        elif(self.wing.main_window_wingsman.isVisible()) :
            self.wing.correct_slot(i)  
        QtWidgets.QApplication.processEvents()



def main():
    
    dataframe = pandas.read_csv(os.getcwd() + '/Random_data_72.csv', delimiter=',', header=0)
    app = QtWidgets.QApplication(sys.argv)
    gui = OneTonCupGui(dataframe)
    gui.show()
    sys.exit(app.exec_())



main()



