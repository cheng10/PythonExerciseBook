from PIL import Image
import os


DIR = 'imgs/'

for img in os.listdir(DIR):
    im = Image.open(DIR+img)
    after = im.resize((50, 50))
    after.show()
    after.save("resize_"+img, 'jpeg')
