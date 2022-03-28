import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
def PlotSpo2(sourcePath, targetPath, nameOfPerson):
#df = pd.read_csv(sys.argv[1] + sys.argv[2])
    try:
        df = pd.read_csv(sourcePath)
        fig, f = plt.subplots()
        f.plot(df.SPO2, label = "SPO2")
        f.plot(df.PULSE, label = "PULSE")
        f.set_ylabel('SPO2 + PULSE')
        f.set_xlabel('sec')
        f.legend(["Spo2", "Pulse"])

        savedFigures = os.listdir(targetPath)
        numberOfSameName = 0
        for figure in savedFigures:
            if (nameOfPerson in figure):
                numberOfSameName += 1

        if numberOfSameName != 0:
            plt.savefig(os.path.join(targetPath, nameOfPerson + str(numberOfSameName) + "-PO80.jpg"))
        else:
            plt.savefig(os.path.join(targetPath, nameOfPerson + "-PO80.jpg"))
    except:
        print("No PO80 data for " + nameOfPerson)

   

