import numpy as np
import sys
numberofsensor = 10000
numberofstop = 100
numberofmap = 50
for map in range(numberofmap):
    sensors = np.random.randint(low=100, size = numberofsensor)
    stoppoints = []
    for i in range(numberofstop):
        stoppoints.append([])
    loc = np.random.randint(low = 0, high = numberofstop-1,size = numberofsensor)
    for i in range(len(loc)):
        stoppoints[loc[i]].append(sensors[i])
    print(len(stoppoints[-5]))

    with open("{}.txt".format(map),"w") as f:
        for stoppoint in stoppoints:
            num2word = [str(x) for x in stoppoint]
            string = " ".join(num2word)+"\n"
            f.write(string)






