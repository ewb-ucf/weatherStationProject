"""
    Description: program that runs the temperature sensor script as a separate
                 process
"""

import datetime,time,os,logging
from lib.Adafruit_BMP085 import BMP085
from lib import settings

#Set the log level here (INFO, DEBUG, etc)
logging.basicConfig(filename="log/run_temperature_sensor.log")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#Create a file handler
handler = logging.FileHandler(os.path.basename(__file__))
handler.setLevel(logging.INFO)

logger.addHandler(handler)

last_collection_time = None


def test_temperature_sensor():
    """ 
    This function test and logs all the temperature sensor of the weatherstation to make
    sure that it is properly initialized, and collecting the correct set ofdata.
    In case of an error, an error message is displayed, explaining the type of
    error and the steps needed to correct said error will be.
    """
    channel = 0x77
    sensor = BMP085(channel)

    logger.info("...testing temperature sensor")

    try: 
        #WAIT!!! your hPaC initialization need to be put here :)
        temperature = sensor.readTemperature()
        logger.debug("**Temperature sensor activated.")
        return sensor

    except:
        logger.error("Pressure sensor failed to initialize.")
        logger.error("Please check your connection and try again.")
        return False



def collect_to_file(sensor):
    """
    This function defines the sensor, sets it's channel, the collection
    frequency, and the output file location. Once this is done, the date and
    data are respectively saved as strings.
    """
    temperature_settings = settings.SENSORS.get("TEMPERATURE")

    frequency = float(temperature_settings[1][1])
    period = float( temperature_settings[2][1])
    last_collection_time = temperature_settings[4][1]

    while 1: 
        s = []
        count = 0 
        logger.info("collecting")
    
        while(count <= period):
            s.append(os.path.join(time.strftime("%Y_%j_%H_%M_%S_"),str(sensor.readTemperature())))
            time.sleep(1)
            count = count + 1
            print count
    
        write_to_file(s)
        logger.info("done counting")
        last_collection_time = datetime.datetime.utcnow()
        logger.info( last_collection_time)
        time.sleep(frequency)

    return True


def write_to_file(s):
   
    logger.info("Writing to file.....")
    temperature_settings = settings.SENSORS.get("TEMPERATURE")
    write_file = temperature_settings[3][1]
    
    with open(os.path.join(write_file,time.strftime("%Y_%j_%H_%M_%S_")),'w+') as file:
        file.writelines("%s\n" % item for item in s)
        file.close()    
 
    return True

def main():
    """
    
    """

    #Collect data every 'freq' for 'period'
    b = test_temperature_sensor()
    if b:
        collect_to_file(b)
    else:
        logger.error("something is wrong")

if __name__=="__main__":
    main()
...testing temperature sensor
collecting
