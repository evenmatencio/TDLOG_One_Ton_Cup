import os
import pandas
from queue import Queue

""" This module contains the parent Data class for the OTC software project
 and the subclasses related to the different data used in the software """


class OneTonCupData:
    def __init__(self):
        self.data_table = Queue(maxsize=0)

    def load_data(self):
        return self.data_table.full


class BoatGPSCoordinates(OneTonCupData):
    def __init__(self, data_import):
        super().__init__()
        self.data_import = data_import

    @staticmethod
    def from_pandas(dataframe):
        data_import=dataframe["Latitude", "Longitude"]
        return BoatGPSCoordinates(data_import)

class Depth(OneTonCupData):
    def __init__(self, data_import):
        super().__init__()
        self.data_import = data_import

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe["Profondeur"]
        return BoatGPSCoordinates(data_import)


class Cap(OneTonCupData):
    def __init__(self, data_import):
        super().__init__()
        self.data_import = data_import

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe["Cap"]
        return BoatGPSCoordinates(data_import)


class RoadDeviation(OneTonCupData):
    def __init__(self, data_import):
        super().__init__()
        self.data_import = data_import

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe["Ecart a la route"]
        return BoatGPSCoordinates(data_import)


class BoatAngles(OneTonCupData):
    def __init__(self, data_import):
        super().__init__()
        self.data_import = data_import

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe["Angle de gite","Angle de tangage"]
        return BoatGPSCoordinates(data_import)


class Speeds(OneTonCupData):
    def __init__(self, data_import):
        super().__init__()
        self.data_import = data_import

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe["Vitesse bateau", "VMG"]
        return BoatGPSCoordinates(data_import)

class FlightHeight(OneTonCupData):
    def __init__(self, data_import):
        super().__init__()
        self.data_import = data_import

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe["Hauteur de vol"]
        return BoatGPSCoordinates(data_import)

class WingAngles(OneTonCupData):
    def __init__(self, data_import):
        super().__init__()
        self.data_import = data_import

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe["Vrillage angle 1","Vrillage angle 2","Cambrure aile"]
        return BoatGPSCoordinates(data_import)

class WindAngles(OneTonCupData):
    def __init__(self, data_import):
        super().__init__()
        self.data_import = data_import

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe["Angle au vent reel","Angle au vent apparent"]
        return BoatGPSCoordinates(data_import)

class WindSpeed(OneTonCupData):
    def __init__(self, data_import):
        super().__init__()
        self.data_import = data_import

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe["Vitesse du vent","Beaufort"]
        return BoatGPSCoordinates(data_import)

class Pressure(OneTonCupData):
    def __init__(self, data_import):
        super().__init__()
        self.data_import = data_import

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe["Pression atmospherique"]
        return BoatGPSCoordinates(data_import)

coord_test = BoatGPSCoordinates()
coord_test.load_data()

coord_test.load_data()


coord_test = BoatGPSCoordinates()
coord_test.load_data()

print(coord_test.data_import)
