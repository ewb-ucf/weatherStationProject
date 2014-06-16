"""

Description  : The purpose of this file is to initialize all the sensors, test and
             : make sure they are properly working.
             : Once this is done, the sensors are  set to collect the appropriate
             : data at  intervals and frequencies set by the file named "settings.py".
         

"""
"""
__author__ = 'Sebastien Benoit'
__date_modified__ = '06/01/2014' 
"""

#import settings,Sensor
from Adafruit_BMP085 import BMP085   
 
def initialize_sensors():
    """
    This function initialize all sensors of the weatherstation, and set them 
    ready to collect and save the data collected.
    """
    initialize_pressure_temperature_sensor()
    
    # iniitialie_temperature()
    # initialize_solar_radiation()
    # initialize_wind()
    # initialize_raim()
    # initialize_GPS()

    return 
    
def initialize_pressure_temperature_sensor():
    
    channel = 0x77
    hPaC    = BMP085(channel)
    return hPaC

def initialize_solar_radiation_sensor():
    """
    set the input pin,names, and return value.
    """
    pass

def initialize_wind_rain_sensor():
    """
    set input pin, name, ad return value.
    """
    pass

#------------------------------------------------------------------------------
#---------------------------------Test Chapter---------------------------------
#------------------------------------------------------------------------------

def test_sensors():
    test_pressure_temperature_sensor()
    # test_solar_radiation_sensor()
    #test_wind_rain_sensor()
    #test_GPS_module()

def test_pressure_temperature_sensor(hPaC):
    """
    This function test and logs all the sensors of the weatherstation to make sure that
    they are properly initialized, and collecting the correct set of data. In
    case of error, an error message specifying the defective sensor,and 
    explaining the type of error and the steps needed to correct said error will
    be displayed.
    """

    print "Please wait while I verify the pressure and temperature sensor..."
    print "..............."
    print "........."
    try: 

        temp = hPaC.readTemperature()
        print "Temperature sensor activated."
        pressure = hPaC.readPressure()
        print "Pressure sensor activated."

    except:
        print "Pressure and Temperature sensor failed to initialize." 
        print "Please check your connection and try again."


def test_solar_radiation_sensor():
    
    """
    test the solar rad sensor
    """
    pass    

def test_wind_rain_sensor():
    """
    test  wind and rain sensor
    """    
    pass

def test_GPS_module():
    """
    make sure GPS reads proper data
    """
    pass

#------------------------------------------------------------------------------
#-----------------------Collection-Chapter-------------------------------------
#------------------------------------------------------------------------------
'
def collect_data():
    collect_pressure_data()
    collect_temperature_data()
    collect_solar_radiation_data()
    collect_rain_data()
    collect_wind_data()
    collect_GPS_data()
    pass

def collect_pressure_data(hPaC):
    """
    collect the data at a predifined frequencyand period.it then saves to its
    assigned folder.(see settings file for modifications.)
    """
    pressure = hPaC.readPressure()
    print "The current Atmospheric Pressure is: %.2f hpa" % (pressure/ 100)
    
   
def collect_temperature_data(hPaC):
    """
    see above for description, pero cambiar el nombre.
    """
    temp = hPaC.readTemperature()
    print "The current local Temperature is : %.2f C" % temp
    

def collect_solar_radiation_data():
    """
    bis
    """
    pass

def collect_rain_data():
    """
    bis
    """
    pass
    
def collect_wind_data():
    """
    bis
    """
    pass    

def collect_GPS_data():
    """
    bis
    """
    pass
'
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------

def main():
    """
    This function call all the necessary functions in the order needed to
    properly run the weatherstation.
    """
    
    b = initialize_pressure_temperature_sensor()
    test_pressure_temperature_sensor(b)
    collect_pressure_data(b)
    collect_temperature_data(b)
    # start_collection()
    print "Got thru main" 

if __name__=="__main__":
    main()
