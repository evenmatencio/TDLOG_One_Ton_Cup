from queue import Queue
import numpy

""" This module contains the parent Data class for the OTC software project
 and the subclasses related to the different data used in the software """
 
 
 
""" Reminder : Static methods. Why?

    Static methods can be used without having to create an object of the class before. 
    
    Instead of doing :             |         We do :
    depth= Depth()                 |         Depth.from_pandas(dataframe)
    depth.from_pandas(dataframe)   |         Better !!
    
"""


class OneTonCupData:
    def __init__(self, data_import):
        self.data_import = data_import


class BoatGPSCoordinates(OneTonCupData):

    @staticmethod
    def from_pandas(dataframe):
        data_import = numpy.asarray(dataframe[['Longitude', 'Latitude']])
        return BoatGPSCoordinates(data_import)


class Depth(OneTonCupData):

    @staticmethod
    def from_pandas(dataframe):
        data_import = numpy.asarray(dataframe["Profondeur"])
        return Depth(data_import)


class BuoyCoordinates(OneTonCupData):

    @staticmethod
    def from_pandas(dataframe):
        data_import = numpy.asarray(dataframe[['Latitude bouee 1', 'Longitude bouee 1', 'Latitude bouee 2', 'Longitude bouee 2',
                                 'Latitude bouee 3', 'Longitude bouee 3', 'Latitude bouee 4', 'Longitude bouee 4']])
        return BuoyCoordinates(data_import)


class Temperature(OneTonCupData):

    @staticmethod
    def from_pandas(dataframe):
        data_import = numpy.asarray(dataframe["Temperature"])
        return Temperature(data_import)


class StreamVelocity(OneTonCupData):

    @staticmethod
    def from_pandas(dataframe):
        data_import = numpy.asarray(dataframe["Vitesse courant"])
        return StreamVelocity(data_import)


class Cap(OneTonCupData):

    @staticmethod
    def from_pandas(dataframe):
        data_import = numpy.asarray(dataframe["Cap"])
        return Cap(data_import)


class RoadDeviation(OneTonCupData):

    @staticmethod
    def from_pandas(dataframe):
        data_import = numpy.asarray(dataframe["Ecart a la route"])
        return RoadDeviation(data_import)


class BoatAngles(OneTonCupData):

    @staticmethod
    def from_pandas(dataframe):
        data_import = numpy.asarray(dataframe[["Angle de gite", "Angle de tangage"]])
        return BoatAngles(data_import)


class Speeds(OneTonCupData):

    @staticmethod
    def from_pandas(dataframe):
        data_import = numpy.asarray(dataframe[["Vitesse bateau", "VMG"]])
        return Speeds(data_import)


class FlightHeight(OneTonCupData):

    @staticmethod
    def from_pandas(dataframe):
        data_import = numpy.asarray(dataframe["Hauteur de vol"])
        return FlightHeight(data_import)


class WingAngles(OneTonCupData):

    @staticmethod
    def from_pandas(dataframe):
        data_import = numpy.asarray(dataframe[["Vrillage angle 1", "Vrillage angle 2", "Cambrure aile"]])
        return WingAngles(data_import)


class WindAngles(OneTonCupData):

    @staticmethod
    def from_pandas(dataframe):
        data_import = numpy.asarray(dataframe[["Angle au vent reel", "Angle au vent apparent"]])
        return WindAngles(data_import)


class WindSpeed(OneTonCupData):

    @staticmethod
    def from_pandas(dataframe):
        data_import = numpy.asarray(dataframe[["Vitesse du vent", "Beaufort"]])
        return WindSpeed(data_import)


class Pressure(OneTonCupData):

    @staticmethod
    def from_pandas(dataframe):
        data_import = numpy.asarray(dataframe["Pression atmospherique"])
        return Pressure(data_import)
    
class BatteryPowerLevel(OneTonCupData):

    @staticmethod
    def from_pandas(dataframe):
        data_import = numpy.asarray(dataframe["Niveau batterie"])
        return BatteryPowerLevel(data_import)
    
