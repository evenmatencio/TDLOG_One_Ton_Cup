from PyQt5 import QtCore, QtGui, QtWidgets
import numpy 
import TDL_OTC_Data as Data
import UpdatingSignal

#Import of Helsman's widgets
import Helmsman.HelmsmanMenu as HelmMenu
import Helmsman.depth_py as CrewDepth
import Helmsman.cappy1 as CrewCap
import Helmsman.windanglespy as CrewWindAngles
import Helmsman.windspeed2 as CrewWindSpeed
import Helmsman.VMG as CrewSpeed

#Import of Foilsman's widgets
import Foilsman.FoilsmanMenu as FoilMenu
import Foilsman.flight_height_py as CrewFlightHeight
import Foilsman.gite_tangage_py as CrewGite

#Import of Wingsman's widgets
import Wingsman.WingsmanMenu as WingMenu
import Wingsman.cambrure_vrillage_py as CrewWingAngles



"""This module contains the classes for the different members of the sailing team"""

""" Vocabulary
* Equipier= Crewmate
* Barreur= Helmsman
* Equipier en charge du foil= Foilsman
* Equipier en charge de l'aile= Wingsman"""

"""The aim is to create a display function proper to each crewmate"""
"""Choice of variables:
   Helmsman: Latitude, Longitude, Apparent wind, True wind, Wind Speed, Depth, Velocity Made Good, Buoy_Latitude, Buoy_Longitude, Direction (Cap)
   Foilsman: Depth, Flight Heigth, Pitching (Tanguage) angle, List angle (angle de list), Deviation from the course, 
   Wingsman: Vrillage angles, Cambrure angles, Wind Speed, Apparent wind, True Wind """


class CrewMate:

    def __init__(self, wind_angles, wind_speed, speed) :
        """Initializes the object CrewMate. 
        Creates all the objects it needs to work correctly : its own data, windows and widgets.
        """

        #================== Name and data ======================
        self.speed = speed
        self.wind_speed = wind_speed
        self.wind_angles = wind_angles

        #========== Updating value ===========
        self.updating_value = UpdatingSignal.UpdatingValue(self)
        self.correct_slot = None

        #=========== Windows and common widgets ==================
        
         # --> Wind angles: True and apparent wind angle
        self.wind_angles_window = QtWidgets.QMainWindow()
        self.wind_angles_widget = CrewWindAngles.Ui_WindAngles()
        
        # --> Wind speed
        self.wind_speed_window = QtWidgets.QMainWindow()
        self.wind_speed_widget = CrewWindSpeed.Ui_WindSpeed()
        
        # --> VMG
        self.boat_speed_window = QtWidgets.QMainWindow()
        self.boat_speed_widget = CrewSpeed.Ui_VMG()
        
        # --> Depth
        self.depth_window = QtWidgets.QMainWindow()
        self.depth_widget = CrewDepth.Ui_Depth()


    def from_pandas(self, dataframe):
        """
        Argument:  A dataframe.
        Action: Imports the data in the right CrewMate instances, 
        thanks to the static method created in TDL_OTC_Data.
        
        """
        self.speed = Data.Speeds.from_pandas(dataframe)
        self.wind_angles = Data.WingAngles.from_pandas(dataframe)
        self.wind_speed = Data.WindSpeed.from_pandas(dataframe)
        

# UPDATING WINDSPEED=============================================


    def windspeed_update(self, i):
        """"
        Argument: Integer 'i'. Represents the index of the dataframe's column we are looking at. 
                  We want to display the value contained in column i.
        Action: Changes the values of each element present in the widget
        Dial= Bouton de réglage; lcdNumber= Apparent Wind Speed Value; lcdNumber2= True Wind Speed
        
        """
        
        # Changing the values 
        self.wind_speed_widget.lcdNumber.display(self.wind_speed.data_import[i][0])
        self.wind_speed_widget.lcdNumber_2.display(self.wind_speed.data_import[i][1])
        self.wind_speed_widget.dial.setValue(int(self.wind_speed.data_import[i][0]))
        
        
        # The background image
        self.wind_speed_widget.label.setPixmap(QtGui.QPixmap("Helmsman/Helmsman/vitessevent.png"))
        
        # Displaying the window
        self.wind_speed_window.show()
        
        # Checking the value in Python's console
        print(f"wind_speed.data_import = {self.wind_speed.data_import[i]}")

    def windspeed_display_and_update(self):
        """
        Action: setupUi: to initialize the parameters of the window.
                Correct slot: 
                Calls the method update to effectively change the value
                Calls the method processEvents to handle the Dataframe 
                scanning (le parcours du dataframe, ie le changement de valeur)
                and display at the same time.
                Calls emit_signal to show that the value has been changed
        """
       
        self.wind_speed_widget.setupUi(self.wind_speed_window, self.wind_speed.data_import[0])
        self.correct_slot = self.windspeed_update
        self.windspeed_update(0)
        QtWidgets.QApplication.processEvents()
        self.wind_speed_window.show()
        self.updating_value.emit_signal()

