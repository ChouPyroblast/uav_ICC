import numpy as np
import sys
numberofsensor = 100
numberofstop = 10

sensors = np.random.randint(low=10, size = numberofsensor)
stoppoints = []
for i in range(numberofstop):
    stoppoints.append([])
loc = np.random.randint(low = 0, high = numberofstop-1,size = numberofsensor)
for i in range(len(loc)):
    stoppoints[loc[i]].append(sensors[i])
print(len(stoppoints[-5]))

with open("1.txt","w") as f:
    for stoppoint in stoppoints:
        num2word = [str(x) for x in stoppoint]
        string = " ".join(num2word)+"\n"
        f.write(string)






