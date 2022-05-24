from PIL import Image
from numpy import array
with Image.open("img.png") as img:
    im = img.convert('RGB')
    width = img.size[0]
    height = img.size[1]
    with open("rgb.txt","w") as f:
        f.write(str(width)+"\n")
        f.write(str(height)+"\n")
        for y in range(height):
            for x in range(width):
                r,g,b = im.getpixel((x,y))
                rgb = (r,g,b)
                f.write(str(rgb)+"\n")
