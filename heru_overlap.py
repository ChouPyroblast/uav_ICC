
COVERAGE = 100
ENERGY = 300
FILE_NAME = "1.txt"

def getDistance(point1,point2):
    return (point1.x-point2.x)**2 + (point1.y-point2.y)**2

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

        #self.number_of_sensors = len(self.sensors)

        self.collected_data = 0

    def collect_data(self):
        for sensor in self.sensors:  # for each sensor in range
              # sensor data volume - 1
            for stop_point in sensor.stop_points:  # find all stoppoints who have this sensor
                stop_point.sensors.remove(sensor)  # remove this sensor from their sensors
                stop_point.total_data -= sensor.data_volume  # recalculate.
            sensor.data_volume = 0
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
    collected_data +=stop_point.total_data
    energy += max(stop_point.sensors).data_volume

    stop_point.collect_data()
print(collected_data)