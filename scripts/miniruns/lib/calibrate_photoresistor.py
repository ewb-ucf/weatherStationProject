"""

Calibrates Photoresistor

"""
import RPi.GPIO as GPIO, time, os, numpy

DEBUG = 1   
GPIO.setmode(GPIO.BCM)

def data_pt_collection(RCpin):
        reading = 0
        GPIO.setup(RCpin, GPIO.OUT)
        GPIO.output(RCpin, GPIO.LOW)
        time.sleep(0.1)

        GPIO.setup(RCpin,GPIO.IN)
        while (GPIO.input(RCpin) == GPIO.LOW):
                reading += 1
        return reading
    
    
def main():

    calibrate_again = 1
    
    calibration_list = []
    average_list = []
    """calibration_list_0 = []
    calibration_list_1 = []
    calibration_list_2 = []
    calibration_list_3 = []
    """
    # y = mx + b
    b = 0
    a_list = [] 
    while calibrate_again == 1:
        period = float(raw_input("Enter a calibration period (in seconds): "))
        condition = int(raw_input( "Label your calibration condition (in lumens): "))

        last_input = raw_input("Last input (y or n): ")

        if last_input == 'y':
            calibrate_again = 0            
        if last_input == 'n':
            calibrate_again = 1
            
        start = time.time()
        tdelta = 0.0
        data_points = []
        while tdelta <= period:
            #apend data to a list.
            data_points.append(data_pt_collection(18))
            """if condition == 0:
                calibration_list_0.append(data_pt_collection(18))
            if condition == 1:
                calibration_list_1.append(data_pt_collection(18))      
            if condition == 2:
                calibration_list_2.append(data_pt_collection(18))
            if condition == 3:
                calibration_list_3.append(data_pt_collection(18))  
            """
            end = time.time()
            tdelta = end - start
            print tdelta

        calibration_list.append(data_points)
        """
        if condition == 0:
            calibrated_0 = numpy.average(calibration_list[0])
            b = calibrated_0
            print calibrated_0
        if condition == 1:
            calibrated_1 = numpy.average(calibration_list_1)
            a_list.append((calibrated_1 - b) / condition)
            print calibrated_1
        if condition == 2:
            calibrated_2 = numpy.average(calibration_list_2)
            a_list.append((calibrated_2 - b) / condition)
            print calibrated_2
        if condition == 3:
            calibrated_3 = numpy.average(calibration_list_3)
            a_list.append((calibrated_3 - b) / condition)
            print calibrated_3
        """
        average_list.append(numpy.average(data_points))
        print average_list[-1]
        # a_list.append(average)
        #a = numpy.average(a_list)    

    #print "y = " + str(a) + "x + " + str(b)

if __name__ == "__main__":
    main()        
