from PIL import Image
import glob, os

size = 50, 50

for infile in glob.glob("*.jpeg"):
    im = Image.open(infile)
    after = im.resize(size)
    after.save("resize_"+infile, "JPEG")
