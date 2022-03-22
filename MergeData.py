import os
import shutil
import sys
import pandas as pd

numOfDirs = len(sys.argv) - 2
df2 = pd.DataFrame(columns=["Dir","Name"])


for i in range(1, numOfDirs):
    path = sys.argv[i]
    listDir = os.listdir(path)
    df = pd.read_csv(os.path.join(path, "tabulka.txt"), header=['index','name'])
    
    for j in range(len(listDir) - 1):
        nameOfFolder = listDir[j]
        index = df.index[df['index'] == nameOfFolder]
        name = df[index, 1]
        shutil.copy(os.path.join(path, nameOfFolder), sys.argv[numOfDirs + 1])
        os.rename(os.path.join(sys.argv[numOfDirs + 1], nameOfFolder), os.path.join(sys.argv[numOfDirs + 1], str(j + 1)))
        