# UPDATING WINDANGLES VALUES ============================================================

    def wind_angles_update(self, i):
        
        #Changing the values 
        self.wind_angles_widget.true_wind_angle_nb.display(int(self.wind_angles.data_import[i][0]))
        self.wind_angles_widget.apparent_wind_angle_nb.display(int(self.wind_angles.data_import[i][1]))
        self.wind_angles_widget.dial.setValue(int(self.wind_angles.data_import[i][0]))
        
        #The background image
        self.wind_angles_widget.img_rosevents.setPixmap(QtGui.QPixmap("Helmsman/Helmsman/RoseVents.jpg"))
        
        #Displaying the window
        self.wind_angles_window.show()
        self.wind_angles_window.show()
        
        #Checking the value in Python's console
        print(f"wind_angles.data_import = {self.wind_angles.data_import[i]}")

    def wind_angles_display_and_update(self):
        
        self.wind_angles_widget.setupUi(self.wind_angles_window)
        self.correct_slot = self.wind_angles_update
        self.wind_angles_update(0)
        self.wind_angles_window.show()
        QtWidgets.QApplication.processEvents()
        self.updating_value.emit_signal()

# UPDATING BOATSPEED=================================================

    def boatspeed_update(self, i):
        
        #Changing the values
        self.boat_speed_widget.vmg_nb.display(self.speed.data_import[i][1])
        self.boat_speed_widget.wind_angle_nb.display(self.speed.data_import[i][1])
        
        #The background image
        self.boat_speed_widget.label.setPixmap(QtGui.QPixmap("Helmsman/Helmsman/VMG.png"))
        
        #Displaying the window
        self.boat_speed_window.show()
        print(f"speed.data_import = {self.speed.data_import[i][1]}")

    def boatspeed_display_and_update(self):
        self.boat_speed_widget.setupUi(self.boat_speed_window)
        self.correct_slot = self.boatspeed_update
        self.boatspeed_update(0)
        QtWidgets.QApplication.processEvents()
        self.boat_speed_window.show()
        self.updating_value.emit_signal()
        

        
   
        
#=============================================================================================================
#==============================================================================================================

class Helmsman(CrewMate):
    
    def __init__(self, wind_angles, wind_speed, speed, cap, road_deviation, depth) :
        super().__init__(wind_angles, wind_speed, speed)
        self.cap = cap
        self.depth = depth
        self.road_deviation = road_deviation

        # Window for helmsman menu
        self.main_window_helmsman = QtWidgets.QMainWindow()
        self.ui_helmsman = HelmMenu.Ui_MainWindowHelmsman()
        self.ui_helmsman.setupUi(self.main_window_helmsman)
        

        # Widgets for helmsman and their windows
        self.cap_window = QtWidgets.QMainWindow()
        self.cap_widget = CrewCap.Ui_Cap()
        self.depth_window = QtWidgets.QMainWindow()
        self.depth_widget = CrewDepth.Ui_Depth()
        
        
        # Widgets managment 
        self.list_of_windows = [self.depth_window,
                                 self.cap_window,
                                 self.wind_angles_window,
                                 self.wind_speed_window,
                                 self.boat_speed_window]
        
        
    def from_pandas(self, dataframe):
        #Importing data from the dataframe
        super().from_pandas(dataframe)
        self.cap = Data.Cap.from_pandas(dataframe)
        self.road_deviation = Data.RoadDeviation.from_pandas(dataframe)
        self.depth = Data.Depth.from_pandas(dataframe)
        
        
    @staticmethod
    def init_from_pandas(dataframe) :
        Helms = Helmsman( 0, 0, 0, 0, 0, 0)
        Helms.from_pandas(dataframe)
        return Helms

      
