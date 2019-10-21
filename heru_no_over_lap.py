import sys
import numpy as np
stoppoints = []
max_sensor_stoppoints = 0 # record the stoppoints with maximum sensors.
Energy = 300 #TODO


with open("2.txt") as f:
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
print(collected_datas.shape)
while energy <= Energy:
    i = np.argmax(collected_datas)
    energy += hovering_time[i]
    total_collected_data += collected_datas[i]
    collected_datas[i]=0
print(hovering_time)
print(total_collected_data)
print(matrix)
