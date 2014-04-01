"""

Description: generated data for testing purposes

"""
frome import datetime, timedelta
import random

def solarData(years=0, days=1, hours=0, minutes=0, seconds=0, interval=12):
    """
    Generate data
    param: interval is in hours
    """
    t_now = datetime.now()
    file_name = 'temperature/'+t_now.strftime("%Y_%j_%H_%M_%S_")
    data = []

    #Data file (.csv) is created for collection
    for b in range(0, days+1):
        d = t_now.day+b
        if b <= 0:
            data.append((t_now+timedelta(days=d)).strftime("%Y_%j_%H_%M_%S_")+str(random.randrange(60, 75)))
        for c in range(0, hours+1, interval):
            h = t_now.hour+c
            if c <= 0:
                data.append((t_now+timedelta(hours=h)).strftime("%Y_%j_%H_%M_%S_")+str(random.randrange(60, 75)))
            for d in range(0, minutes+1):
                m = t_now.minute+d
                if d <= 0:
                    data.append((t_now+timedelta(minutes=m)).strftime("%Y_%j_%H_%M_%S_")+str(random.randrange(60, 75)))
                for e in range(0, seconds+1):
                    s = t_now.second+e
                    if e <= 0:
                        data.append((t_now+timedelta(seconds=s)).strftime("%Y_%j_%H_%M_%S_")+str(random.randrange(60, 75)))
    
    #with open(file_name, "w+") as f:
    #    f.writelines(data)

    return data
        

def windData():
    pass

def rainfallData():
    pass

def pressureData():
    pass
