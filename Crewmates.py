from PyQt5 import QtCore, QtGui, QtWidgets
import TDL_OTC_Data as Data
import Helmsman.HelmsmanMenu as HelmMenu
import Helmsman.GiteWidget as HelmGite
import Helmsman.WindAnglewidget as HelmWindAngle

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
    def __init__(self, name, temperature, gps_coordinates, depth, buoy_coordinates, stream_velocity, cap,
                 road_deviation,
                 boat_angles, speed, flight_height, wing_angles, wind_angles, wind_speed, pressure):
        super().__init__(name, temperature, gps_coordinates, depth, buoy_coordinates, stream_velocity, cap,
                       road_deviation,
                       boat_angles, speed, flight_height, wing_angles, wind_angles, wind_speed)
        self.pressure = pressure
        # Window for helmsman menu
        self.main_window_helmsman = QtWidgets.QMainWindow()
        self.ui_helmsman = HelmMenu.Ui_MainWindowHelmsman()
        self.ui_helmsman.setupUi(self.main_window_helmsman)
        
        # Widgets for helmsman
        self.gite_window = QtWidgets.QMainWindow()
        self.gite_widget = HelmGite.Ui_GiteWidget()
        self.gite_widget.setupUi(self.gite_window)

        

    def from_pandas(self, dataframe):
        super().from_pandas(dataframe)
        self.pressure = Data.Pressure.from_pandas(dataframe)
        
    


    def update(self, i):
        #Ajouter les widgets des positions gps
        self.ui_helmsman.depth_widget.depth_value = self.depth[i]
        self.ui_helmsman.cap_widget.cap_value = self.cap[i]
        #Ajouter vitesse du courant
        self.ui_helmsman.wind_angles_widget.true_wind_value = self.wind_angles[0][i]
        self.ui_helmsman.wind_angles_widget.apparent_wind_value = self.wind_angles[1][i]
        self.ui_helmsman.wind_speed_widget.true_wind_angle_value = self.wind_angles[0][i]
        self.ui_helmsman.wind_speed_widget.apparent_wind_angle_value = self.wind_angles[1][i]
        self.ui_helmsman.VMG_widget.VMG_value = self.speed[1][i]
        self.ui_helmsman.boat_speed_widget.true_speed_value = self.speed[0][i]
        self.ui_helmsman.wind_speed_widget.apparent_wind_speed_value = self.speed[0][i]
        self.ui_helmsman.wind_speed_widget.beaufort_value = self.speed[1][i]

    def display(self):
        """
        - Affichage primaire des données brutes
        - print.data= donne les indices (1ere colonne), contenu de la ligne(2eme colonne), name (ex: pressure)"""

        self.road_deviation.print_data()
        self.depth.print_data()
        self.boat_coordinates.print_data()
        self.wind_angles.print_data()
        self.wind_speed.print_data()
        self.buoy_coordinates.print_data()
        self.speed.print_data()
        self.stream_velocity.print_data()


# class Foilsman(CrewMate):
#     def __init__(self, name, gps_coordinates, depth, buoy_coordinates, stream_velocity, cap,
#                  road_deviation,
#                  boat_angles, speed, flight_height, wing_angles, wind_angles, wind_speed, pressure):
#         super().__init__(self, gps_coordinates, depth, buoy_coordinates, stream_velocity, cap,
#                          road_deviation,
#                          boat_angles, speed, flight_height, wing_angles, wind_angles, wind_speed)
#
#     def display(self):
#         self.depth.print_data()
#         self.wing_angles.print_data()
#         self.wind_speed.print_data()
#         self.road_deviation.print_data()
#         self.flight_height.print_data()
#         self.buoy_coordinates.print_data()
#         self.speed.print_data()
#         self.boat_coordinates.print_data()
#
#     def update(self, i):
#         self.ui_helmsman.boat_angles_widget.value_gite = self.boat_angles[0][i]
#         self.ui_helmsman.boat_angles.value_tangage = self.boat_angles[1][i]
#
# class Wingsman(CrewMate):
#     def __init__(self, name, gps_coordinates, depth, buoy_coordinates, stream_velocity, cap,
#                  road_deviation,
#                  boat_angles, speed, flight_height, wing_angles, wind_angles, wind_speed, pressure):
#         super().__init__(self, name, gps_coordinates, depth, buoy_coordinates, stream_velocity, cap,
#                          road_deviation,
#                          boat_angles, speed, flight_height, wing_angles, wind_angles, wind_speed)
#
#     def display(self):
#         self.wing_angles.print_data()
#         self.wind_speed.print_data()
#         self.road_deviation.print_data()
#         self.buoy_coordinates.print_data()
#         self.speed.print_data()
#         self.boat_coordinates.print_data()
#