# UPDATING CAP VALUES ============================================================

    def cap_update(self, i):
        
        # Changing the values in the widget
        self.cap_widget.true_direction_value.display(int(self.cap.data_import[i]))
        self.cap_widget.deviation_value.display(int(self.road_deviation.data_import[i]))
        self.cap_widget.dial.setValue(int(self.cap.data_import[i]))
        
        # The background image
        self.cap_widget.cap_picture.setPixmap(QtGui.QPixmap("Helmsman/Helmsman/roeventcap.jpg"))
        
        #Displaying the window
        self.cap_window.show()
        
        #Checking the value in Python's console
        print(f"cap.data_import = {self.cap.data_import[i]}")
        
    def cap_display_and_update(self):
        self.cap_widget.setupUi(self.cap_window)
        self.correct_slot = self.cap_update
        self.cap_update(0)
        QtWidgets.QApplication.processEvents()
        self.cap_window.show()
        self.updating_value.emit_signal()
        
        
# UPDATING DEPTH VALUES ============================================================

    def depth_update(self, i):
        
        # Changing the values in the widget
        self.depth_widget.depth_nb.display(int(self.depth.data_import[i]))
        
        # The background image
        self.depth_widget.depth_boat.setPixmap(QtGui.QPixmap("Helmsman/Helmsman/depth.png"))
        
        #Displaying the window
        self.depth_window.show()
        
        #Checking the value in Python's console
        print(f"depth.data_import = {self.depth.data_import[i]}")


    def depth_display_and_update(self):
        self.depth_widget.setupUi(self.depth_window)
        self.correct_slot = self.depth_update
        self.depth_update(0)
        self.depth_window.show()
        QtWidgets.QApplication.processEvents()
        self.updating_value.emit_signal()
       

        


#=============================================================================================================
#==============================================================================================================

class Foilsman(CrewMate):
    
    def __init__(self, wind_angles, wind_speed, speed, boat_angles, flight_height, depth) :
        super().__init__(wind_angles, wind_speed, speed)
        self.boat_angles = boat_angles
        self.flight_height = flight_height
        self.depth = depth

        # Window for foilsman menu
        self.main_window_foilsman = QtWidgets.QMainWindow()
        self.ui_foilsman = FoilMenu.Ui_MainWindowFoilsman()
        self.ui_foilsman.setupUi(self.main_window_foilsman)

        # Widgets for foilsman and their window
        self.gite_window = QtWidgets.QMainWindow()
        self.gite_widget = CrewGite.Ui_gite_tangage()
        self.flight_height_window = QtWidgets.QMainWindow()
        self.flight_height_widget = CrewFlightHeight.Ui_flight_height()
        self.depth_window = QtWidgets.QMainWindow()
        self.depth_widget = CrewDepth.Ui_Depth()

        # Widgets managment 
        self.list_of_windows = [self.depth_window,
                                self.wind_angles_window,
                                self.wind_speed_window,
                                self.boat_speed_window,
                                self.gite_window,
                                self.flight_height_window]


    def from_pandas(self, dataframe):
        super().from_pandas(dataframe)
        self.depth = Data.Depth.from_pandas(dataframe)
        self.boat_angles = Data.BoatAngles.from_pandas(dataframe)
        self.flight_height = Data.FlightHeight.from_pandas(dataframe)
        
        
    @staticmethod
    def init_from_pandas(dataframe) :
        Foil = Foilsman(0, 0, 0, 0, 0, 0)
        Foil.from_pandas(dataframe)
        return Foil
           

