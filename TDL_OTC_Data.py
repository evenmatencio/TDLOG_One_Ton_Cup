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

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe["Latitude", 'Longitude']
        return BoatGPSCoordinates(data_import)



class Depth(OneTonCupData):
    def __init__(self, data_import):
        super().__init__()
        self.data_import = data_import

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






