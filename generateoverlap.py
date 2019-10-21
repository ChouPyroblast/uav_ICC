import numpy as np
import random
max_data = 10
max_sensor = 100000
max_length = 1000

with open("1.txt","w") as f:
    for i in range(max_sensor):
        x = random.random()*max_length
        y = random.random()*max_length
        data = random.randint(1,max_data)
        string = "{} {} {}\n".format(x,y,data)
        f.write(string)