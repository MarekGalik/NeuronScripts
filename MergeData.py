import os
import shutil
import sys
import pandas as pd

numOfSources = len(sys.argv) - 2
tabulka = pd.DataFrame(columns=["Dir","Name"])
targetPath = sys.argv[len(sys.argv) - 1]
counter = 0
f = open(os.path.join(targetPath, "tabulka.txt"),"w+")

for i in range(1, numOfSources + 1):
    sourcePath = sys.argv[i]
    listDir = os.listdir(sourcePath)
    df = pd.read_csv(os.path.join(sourcePath, "tabulka.txt"), names=[0,1], sep=' ')

    numofDirs = len(listDir)
    for j in range(numofDirs - 1):
        counter += 1
        index = listDir.index((str(j + 1)))
        nameOfFolder = listDir[index]
        name = str(df.loc[j, 1])
        copyPath = os.path.join(targetPath, str(counter))
        shutil.copytree(os.path.join(sourcePath, nameOfFolder), copyPath)  
        f.write(str(counter) + " " + name + "\n")
        try:
            renameList = os.listdir(os.path.join(copyPath, "PO80"))
            for file in renameList:
                if "_wave.csv" in file:
                    os.rename(os.path.join(copyPath, "PO80", file), os.path.join(copyPath, "PO80", str(counter) + "_wave.csv"))
                else:
                    os.rename(os.path.join(copyPath, "PO80", file), os.path.join(copyPath, "PO80", str(counter) + ".csv"))
        except: 
            print("No PO80 data in " + str(counter) + ". folder")