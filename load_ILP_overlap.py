from numpy.linalg import norm
import sys
import queue as Q
import time
import numpy as np
start_time = time.time()
COVERAGE = 100
#ENERGY = int(sys.argv[1])
FILE_NAME = sys.argv[1]

def getDistance(point1,point2):
    return np.sqrt((point1.x-point2.x)**2 + (point1.y-point2.y)**2)

class Sensor():
    def __init__(self,x,y,data_volume):
        self.x = x
        self.y = y
        self.data_volume = data_volume
        self.INIT_DATA_VOLUME = data_volume
        self.stop_points = []


class StopPoint():
    def __init__(self,x,y,sensors):
        self.x = x
        self.y = y

        self.sensors = []
        for sensor in sensors:
            if getDistance(sensor,self) <= COVERAGE:
                self.sensors.append(sensor)
                sensor.stop_points.append(self)
        self.number_of_sensors = len(self.sensors)
        self.hoveringtime = 0
        self.collected_data = 0
    def collect_data(self):
        for sensor in self.sensors:  # for each sensor in range
            sensor.data_volume = sensor.data_volume - 1 # sensor data volume - 1
            if sensor.data_volume == 0:  # if no more data
                for stop_point in sensor.stop_points:  # find all stoppoints who have this sensor
                    stop_point.sensors.remove(sensor)  # remove this sensor from their sensors
                    stop_point.number_of_sensors = len(stop_point.sensors)  # recalculate.

    def __lt__(self, other):

        return self.number_of_sensors<other.number_of_sensors

    def __le__(self, other):
        return self.number_of_sensors <= other.number_of_sensors

    def __eq__(self, other):
        return self.number_of_sensors == other.number_of_sensors

    def __ne__(self, other):
        return self.number_of_sensors != other.number_of_sensor

    def __gt__(self, other):

        return self.number_of_sensors > other.number_of_sensors

    def __ge__(self, other):
        return self.number_of_sensors >= other.number_of_sensors


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


in_range = np.zeros((len(sensors),len(stop_points)))
for i in range(len(sensors)):
    for j in range(len(stop_points)):
        if sensors[i] in stop_points[j].sensors:
            in_range[i,j] = 1

data_volumes = [sensor.data_volume for sensor in sensors]