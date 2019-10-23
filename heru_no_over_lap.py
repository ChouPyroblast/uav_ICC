import sys
import numpy as np
import time
start_time = time.time()

stoppoints = []
max_sensor_stoppoints = 0 # record the stoppoints with maximum sensors.
Energy = int(sys.argv[1]) #TODO
Filename = sys.argv[2]

with open(Filename) as f:
    for line in f.readlines():
        sensors = line.split()
        weights = [int(x) for x in sensors]
        #weights.sort(reverse=True)
        stoppoints.append(weights)
        max_sensor_stoppoints = max(max_sensor_stoppoints,len(weights))
matrix = np.zeros((len(stoppoints),max_sensor_stoppoints))
for i in range(len(stoppoints)):
    matrix[i,:len(stoppoints[i])]=stoppoints[i]
# every row is a stop points. each element is a sensor's data volume
# non_zero_matrix = matrix > 0
total_collected_data = 0
hovering_time = [0]*len(stoppoints)
energy = 0
collected_datas = matrix.sum(axis = 1) # this is each stoppoints' collected data.
hovering_time = matrix.max(axis = 1) # this is each stoppoints' hovering time.
while energy <= Energy:
    i = np.argmax(collected_datas)
    energy += hovering_time[i]
    total_collected_data += collected_datas[i]
    collected_datas[i]=0

print("{},{},{}".format(Filename,total_collected_data,time.time() - start_time))