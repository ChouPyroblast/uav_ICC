import numpy as np
import random
max_data = 100
max_sensor = 10000
max_length = 1000
numberofmap = 50
for map in range(numberofmap):
    with open("{}.txt".format(map), "w") as f:
        for i in range(max_sensor):
            x = random.random()*max_length
            y = random.random()*max_length
            data = random.randint(1,max_data)
            string = "{} {} {}\n".format(x,y,data)
            f.write(string)
