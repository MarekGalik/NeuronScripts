import sys
import os
import matplotlib.pyplot as plt
import numpy as np

def PlotCoinSPO2(sourcePath, targetPath, index, nameOfPerson, nameOfSnap):
    pathToTxt = os.path.join(sourcePath,"result.txt")
    big_list = []

    try:
        with open(pathToTxt, "r") as file:
            lines=file.readlines()
            for line in lines:
                if ("LEDs" in line):
                    big_list.append(line)
                else:
                    big_list.append(list(map(str,line.split())))
    except:
        print("Result.txt not found.")
        return
    
    fig, ax = plt.subplots(figsize=(15,5))
    x = np.linspace(0, ((len(big_list[1])-1)/99), (len(big_list[1]))-1)

    for i in range(len(big_list)):
        if (str(big_list[i]).find(nameOfSnap) != -1):
            big_list[i+1].pop(0)
            big_list[i+2].pop(0)
            big_list[i+3].pop(0)
            big_list[i+1] = list(map(float,big_list[i+1]))
            big_list[i+2] = list(map(float,big_list[i+2]))
            big_list[i+3] = list(map(float,big_list[i+3]))
            ax.plot(x,big_list[i+1], label = "SPO2", color = "red")
            ax.plot(x,big_list[i+2], label = "SPO2X", color = "green")
            ax.plot(x,big_list[i+3], label = "BPM", color = "blue")
            ax.legend()
            savedFigures = os.listdir(targetPath)
            numberOfSameName = 0
            numberOfSameName2 = 0
            for figure in savedFigures:
                if (nameOfPerson in figure and "-SPO2Coin.jpg" in figure):
                    numberOfSameName += 1
                    if(index in figure):
                        numberOfSameName2 +=1

            if (numberOfSameName > 0):
                if (numberOfSameName2 == 0):
                    plt.title(index + ". meranie-" + nameOfPerson + "-SPO2-snap1",fontsize = 15, weight = "bold")
                else:
                    plt.title(index + ". meranie-" + nameOfPerson + "-SPO2-snap" + str(numberOfSameName2+1),fontsize = 15, weight = "bold")
                plt.savefig(targetPath + "\\" + index + ". meranie-" + nameOfPerson + str(numberOfSameName + 1) + "-SPO2Coin.jpg")
            else:
                plt.title(index + ". meranie-" + nameOfPerson + "-SPO2-snap1",fontsize = 15, weight = "bold")
                plt.savefig(targetPath + "\\" + index + ". meranie-" + nameOfPerson + "-SPO2Coin.jpg")
            return
    print("No SPO2 data in result.txt for required snap.")
