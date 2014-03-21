"""

    Description: This file is where you set and change ports,
    set collection rates, etc

"""

import os

DEBUG = True

SITE_NAME = ""
BASE_DIR = os.getcwd()
DATA_DIR = os.path.join(BASE_DIR, '../data')


#Uncomment the sensors that you are collecting from and add
#appropriate ports ALSO!!! add to the list of active sensors

SENSORS = {

           'TEMPERATURE': { 
                            'NAME'     : 'temperature',
                            'INPUT_PIN': '7',
                            'DATA_RATE': None,
                            'COLLECTION_FREQUENCY': '.001', #reads/hr
                            'READ_TIME': '60', #seconds
                            'WRITE_FILE': os.path.join(DATA_DIR, 'temperature'), 
                          },

            'PRESSURE':   {
                            'NAME'     : "pressure",
                            'INPUT_PIN': '7',
                            'DATA_RATE': None,
                            'COLLECTION_FREQUENCY': '.001', #reads/hr
                            'READ_TIME': '30', #seconds
                            'WRITE_FILE': os.path.join(DATA_DIR, 'pressure'), 
                          } 
}
