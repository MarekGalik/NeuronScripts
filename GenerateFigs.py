import sys
import os
import pandas as pd
from PlotAnalysis import PlotAnalysis
from PlotPO80 import PlotPO80
 
sourcePath = sys.argv[1]
targetPath = sys.argv[2]
def generateFigs(sourcePath, targetPath):
    listDir = os.listdir(sourcePath)
    if ("tabulka.txt" in listDir):
        listDir.remove("tabulka.txt")
    df = pd.read_csv(os.path.join(sourcePath, "tabulka.txt"), names=[0,1], sep=' ')
    nameOfLedsFolder = ""
 
    for dir in listDir:
        nameOfPerson = str(df.loc[(int(dir))-1, 1])
        pathToDir = os.path.join(sourcePath, str(dir))
        listDirInDir = os.listdir(pathToDir)
        for dirInDir in listDirInDir:
            if ("PO80" in dirInDir):
                PlotPO80(os.path.join(sourcePath, dir, dirInDir, dir + ".csv"),targetPath, nameOfPerson)
            if("LEDs" in dirInDir):
                nameOfLedsFolder = dirInDir
        if (nameOfLedsFolder == ""):
            print("In directory " + dir + " is no Leds-... folder.")
            continue
 
        pathToFiles = os.path.join(pathToDir, nameOfLedsFolder)
        files = os.listdir(pathToFiles)
        for file in files:
            if (".txt" in file and "-Log" not in file):
                PlotAnalysis(os.path.join(pathToFiles,file),nameOfPerson,targetPath)
