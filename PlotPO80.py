import matplotlib.pyplot as plt
import pandas as pd
import sys
import os
def PlotPO80(sourcePath, targetPath, nameOfPerson, index):
#df = pd.read_csv(sys.argv[1] + sys.argv[2])
    try:
        df = pd.read_csv(sourcePath)
        fig, ax = plt.subplots(figsize=(15,5))
        lns1 = ax.plot(df.SPO2, label = "SPO2", color = "red")
        ax2 = ax.twinx()
        lns2 = ax2.plot(df.PULSE, label = "PULSE", color = "blue")
        ax.set_ylabel('SPO2')
        ax2.set_ylabel('PULSE')
        ax.set_xlabel('sec')
        labs = ["SPO2", "PULSE"]
        lns = lns1 + lns2
        ax.legend(lns, labs, loc=0)
        plt.title(index + ". meranie-" + nameOfPerson + "-PO80",fontsize = 15, weight = "bold")

        savedFigures = os.listdir(targetPath)
        numberOfSameName = 0
        for figure in savedFigures:
            if (nameOfPerson in figure and "-PO80.jpg" in figure):
                numberOfSameName += 1

        if numberOfSameName != 0:
            plt.savefig(targetPath + "\\" + index + ". meranie-" + nameOfPerson + str(numberOfSameName + 1) + "-PO80.jpg")
        else:
            plt.savefig(targetPath + "\\" + index + ". meranie-" + nameOfPerson + "-PO80.jpg")
    except:
        print("No PO80 data for " + nameOfPerson)

   

