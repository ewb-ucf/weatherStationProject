"""
    Description: program that runs the temperature sensor script as a separate
                 process
"""

import settings,datetime,time,os
from Adafruit_BMP085 import BMP085

last_collection_time = None


def collect_to_file():
    """
    This function defines the sensor, sets it's channel, the collection
    frequency, and the output file location. Once this is done, the date and
    data are respectively saved as strings.
    """
    channel = 0x77
    sensor = BMP085(channel)
    temperature_settings = settings.SENSORS.get("TEMPERATURE")

    frequency = float(temperature_settings[1][1])
    period = float( temperature_settings[2][1])
    last_collection_time = temperature_settings[4][1]

    s = []
    s.append(os.path.join(time.strftime("%Y_%j_%H_%M_%S_"),str(sensor.readTemperature())))
    write_to_file(s)   
        
    while 1: 
        if ( (datetime.datetime.utcnow()-last_collection_time) >= datetime.timedelta(seconds=(frequency)) ):
            s = []
            count = 0 
            print "collecting"
    
            while(count <= period):
                s.append(os.path.join(time.strftime("%Y_%j_%H_%M_%S_"),str(sensor.readTemperature())))
                time.sleep(1)
                count = count + 1
                print count
    
            write_to_file(s)
            print "done counting"
            last_collection_time = datetime.datetime.utcnow()
            print last_collection_time

    return True

def write_to_file(s):
   
    print "Writing to file....."
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
    collect_to_file()

if __name__=="__main__":
    main()
