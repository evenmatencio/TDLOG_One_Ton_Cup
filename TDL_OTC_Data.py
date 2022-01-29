from queue import Queue

""" This module contains the parent Data class for the OTC software project
 and the subclasses related to the different data used in the software """


class OneTonCupData:
    def __init__(self, data_import):
        self.data_import = data_import


class BoatGPSCoordinates(OneTonCupData):
    def __init__(self, data_import):
        super().__init__(data_import)

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe[['Longitude', 'Latitude']]
        return BoatGPSCoordinates(data_import)


class Depth(OneTonCupData):
    def __init__(self, data_import):
        super().__init__(data_import)

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe["Profondeur"]
        return Depth(data_import)


class BuoyCoordinates(OneTonCupData):
    def __init__(self, data_import):
        super().__init__(data_import)

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe[['Latitude bouee 1', 'Longitude bouee 1', 'Latitude bouee 2', 'Longitude bouee 2',
                                 'Latitude bouee 3', 'Longitude bouee 3', 'Latitude bouee 4', 'Longitude bouee 4']]
        return BuoyCoordinates(data_import)


class Temperature(OneTonCupData):
    def __init__(self, data_import):
        super().__init__(data_import)

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe["Temperature"]
        return Temperature(data_import)


class StreamVelocity(OneTonCupData):
    def __init__(self, data_import):
        super().__init__(data_import)

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe["Vitesse courant"]
        return StreamVelocity(data_import)


class Cap(OneTonCupData):
    def __init__(self, data_import):
        super().__init__(data_import)

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe["Cap"]
        return Cap(data_import)


class RoadDeviation(OneTonCupData):
    def __init__(self, data_import):
        super().__init__(data_import)

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe["Ecart a la route"]
        return RoadDeviation(data_import)


class BoatAngles(OneTonCupData):
    def __init__(self, data_import):
        super().__init__(data_import)

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe[["Angle de gite", "Angle de tangage"]]
        return BoatAngles(data_import)


class Speeds(OneTonCupData):
    def __init__(self, data_import):
        super().__init__(data_import)

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe[["Vitesse bateau", "VMG"]]
        return Speeds(data_import)


class FlightHeight(OneTonCupData):
    def __init__(self, data_import):
        super().__init__(data_import)

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe["Hauteur de vol"]
        return FlightHeight(data_import)


class WingAngles(OneTonCupData):
    def __init__(self, data_import):
        super().__init__(data_import)

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe[["Vrillage angle 1", "Vrillage angle 2", "Cambrure aile"]]
        return WingAngles(data_import)


class WindAngles(OneTonCupData):
    def __init__(self, data_import):
        super().__init__(data_import)

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe[["Angle au vent reel", "Angle au vent apparent"]]
        return WindAngles(data_import)


class WindSpeed(OneTonCupData):
    def __init__(self, data_import):
        super().__init__(data_import)

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe[["Vitesse du vent", "Beaufort"]]
        return WindSpeed(data_import)


class Pressure(OneTonCupData):
    def __init__(self, data_import):
        super().__init__(data_import)

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe["Pression atmospherique"]
        return Pressure(data_import)
    
class BatteryPowerLevel(OneTonCupData):
    def __init__(self, data_import):
        super().__init__(data_import)

    @staticmethod
    def from_pandas(dataframe):
        data_import = dataframe["Niveau batterie"]
        return BatteryPowerLevel(data_import)
    
