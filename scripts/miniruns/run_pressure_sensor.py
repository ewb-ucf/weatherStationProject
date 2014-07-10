"""
    Description: program that runs the pressure sensor script as a separate
                 process
"""

__author__="Sebastien Benoit"

import datetime,time,os,logging
from lib.Adafruit_BMP085 import BMP085
from lib import settings

#Set the log level here (INFO, DEBUG, etc)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#Create a file handler
handler = logging.FileHandler("log/run_pressure_sensor.log")
handler.setLevel(logging.INFO)

logger.addHandler(handler)


last_collection_time = None

def test_pressure_sensor():
    """ 
    This function test and logs all the sensors of the weatherstation to make
    sure that they are properly initialized, and collecting the correct set of data.
    In case of an error, an error message specifying the defective sensor,and 
    explaining the type of error and the steps needed to correct said error will
    be displayed.
    """
    channel = 0x77
    sensor = BMP085(0x77)

    logger.info("...testing pressure sensor")

    try: 
        #WAIT!!! your hPaC initialization need to be put here :)
        pressure = sensor.readPressure()
        logger.debug("**Pressure sensor activated.")
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
    pressure_settings = settings.SENSORS.get("PRESSURE")

    frequency =float( pressure_settings[1][1])
    period =float( pressure_settings[2][1])
    last_collection_time = pressure_settings[4][1]


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
    pressure_settings = settings.SENSORS.get("PRESSURE")
    write_file = pressure_settings[3][1]
     
    with open(os.path.join(write_file,time.strftime("%Y_%j_%H_%M_%S_")),'w+') as file:
        file.writelines("%s\n" % item for item in s)
        file.close()
 
    return True


def main():
    """
    Start running data collection program   

    """

    #Collect data every 'freq' for 'period'
    b = test_pressure_sensor()
    if b:
        collect_to_file(b)
    else:
       logger.error("something is wrong")

if __name__=="__main__":
   main()

