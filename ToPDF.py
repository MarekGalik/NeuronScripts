from PIL import Image
import os
from GenerateFigs import generateFigs
import sys

sourcePath = sys.argv[1]
targetPath = sys.argv[2]

generateFigs(sourcePath, targetPath)

sourcePath = sys.argv[2]

images = [
    Image.open(os.path.join(sourcePath, f))
    for f in os.listdir(sourcePath)
]

pdf_path = os.path.join(targetPath, "report.pdf")
    
images[0].save(
    pdf_path, "PDF" ,resolution=100.0, save_all=True, append_images=images[1:]
)
