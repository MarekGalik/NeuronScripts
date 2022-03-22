import os
import shutil
import sys
import pandas as pd

numOfSources = len(sys.argv) - 2
tabulka = pd.DataFrame(columns=["Dir","Name"])
targetPath = sys.argv[len(sys.argv) - 1]
counter = 0

for i in range(1, numOfSources + 1):
    sourcePath = sys.argv[i]
    listDir = os.listdir(sourcePath)
    df = pd.read_csv(os.path.join(sourcePath, "tabulka.txt"), header=[0,1])
    
    numofDirs = len(listDir)
    for j in range(numofDirs - 1):
        counter += 1
        nameOfFolder = listDir[j]
        #rowIndex = df.index[df[0] == nameOfFolder]
        #rowIndex = pd.Index[df[0] == nameOfFolder]
        name = df[int(df[0] == nameOfFolder), 1]
        shutil.copy(os.path.join(sourcePath, nameOfFolder), targetPath)
        os.rename(os.path.join(targetPath, nameOfFolder), os.path.join(targetPath, str(counter)))  
        tabulka = tabulka.append({'Dir' : str(j + 1), 'Name' : name})