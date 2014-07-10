"""
    Description: program that runs the pressure sensor script as a separate
                 process
"""

__author__="Sebastien Benoit"

import datetime,time,os,logging
import RPi.GPIO as GPIO
from lib import settings

#Set the log level here (INFO, DEBUG, etc)
logging.basicConfig(filename="log/run_solar_radiation_sensor.log")
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#Create a file handler
handler = logging.FileHandler(os.path.basename(__file__))
handler.setLevel(logging.INFO)

logger.addHandler(handler)


last_collection_time = None

GPIO.setmode(GPIO.BCM)

def test_solar_radiation_sensor():
    """ 
    This function test and logs all the sensors of the weatherstation to make
    sure that they are properly initialized, and collecting the correct set of data.
    In case of an error, an error message specifying the defective sensor,and 
    explaining the type of error and the steps needed to correct said error will
    be displayed.
    """
    channel = 0x77
    sensor = GPIO

    logger.info("...testing photo resistor")

    try: 
        #WAIT!!! your hPaC initialization need to be put here :)
        solar_radiation = sensor.readPressure()
        logger.debug("**Photo resistor activated.")
        return sensor

    except:
        logger.error("Photo resistor failed to initialize.")
        logger.error("Please check your connection and try again.")
        return False

def collect_to_file(sensor):
    """
    This function defines the sensor, sets it's channel, the collection
    frequency, and the output file location. Once this is done, the date and
    data are respectively saved as strings.
    """
    solar_radiation_settings = settings.SENSORS.get("SOLAR_RADIATION")

    frequency =float( solar_radiation_settings[1][1])
    period =float( solar_radiation_settings[2][1])
    last_collection_time = solar_radiation_settings[4][1]


    while 1: 
        s = []
        count = 0 
        logger.info("collecting")
    
        while(count <= period):
            s.append(os.path.join(time.strftime("%Y_%j_%H_%M_%S_"),str(sensor.readPressure())))
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
    solar_radiation_settings = settings.SENSORS.get("SOLAR_RADIATION")
    write_file = solar_radiation_settings[3][1]
     
    with open(os.path.join(write_file,time.strftime("%Y_%j_%H_%M_%S_")),'w+') as file:
        file.writelines("%s\n" % item for item in s)
        file.close()
 
    return True


def main():
    """
    Start running data collection program   

    """

    #Collect data every 'freq' for 'period'
    b = test_solar_radiation_sensor()
    if b:
        collect_to_file(b)
    else:
       logger.error("something is wrong")

if __name__=="__main__":
   main()
