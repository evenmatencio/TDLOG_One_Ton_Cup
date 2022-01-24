from PyQt5 import QtCore, QtGui, QtWidgets
import TDL_OTC_Data as Data
import UpdatingSignal

#Import of Helsman's widgets
import Helmsman.HelmsmanMenu as HelmMenu
import Helmsman.depth_py as CrewDepth
import Helmsman.cappy1 as CrewCap
import Helmsman.windanglespy as CrewWindAngles
import Helmsman.windspeed2 as CrewWindSpeed
import Helmsman.VMG as CrewSpeed

# #Import of Foilsman's widgets
# import Foilsman.FoilsmanMenu as FoilMenu
# import Foilsman.flight_height_py as CrewFlightHeight
# import Foilsman.gite_tangage_py as CrewGite

# #Import of Wingsman's widgets
# import Wingsman.WingsmanMenu as WingMenu
# import Wingsman.cambrure_vrillage_py as CrewWingAngles

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

    def __init__(self, name, temperature, boat_coordinates, depth, buoy_coordinates, stream_velocity, cap,
                 road_deviation,
                 boat_angles, speed, flight_height, wing_angles, wind_angles, wind_speed):
        self.name = name
        self.temperature = temperature
        self.boat_coordinates = boat_coordinates
        self.depth = depth
        self.buoy_coordinates = buoy_coordinates
        self.stream_velocity = stream_velocity
        self.cap = cap
        self.road_deviation = road_deviation
        self.boat_angles = boat_angles
        self.speed = speed
        self.flight_height = flight_height
        self.wing_angles = wing_angles
        self.wind_speed = wind_speed
        self.wind_angles = wind_angles


    def from_pandas(self, dataframe):
        self.boat_coordinates = Data.BoatGPSCoordinates.from_pandas(dataframe)
        self.depth = Data.Depth.from_pandas(dataframe)
        self.buoy_coordinates = Data.BuoyCoordinates.from_pandas(dataframe)
        self.temperature = Data.Temperature.from_pandas(dataframe)
        self.stream_velocity = Data.StreamVelocity.from_pandas(dataframe)
        self.cap = Data.Cap.from_pandas(dataframe)
        self.road_deviation = Data.RoadDeviation.from_pandas(dataframe)
        self.boat_angles = Data.BoatAngles.from_pandas(dataframe)
        self.speed = Data.Speeds.from_pandas(dataframe)
        self.flight_height = Data.FlightHeight.from_pandas(dataframe)
        self.wing_angles = Data.WingAngles.from_pandas(dataframe)
        self.wind_angles = Data.WindAngles.from_pandas(dataframe)
        self.wind_speed = Data.WindSpeed.from_pandas(dataframe)



    def display(self):
        self.road_deviation.print_data()
        self.depth.print_data()
        self.boat_coordinates.print_data()
        self.wind_angles.print_data()
        self.wind_speed.print_data()
        self.buoy_coordinates.print_data()
        self.speed.print_data()
        self.stream_velocity.print_data()
        self.depth.print_data()
        self.wing_angles.print_data()
        self.wind_speed.print_data()
        self.road_deviation.print_data()
        self.flight_height.print_data()
        self.wing_angles.print_data()
        self.wind_speed.print_data()
        self.road_deviation.print_data()


