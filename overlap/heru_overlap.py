import time
import sys
import numpy as np
start_time = time.time()
COVERAGE = 100
ENERGY = int(sys.argv[1]) #TODO
FILE_NAME = sys.argv[2]

def getDistance(point1,point2):
    return np.sqrt((point1.x-point2.x)**2 + (point1.y-point2.y)**2)

class Sensor():
    def __init__(self,x,y,data_volume):
        self.x = x
        self.y = y
        self.data_volume = data_volume
        self.INIT_DATA_VOLUME = data_volume
        self.stop_points = []
    def __lt__(self, other):

        return self.data_volume<other.data_volume

    def __le__(self, other):
        return self.data_volume <= other.data_volume

    def __eq__(self, other):
        return self.data_volume == other.data_volume

    def __ne__(self, other):
        return self.data_volume != other.data_volume

    def __gt__(self, other):

        return self.data_volume > other.data_volume

    def __ge__(self, other):
        return self.data_volume >= other.data_volume

class StopPoint():
    def __init__(self,x,y,sensors):
        self.x = x
        self.y = y
        self.total_data = 0
        self.sensors = []
        self.hoveringtime = 0
        for sensor in sensors:
            if getDistance(sensor,self) <= COVERAGE:
                self.sensors.append(sensor)
                sensor.stop_points.append(self)
                self.total_data += sensor.data_volume
        self.collected_data = 0

    def collect_data(self):
        for sensor_ in self.sensors:  # for each sensor in range
            for stop_point_ in sensor_.stop_points:  # find all stoppoints who have this sensor\
                stop_point_.sensors.remove(sensor_)  # TODO bug here remove this sensor from their sensors
                stop_point_.total_data -= sensor_.data_volume  # recalculate.
            sensor_.data_volume = 0

    def __lt__(self, other):

        return self.total_data<other.total_data

    def __le__(self, other):
        return self.total_data <= other.total_data

    def __eq__(self, other):
        return self.total_data == other.total_data

    def __ne__(self, other):
        return self.total_data != other.total_data

    def __gt__(self, other):

        return self.total_data > other.total_data

    def __ge__(self, other):
        return self.total_data >= other.total_data
# load sensors from .txt file


sensors = []
stop_points = []

with open(FILE_NAME) as f:
    for line in f.readlines():
        words = line.split()
        sensor = Sensor(float(words[0]),float(words[1]),int(words[2]))  # format x, y, datavolume
        sensors.append(sensor)
# set stoppoints. distance 100.


for i in range(0,1001,100):
    for j in range(0,1001,100):
        stop_point = StopPoint(i,j,sensors)
        stop_points.append(stop_point)




energy = 0
collected_data = 0
while energy < ENERGY:
    stop_point  = max(stop_points)
    #print(stop_point.total_data)
    collected_data += stop_point.total_data
    energy += max(stop_point.sensors).data_volume
    if energy > ENERGY:

        diff = ENERGY - (energy - max(stop_point.sensors).data_volume) # The last time rest energy
        for sensor in stop_point.sensors:
            if sensor.data_volume > diff: # use more energy.
                collected_data -= sensor.data_volume-diff #
        break
    stop_point.collect_data()


print("{},{},{}".format(FILE_NAME,collected_data,time.time() - start_time))