#UPDATING BOAT ANGLES ==================================================

    def boat_angles_display_and_update(self):
        self.gite_widget.setupUi(self.gite_window)
        self.correct_slot = self.boat_angles_update
        self.boat_angles_update(0)
        self.gite_window.show()
        QtWidgets.QApplication.processEvents()
        self.updating_value.emit_signal()

    def boat_angles_update(self, i):
        # Changing the values in the widget
        self.gite_widget.gite_nb.display(int(self.boat_angles.data_import[i][0]))
        self.gite_widget.tangage_nb.display(int(self.boat_angles.data_import[i][0]))
        
        # The background images
        self.gite_widget.image_gite.setPixmap(QtGui.QPixmap("Foilsman/Foilsman/gite.png"))
        self.gite_widget.image_tangage.setPixmap(QtGui.QPixmap("Foilsman/Foilsman/tangage.png"))
        
        #Displaying the window
        self.gite_window.show()
        
        #Checking the value in Python's console
        print(f"boat_angles.data_import = {self.boat_angles.data_import[i]}")


#UPDATING FLIGHT HIGHT=====================================
    
    def flight_height_update(self, i):
        
        # Changing the values in the widget
        self.flight_height_widget.fh_nb.display(self.flight_height.data_import[i])
        
        
       #Displaying the window
        self.flight_height_window.show()
        
        #Checking the value in Python's console
        print(f"flight_height.data_import = {self.flight_height.data_import[i]}")

    def flight_height_display_and_update(self):
        self.flight_height_widget.setupUi(self.flight_height_window)
        self.correct_slot = self.flight_height_update
        self.flight_height_update(0)
        QtWidgets.QApplication.processEvents()
        self.flight_height_window.show()
        self.updating_value.emit_signal()
        
    
# UPDATING DEPTH VALUES ============================================================

    def depth_update(self, i):
        # Changing the values in the widget
        self.depth_widget.depth_nb.display(self.depth.data_import[i])
        
        # The background image
        self.depth_widget.depth_boat.setPixmap(QtGui.QPixmap("Helmsman/Helmsman/depth.png"))
        
        #Displaying the window
        self.depth_window.show()
        
        #Checking the value in Python's console
        print(f"depth.data_import = {self.depth.data_import[i]}")


    def depth_display_and_update(self):
        self.depth_widget.setupUi(self.depth_window)
        self.correct_slot = self.depth_update
        self.depth_update(0)
        self.depth_window.show()
        QtWidgets.QApplication.processEvents()
        self.updating_value.emit_signal()





#=============================================================================================================
#==============================================================================================================

class Wingsman(CrewMate):

    def __init__(self, wind_angles, wind_speed, speed, wing_angles) : 
        super().__init__(wind_angles, wind_speed, speed)
        self.wing_angles= wing_angles

        # Window for wingsman menu
        self.main_window_wingsman = QtWidgets.QMainWindow()
        self.ui_wingsman = WingMenu.Ui_MainWindowWingsman()
        self.ui_wingsman.setupUi(self.main_window_wingsman)

        # Widgets for helmsman and their windows
        self.wing_angles_window = QtWidgets.QMainWindow()
        self.wing_angles_widget = CrewWingAngles.Ui_wing_angles()

        # Windows managment
        self.list_of_windows = [self.wing_angles_window,
                                self.wind_angles_window,
                                self.wind_speed_window,
                                self.boat_speed_window]

    
    def from_pandas(self, dataframe):
        super().from_pandas(dataframe)
        self.wing_angles = Data.WingAngles.from_pandas(dataframe)

    @staticmethod
    def init_from_pandas(dataframe) :
        Wings = Wingsman(0, 0, 0, 0)
        Wings.from_pandas(dataframe)
        return Wings


#UPDATING WING ANGLES======================================

    def wing_angles_update(self, i):
        
        # Changing the values in the widget
        self.wing_angles_widget.camber_nb.display(self.speed.data_import[i][1])
        self.wing_angles_widget.twisting1_nb.display(self.wing_angles.data_import[i][0])
        self.wing_angles_widget.twisting2_nb.display(self.wing_angles.data_import[i][1])
        self.wing_angles_widget.camber_nb.display(self.wing_angles.data_import[i][2])
        
        #Displaying the window
        self.wing_angles_window.show()
        
        #Checking the value in Python's console
        print(f"wing_angles.data_import = {self.wing_angles.data_import[i][1]}")

    def wing_angles_display_and_update(self):
        self.wing_angles_widget.setupUi(self.wing_angles_window)
        self.correct_slot = self.wing_angles_update
        self.wing_angles_update(0)
        QtWidgets.QApplication.processEvents()
        self.wing_angles_window.show()
        self.updating_value.emit_signal()




