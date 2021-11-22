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
    def __init__(self):
        super().__init__()
        self.data_import = None

    def load_data(self):
        self.data_import = pandas.read_csv(os.getcwd() + "/Random_data.csv", delimiter=',', header=0,
                                           usecols=['Latitude', 'Longitude'])
    def print_data(self):
        print(self.data_import)

class Depth(OneTonCupData):
    def __init__(self):
        super().__init__()
        self.data_import = None

    def load_data(self):
        self.data_import = pandas.read_csv(os.getcwd() + "/Random_data.csv", delimiter=',', header=0,
                                           usecols=['Profondeur'])
    def print_data(self):
        print(self.data_import)

coord_test = BoatGPSCoordinates()
coord_test.load_data()

coord_test.load_data()


coord_test = BoatGPSCoordinates()
coord_test.load_data()

print(coord_test.data_import)
