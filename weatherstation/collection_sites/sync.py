"""
Description: Sync Data Files from Pi with models

"""

from models import *
from datetime import datetime
import os

def getAllData(sitenm):
    """
    Get Data from all sensors
    """
    data = []

    for sensor in Sensor.objects.all():
        data.append(getDataObjects(sensor.dataType, sitenm))
    
    return data

def getDataObjects(data_type, sitenm):
    """
    Collect data of specified type and return a list of unparsed data items
    """
    sensor_data = []

    for root, dirs, files in os.walk("/home/ubuntu/weatherStationProject/test_data/"+data_type):
        for f in files:
            print "Getting data from file" + str(f)
            with open(os.path.join(root, f), 'r') as f0:
                for line in f0:
                    pos = line.rfind('_')
                    ts = datetime.strptime(line[:pos-1], '%Y_%j_%H_%M_%S')
            
                    sensor_data.append((WeatherData(sitename=sitenm, timestamp=ts, value=line[pos+1:], dataType=data_type)).save())

    return sensor_data

