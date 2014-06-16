"""

Description  : The purpose of this file is to initialize all the sensors, test and
             : make sure they are properly working.
             : Once this is done, the sensors are  set to collect the appropriate
             : data at  intervals and frequencies set by the file named "settings.py".
         

"""

__author__ ="Sebastien Benoit"
__date__ = "06/01/2014"


from Adafruit_BMP085 import BMP085   
import logging, os

#Set the log level here (INFO, DEBUG, etc)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

#Create a file handler
handler = logging.FileHandler(os.path.basename(__file__))
handler.setLevel(logging.INFO)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(messages)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
 
def initialize_sensors():
    """
    This function initializes and tests all sensors of the weatherstation.
    """

    pass = True

    logger.info("Initializing and testing sensors...")
    
    if test_pressure_temperature_sensor():
        logger.info("pressure_temperature sensor test successfully")
    else:
        logger.error("pressure_temperature sensor test not successful")
   
    if pass == True:
        logger.info("ALL PRELIM SENSOR TESTS PASSED") 
    if pass == False:
        logger.error("NOT ALL SENSOR TESTS PASSED")
    
    return pass
    

#------------------------------------------------------------------------------
#---------------------------------Test Chapter---------------------------------
#------------------------------------------------------------------------------

def test_pressure_temperature_sensor():
    """
    This function test and logs all the sensors of the weatherstation to make sure that
    they are properly initialized, and collecting the correct set of data. In
    case of error, an error message specifying the defective sensor,and 
    explaining the type of error and the steps needed to correct said error will
    be displayed.
    """

    logger.info("...testing pressure_temperature sensor")

    try: 
        #WAIT!!! your hPaC initialization need to be put here :)
        temp = hPaC.readTemperature()
        logger.debug("**Temperature sensor activated.")
        pressure = hPaC.readPressure()
        logger.debug("**Pressure sensor activated.")
        return True

    except:
        logger.error("Pressure and Temperature sensor failed to initialize.")
        logger.error("Please check your connection and try again.")


def test_solar_radiation_sensor(): 
    """
    test the solar rad sensor
    """
    logger.info("...testing solar_radiation sensor")
    pass    

def test_wind_rain_sensor():
    """
    test  wind and rain sensor
    """    
    logger.info("...testing wind_rain sensor")

    pass

def test_GPS_module():
    """
    make sure GPS reads proper data
    """
    logger.info("...testing GPS module sensor")

    pass

#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def main():
    """
    This function call all the necessary functions in the order needed to
    properly run the weatherstation.
    """

    logger.info("STARTING TO INITIALIZE AND RUN TESTS")
    
    b = initialize_pressure_temperature_sensor()
    test_pressure_temperature_sensor(b)


if __name__=="__main__":
    main()
