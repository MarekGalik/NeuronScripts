from PIL import Image
import os
from GenerateFigs import generateFigs
import sys
from tkinter import Tcl

sourcePath = sys.argv[1]
targetPath = sys.argv[2]

generateFigs(sourcePath, targetPath)

sourcePath = sys.argv[2]

sortedList = Tcl().call('lsort', '-dict', os.listdir(sourcePath))

images = [
    Image.open(os.path.join(sourcePath, f))
    for f in sortedList
]

pdf_path = os.path.join(targetPath, "report.pdf")

images[0].save(
    pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)

for file in os.listdir(targetPath):
    if file != "report.pdf":
        os.remove(os.path.join(targetPath, file))
