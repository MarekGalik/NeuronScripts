import os
import shutil
import sys

target = sys.argv[2]
src = sys.argv[1]

listDir = os.listdir(src)

size = int(len(listDir)/5)+1
for file in range(1, size):
    try:
        index = listDir.index((str(file) + ".csv"))
        sourcePath =  os.path.join(src, listDir[index])
        os.mkdir((target + "\\" + str(file) + "\\PO80"))
        targetPath = os.path.join(target, str(file), "PO80", listDir[index])
        shutil.copyfile(sourcePath, targetPath)
    except:
        size += 1
        
size = int(len(listDir)/5)+1
for file in range(1, size):
    try:
        index = listDir.index((str(file) + "_wave.csv"))
        sourcePath =  os.path.join(src, listDir[index])
        targetPath = os.path.join(target, str(file), "PO80", listDir[index])
        shutil.copyfile(sourcePath, targetPath)
    except:
        size += 1

for file in range(0, len(listDir)):
    os.remove(os.path.join(src, listDir[file]))