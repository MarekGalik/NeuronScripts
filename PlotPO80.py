import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
def PlotPO80(sourcePath, targetPath, nameOfPerson):
#df = pd.read_csv(sys.argv[1] + sys.argv[2])
    try:
        df = pd.read_csv(sourcePath)
        fig, ax = plt.subplots()
        lns1 = ax.plot(df.SPO2, label = "SPO2", color = "red")
        ax2 = ax.twinx()
        lns2 = ax2.plot(df.PULSE, label = "PULSE", color = "blue")
        ax.set_ylabel('SPO2')
        ax2.set_ylabel('PULSE')
        ax.set_xlabel('sec')
        labs = ["SPO2", "PULSE"]
        lns = lns1 + lns2
        ax.legend(lns, labs, loc=0)

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

   

