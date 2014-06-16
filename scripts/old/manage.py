"""

   Description: This script runs when the pi is turned on and
    1) reads and stores data from sensors according to "settings.py"
    2) creates logs based on how data is collected

"""

import Sensor, settings
import logging, os, datetime, time
import RPi.GPIO as GPIO 

def activateAllSensors():
    """
        Activate collect() at appropriate times (and log)
    """

    sensorsList = []

    #Create sensor objects from settings.py dictionary
    for sensor in settings.SENSORS.items():
         sensorsList.append(
            Sensor.Sensor( name = sensor[1].get('NAME'),
                    input_pin = sensor[1].get('INPUT_PIN'),
                    data_rate = sensor[1].get('DATA_RATE'),
                    collection_freq = sensor[1].get('COLLECTION_FREQUENCY'),
                    read_time = sensor[1].get('READ_TIME'),
                    write_file = sensor[1].get('WRITE_FILE')
                )
           )

    #log

    return sensorsList
   
def startSensors(sensors):
    """
        Start running the sensor
    """
    while True:
        for sensor in sensors:
            if sensor.lastCollectionTime == None:
                collect(sensor)
            elif(time.time() - sensor.lastCollectionTime) >= (sensor.collection_freq)*(3600):
                collect(sensor)

def collect(sensor):
    """
    Collect data from sensor (and log)
    """

    #Fix me: we probably dont need to set these up each time
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(int(sensor.input_pin), GPIO.IN)

    #Collect data for appropriate window time and create collection file
    start = datetime.datetime.utcnow()

    s = []

    while ( (datetime.datetime.utcnow() - start) < datetime.timedelta(seconds=(float(sensor.read_time))) ):
        s.append(os.path.join(time.strftime("%Y_%j_%H_%M_%S_"), str(GPIO.input(int(sensor.input_pin)))))

    with open(os.path.join(sensor.write_file, time.strftime("%Y_%j_%H_%M_%S_")), 'w+') as file:
        file.writelines("%s\n" % item for item in s)

    sensor.lastCollectionTime = time.time()