class Helmsman(CrewMate):
    
    def __init__(self, name, temperature, gps_coordinates, depth, buoy_coordinates, stream_velocity, cap, \
                 road_deviation, boat_angles, speed, flight_height, wing_angles, wind_angles, wind_speed, pressure):
        super().__init__(name, temperature, gps_coordinates, depth, buoy_coordinates, stream_velocity, cap, \
                       road_deviation, boat_angles, speed, flight_height, wing_angles, wind_angles, wind_speed)
        self.pressure = pressure
        
        # For updating values
        self.updating_value = UpdatingSignal.UpdatingValue(self)

        # Window for helmsman menu
        self.main_window_helmsman = QtWidgets.QMainWindow()
        self.ui_helmsman = HelmMenu.Ui_MainWindowHelmsman()
        self.ui_helmsman.setupUi(self.main_window_helmsman)
        

        # Widgets for helmsman and its windows
        self.cap_window = QtWidgets.QMainWindow()
        self.cap_widget = CrewCap.Ui_Cap()
        self.depth_window = QtWidgets.QMainWindow()
        self.depth_widget = CrewDepth.Ui_Depth()
        self.wind_angles_window = QtWidgets.QMainWindow()
        self.wind_angles_widget = CrewWindAngles.Ui_WindAngles()
        self.wind_speed_window = QtWidgets.QMainWindow()
        self.wind_speed_widget = CrewWindSpeed.Ui_WindSpeed()
        self.boat_speed_window = QtWidgets.QMainWindow()
        self.boat_speed_widget = CrewSpeed.Ui_VMG()
        
        
        # Widgets managment 
        self.displayed_widget = [self.depth_window,
                                 self.cap_window,
                                 self.wind_angles_window,
                                 self.wind_speed_window,
                                 self.boat_speed_window]
        
        self.correct_slot = None


    def depth_update(self, i):
        self.depth_widget.depth_nb.display(int(self.depth.data_import[i]))
        self.depth_widget.depth_boat.setPixmap(QtGui.QPixmap("Helmsman/Helmsman/depth.png"))
        self.depth_window.show()
        print(f"depth.data_import = {self.depth.data_import[i]}")


    def depth_display_and_update(self):
        self.depth_widget.setupUi(self.depth_window, int(self.depth.data_import[0]))
        self.correct_slot = self.depth_update
        self.depth_update(0)
        self.depth_window.show()
        QtWidgets.QApplication.processEvents()
        self.updating_value.emit_signal()

    
    def windspeed_update(self, i):
        #self.wind_speed_window.close()
        self.wind_speed_widget.lcdNumber.display(self.wind_speed.data_import.loc[i][0])
        self.wind_speed_widget.lcdNumber_2.display(self.wind_speed.data_import.loc[i][1])
        self.wind_speed_widget.dial.setValue(int(self.wind_speed.data_import.loc[i][0]))
        self.wind_speed_widget.label.setPixmap(QtGui.QPixmap("Helmsman/Helmsman/vitessevent.png"))
        # self.wind_speed_widget.update(self.wind_speed.data_import.loc[i])
        self.wind_speed_window.show()
        # self.updating_value.emit_signal()
        print(f"wind_speed.data_import = {self.wind_speed.data_import.loc[i]}")
 
        
    def windspeed_display_and_update(self) :
        self.wind_speed_widget.setupUi(self.wind_speed_window, self.wind_speed.data_import.loc[0])
        self.correct_slot = self.windspeed_update
        self.windspeed_update(0)
        QtWidgets.QApplication.processEvents()
        self.wind_speed_window.show()
        self.updating_value.emit_signal()
        
    
    def cap_update(self, i):
        self.cap_window.close()
        self.cap_widget.true_direction_value.display(int(self.cap.data_import[i]))
        self.cap_widget.deviation_value.display(int(self.road_deviation.data_import[i]))
        self.cap_widget.cap_picture.setPixmap(QtGui.QPixmap("Helmsman/Helmsman/roeventcap.jpg"))
        self.cap_window.show()
        print(f"cap.data_import = {self.cap.data_import[i]}")


    def depth_display_and_update(self):
        self.depth_widget.setupUi(self.depth_window, int(self.depth.data_import[0]))
        self.correct_slot = self.depth_update
        self.depth_update(0)
        self.depth_window.show()
        QtWidgets.QApplication.processEvents()
        self.updating_value.emit_signal()
        
        
        

    def from_pandas(self, dataframe):
        super().from_pandas(dataframe)
        

    def update(self, i):
        #Ajouter les coordinnées des bouées et des bateaux ?
        #Ajouter vitesse du courant (créer le widget)
        #Ajouter la vitesse du bateau dans le widget de la VMC:
        #self.ui_helmsman.boat_speed_widget.true_speed_value = self.speed[0][i]
        #Road deviation ?

        self.ui_helmsman.depth_widget.depth_value = self.depth[i]
        self.ui_helmsman.cap_widget.cap_value = self.cap[i]
        self.ui_helmsman.wind_angles_widget.true_wind_value = self.wind_angles[0][i]
        self.ui_helmsman.wind_angles_widget.apparent_wind_value = self.wind_angles[1][i]
        self.ui_helmsman.wind_speed_widget.true_wind_angle_value = self.wind_angles[0][i]
        self.ui_helmsman.wind_speed_widget.apparent_wind_angle_value = self.wind_angles[1][i]
        self.ui_helmsman.boat_speed_widget.VMG_value = self.speed[1][i]


