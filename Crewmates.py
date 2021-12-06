import os
import pandas
from queue import Queue


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

class Crewmate():
    def __init__(self, name, dataframe):
        self.mate_name=name
        self.boat_coordinates=BoatGPSCoordinates.frompandas(dataframe)
        self.depth=Depth.frompandas(dataframe)
        self.buoy_coordinates=BuoyCoordinates.frompandas(dataframe)
        self.temperature=Temperature.frompandas(dataframe)
        self.stream_velocity=StreamVelocity.frompandas(dataframe)
        self.cap=Cap.frompandas(dataframe)
        self.road_deviation=RoadDeviation.frompandas(dataframe)
        self.boat_angles=BoatAngles.frompandas(dataframe)
        self.speed=Speed.frompandas(dataframe)
        self.flight_height=FlightHeight.frompandas(dataframe)
        self.wing_angles=WingAngles.frompandas(dataframe)
        self.wind_angles = WindAngles.frompandas(dataframe)
        self.wind_speed = WindSpeed.frompandas(dataframe)
        self.pressure=Pressure.frompandas(dataframe)


class Helmsman(Crewmate):
    def __init__(self, name, dataframe):
        super.__init__(self, name, dataframe)
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


class Foilsman(Crewmate):
    def __init__(self, name, dataframe):
        super().__init__(self, name, dataframe)
    def display(self):
        self.depth.print_data()
        self.wing_angles.print_data()
        self.wind_speed.print_data()
        self.road_deviation.print_data()
        self.flight_height.print_data()

class Wingsman(Crewmate):
    def __init__(self, name, dataframe):
        super().__init__(self, name, dataframe)
    def display(self):
        self.wing_angles.print_data()
        self.wind_speed.print_data()
        self.road_deviation.print_data()
        self.pressure.print_data()
