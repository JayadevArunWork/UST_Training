#MY USE CASE PROBLEM
#IMAGE RESIZER: Resize all images in a folder to a given width and height using Pillow
from PIL import Image
import os

FOLDER = "./images" 
OUTPUT = "./resized" 
WIDTH, HEIGHT = 800, 600 

os.makedirs(OUTPUT, exist_ok=True)

for file in os.listdir(FOLDER):
    if file.lower().endswith((".jpg", ".jpeg", ".png", ".gif", ".bmp")):
        path = os.path.join(FOLDER, file)
        img = Image.open(path)
        img = img.resize((WIDTH, HEIGHT), Image.ANTIALIAS)

        out_path = os.path.join(OUTPUT, file)
        img.save(out_path)
        print("Resized Finish!")