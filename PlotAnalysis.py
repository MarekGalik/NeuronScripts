from cProfile import label
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
 
def PlotAnalysis(sourcePath, nameOfPerson, targetPath, index):
    df = pd.read_csv(sourcePath)
    sampling = 99
    df.drop(index=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15], axis=0, inplace=True)
    df.columns = ['a']
    new = df['a'].str.split("\t", expand=True)
    df.drop(columns=["a"],inplace=True)
    df["red"] = new[0]
    df["ir"] = new[1]
 
    df["red"] = df["red"].astype(int)
    df["ir"] = df["ir"].astype(int)
 
    savedFigures = os.listdir(targetPath)
    numberOfSameName = 0
    numberOfSameName2 = 0
    for figure in savedFigures:
        if (nameOfPerson in figure and "-Coin.jpg" in figure):
            numberOfSameName += 1
        if (nameOfPerson in figure and "-CoinZoom.jpg" in figure):
            numberOfSameName2 += 1
 
    x = np.linspace(0, df.shape[0]/sampling, df.shape[0])
    fig, ax = plt.subplots(figsize=(15,5))
    lns1 = ax.plot(x, df.red, color='green', linewidth=1.0, label="red")
    ax.set_ylabel("red", fontsize = 15, weight = "bold")
    ax2 = ax.twinx()
    ax2.set_ylabel("ir", fontsize = 15, weight = "bold")
    lns2 = ax2.plot(x, df.ir, color='red', linewidth=1.0, label = "ir")
    ax.set_xlabel("sec")
    plt.title(index + ". meranie-" + str(nameOfPerson + " - snap" + str(numberOfSameName+1)), fontsize = 15, weight = "bold")
    lns = lns1 + lns2
    labs = ["red", "ir"]
    ax.legend(lns, labs, loc=0)

    if (numberOfSameName>0):
        plt.savefig(targetPath + "\\" + index + ". meranie-" + nameOfPerson + str(numberOfSameName+1)  + "-Coin.jpg")
    else:
        plt.savefig(targetPath + "\\" +  index + ". meranie-" + nameOfPerson + "-Coin.jpg")

    xZoom = np.linspace(0, 3, 297)
    fig, axZoom = plt.subplots(figsize=(15,5))
    lns1 = axZoom.plot(xZoom, df.red.iloc[0 : 297], color='green', linewidth=1.0, label="red")
    axZoom.set_ylabel("red", fontsize = 15, weight = "bold")
    ax2Zoom = axZoom.twinx()
    ax2Zoom.set_ylabel("ir", fontsize = 15, weight = "bold")
    lns2 = ax2Zoom.plot(xZoom, df.ir.iloc[0 : 297], color='red', linewidth=1.0, label = "ir")
    axZoom.set_xlabel("sec")
    plt.title(index + ". meranie-" + str(nameOfPerson + "-Zoom" + str(numberOfSameName+1)), fontsize = 15, weight = "bold")
    lns = lns1 + lns2
    labs = ["red", "ir"]
    axZoom.legend(lns, labs, loc=0)
    if (numberOfSameName2>0):
        plt.savefig(targetPath + "\\" + index + ". meranie-" + nameOfPerson + str(numberOfSameName2+1)  + "-CoinZoom.jpg")
    else:
        plt.savefig(targetPath + "\\" + index + ". meranie-" + nameOfPerson + "-CoinZoom.jpg")

