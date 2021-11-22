import os
import pandas
from queue import Queue

""" This module contains the parent Data class for the OTC software project
 and the subclasses related to the different data used in the software """


class OneTonCupData:
    def __init__(self):
        self.data_table = Queue(maxsize=0)
        self.data_import = None

    def load_data(self):
        return self.data_table.full

    def print_data(self):
        print(self.data_import)


dataframe = pandas.read_csv(os.getcwd() + '/Random_data.csv', delimiter=',', header=0)


class BoatGPSCoordinates(OneTonCupData):
    def __init__(self, data_import):
        super().__init__()
        self.data_import = data_import
<<<<<<< HEAD

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe["Latitude", 'Longitude']
        return BoatGPSCoordinates(data_import)


=======

    @staticmethod
    def from_pandas(dataframe):
        data_import=dataframe["Latitude", "Longitude"]
        return BoatGPSCoordinates(data_import)
>>>>>>> ea42a034f92ee6be35ff71945b038ec0b743f740

class Depth(OneTonCupData):
    def __init__(self, data_import):
        super().__init__()
        self.data_import = data_import
<<<<<<< HEAD

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe["Profondeur"]
        return Depth(data_import)



class BuoyCoordinates(OneTonCupData):
    def __int__(self, data_import):
        super().__init__()
        self.data_import = data_import

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe['Latitude bouee 1', 'Longitude bouee 1', 'Latitude bouee 2', 'Longitude bouee 2',
                                'Latitude bouee 3', 'Longitude bouee 3', 'Latitude bouee 4', 'Longitude bouee 4']
        return BuoyCoordinates(data_import)



class Temperature(OneTonCupData):
    def __init__(self, data_import):
        super().__init__()
        self.data_import = data_import

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe['Temperature']
        return Temperature(data_import)


class StreamVelocity(OneTonCupData):
    def __init__(self, data_import):
        super().__init__()
        self.data_import = data_import

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe['Vitesse courant']
        return StreamVelocity(data_import)

=======

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
>>>>>>> ea42a034f92ee6be35ff71945b038ec0b743f740





