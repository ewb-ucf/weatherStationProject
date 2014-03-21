"""

    Description: This class stores sensor object

"""

import settings

class Sensor():
    """
        Holds all sensor options and data
    """

    def __init__(self, name=None, input_pin=None, data_rate=None, collection_freq='.001', read_time='60', write_file=None, lastCollectionTime=None):
        """
            Constructor creates all sensor objects
        """ 
        self.name = name
        self.input_pin = input_pin
        self.data_rate = data_rate
        self.collection_freq = collection_freq
        self.read_time = read_time
        self.write_file = write_file
        self.lastCollectionTime = lastCollectionTime

def setLastCollectionTime(t):
    self.lastCollectionTime = t

def getLastCollectionTime():
    return self.lastCollectionTime

def ShowAllSettings():
    pass
