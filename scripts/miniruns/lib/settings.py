"""

    Description: This file is where you set and change ports,
    set collection rates, etc

"""

import os, datetime

DEBUG = True

SITE_NAME = ""
BASE_DIR = os.getcwd()
DATA_DIR = os.path.join(BASE_DIR, '../../data')


#Uncomment the sensors that you are collecting from and add
#appropriate ports ALSO!!! add to the list of active sensors

SENSORS = {

           'TEMPERATURE': [ 
                           [ 'NAME'     , 'temperature'],
                           [ 'FREQ', '20'], #read every 120 sec
                           [ 'PERIOD', '30'], #for 30 seconds
                           [ 'WRITE_FILE', os.path.join(DATA_DIR,'temperature')],
                           ['INITIAL_COLLECTION_TIME',datetime.datetime.utcnow()],
                          ],

            
              'PRESSURE': [ 
                            [ 'NAME'     , 'pressure'],
                            [ 'FREQ', '20'], #read every 120 sec
                            [ 'PERIOD', '30'], #for 30 seconds
                            [ 'WRITE_FILE', os.path.join(DATA_DIR,'pressure')], 
                            ['INITIAL_COLLECTION_TIME',datetime.datetime.utcnow()],
                           ],


          'SOLAR_RADIATION': [
                            ['NAME', 'solar_radiation'],
                            ['FREQ', '20'],
                            ['PERIOD','30'],
                            ['WRITE_FILE',os.path.join(DATA_DIR,'solar_radiation')],
                            ['INITIAL_COLLECTION_TIME',datetime.datetime.utcnow()],
                           ] 
      
}
