"""

    Description: This class stores sensor object

"""

import settings

class Sensor():
    """
        Holds all sensor options and data
    """

    def __init__(self, param_list=None,name=None, input_pin=None, channel=None, data_rate=None,collection_freq=None, read_time=None, write_file=None, lastCollectionTime=None):
        """
            Constructor creates all sensor objects
        """ 

        self.param_list = param_list

        # THERE IS A BETTER WAY TO DO THIS --- FIX ME PLEASE
        if self.param_list != None:
            print "Initializing settings from list"
            self.name               = self.param_list[0]
            self.input_pin          = self.param_list[1]
            self.channel            = self.param_list[2]
            self.data_rate          = self.param_list[3]
            self.collection_freq    = self.param_list[4]
            self.read_time          = self.param_list[5]
            self.write_file         = self.param_list[6]
            self.lastCollectionTime = self.param_list[7]

    def setLastCollectionTime(t):
        self.lastCollectionTime = t

    def getLastCollectionTime():
        return self.lastCollectionTime

    def ShowAllSettings():
        pass
