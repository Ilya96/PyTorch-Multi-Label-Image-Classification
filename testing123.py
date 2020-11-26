import sys
import os
from PIL import Image

# Opens a image in RGB mode  
files= [f for f in os.listdir("fashion-product-images/images")]
for i in files:
    img = Image.open(r"fashion-product-images/images/" + i)
    img = img.resize((227, 227))
    img.save("fashion-product-images/images2/" + i)