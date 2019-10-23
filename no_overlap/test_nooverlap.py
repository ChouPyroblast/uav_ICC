import os

for f in os.listdir("."):
    for energy in range(1000,5001,100):
        if ".txt" in f:
            print("python heru_no_over_lap.py {} {} >> heru_{}.test".format(energy, f, energy))
            os.system("python heru_no_over_lap.py {} {} >> heru_{}.test".format(energy,f,energy))
            print("python no_over_lap.py {} {} >> alg_{}.test".format(energy, f, energy))
            os.system("python no_over_lap.py {} {} >> alg_{}.test".format(energy, f, energy))