# class Foilsman(CrewMate):
#     def __init__(self, name, gps_coordinates, depth, buoy_coordinates, stream_velocity, cap,
#                  road_deviation,
#                  boat_angles, speed, flight_height, wing_angles, wind_angles, wind_speed):
#         super().__init__(self, gps_coordinates, depth, buoy_coordinates, stream_velocity, cap,
#                          road_deviation,
#                          boat_angles, speed, flight_height, wing_angles, wind_angles, wind_speed)
#         # For updating values
#         self.updating_value = UpdatingSignal.UpdatingValue()
#         # Window for foilsman menu
#         self.main_window_foilsman = QtWidgets.QMainWindow()
#         self.ui_foilsman = FoilMenu.Ui_MainWindowHelmsman()
#         self.ui_foilsman.setupUi(self.main_window_foilsman)
#         # Widgets for foilsman and its windows
#         #Coordonnées du bateau et des bouées ?
#         #Road_deviation ?
#         #Ajouter la vitesse vraie du baetau au widget VMG
#         self.wind_angles_window = QtWidgets.QMainWindow()
#         self.wind_angles_widget = CrewWindAngles.Ui_wind_angles()
#         self.wind_speed_window = QtWidgets.QMainWindow()
#         self.wind_speed_widget = CrewWindSpeed.Ui_wind_angles()
#         self.gite_window = QtWidgets.QMainWindow()
#         self.gite_widget = CrewGite.Ui_gite_tangage()
#         self.depth_window = QtWidgets.QMainWindow()
#         self.depth_widget = CrewDepth.Ui_Depth()
#         self.flight_height_window = QtWidgets.QMainWindow()
#         self.flight_height_widget = CrewFlightHeight.Ui_Depth()
#         self.boat_speed_window = QtWidgets.QMainWindow()
#         self.boat_speed_widget = CrewSpeed.Ui_VMG()

#     def update(self, i):
#         self.ui_foilsman.gite_widget.gite_value = self.boat_angles[0][i]
#         self.ui_foilsman.gite_widget.tangage_value = self.boat_angles[1][i]
#         self.ui_foilsman.wind_angles_widget.true_wind_value = self.wind_angles[0][i]
#         self.ui_foilsman.wind_angles_widget.apparent_wind_value = self.wind_angles[1][i]
#         self.ui_foilsman.wind_speed_widget.true_wind_angle_value = self.wind_angles[0][i]
#         self.ui_foilsman.wind_speed_widget.apparent_wind_angle_value = self.wind_angles[1][i]
#         self.ui_foilsman.depth_widget.depth_value = self.depth[i]
#         self.ui_foilsman.flight_height_widget.flight_height_value = self.flight_height[i]
#         self.ui_foilsman.boat_speed_widget.VMG_value = self.speed[1][i]




# class Wingsman(CrewMate):
#     def __init__(self, name, gps_coordinates, depth, buoy_coordinates, stream_velocity, cap,
#                  road_deviation,
#                  boat_angles, speed, flight_height, wing_angles, wind_angles, wind_speed):
#         super().__init__(self, name, gps_coordinates, depth, buoy_coordinates, stream_velocity, cap,
#                          road_deviation,
#                          boat_angles, speed, flight_height, wing_angles, wind_angles, wind_speed)
#         # For updating values
#         self.updating_value = UpdatingSignal.UpdatingValue()

#         # Window for wingsman menu
#         self.main_window_wingsman = QtWidgets.QMainWindow()
#         self.ui_wingsman = WingMenu.Ui_MainWindowWingsman()
#         self.ui_wingsman.setupUi(self.main_window_wingsman)

#         # Widgets for helmsman and its windows
#         #Coordonnées du bateau et des bouées?
#         #Road deviation
#         self.boat_speed_window = QtWidgets.QMainWindow()
#         self.boat_speed_widget = CrewSpeed.Ui_VMG()
#         self.wing_angles_window = QtWidgets.QMainWindow()
#         self.wing_angles_widget = CrewWingAngles.Ui_VMG()
#         self.wind_angles_window = QtWidgets.QMainWindow()
#         self.wind_angles_widget = CrewWindAngles.Ui_wind_angles()
#         self.wind_speed_window = QtWidgets.QMainWindow()
#         self.wind_speed_widget = CrewWindSpeed.Ui_wind_angles()
#     def update(self, i):
#         self.ui_wingsman.wing_angles_widget.cambrure_value = self.wind_angles[0][i]
#         self.ui_wingsman.wing_angles_widget.vrillage_value_1 = self.wind_angles[1][i]
#         self.ui_wingsman.wing_angles_widget.vrillage_value_2 = self.wind_angles[2][i]
#         self.ui_wingsman.boat_speed_widget.VMG_value = self.speed[1][i]
#         self.ui_wingsman.wind_angles_widget.true_wind_value = self.wind_angles[0][i]
#         self.ui_wingsman.wind_angles_widget.apparent_wind_value = self.wind_angles[1][i]
#         self.ui_wingsman.wind_speed_widget.true_wind_angle_value = self.wind_angles[0][i]
#         self.ui_wingsman.wind_speed_widget.apparent_wind_angle_value = self.wind_angles[1][i]
