from PIL import Image
width=0
height=0
with open("rgb_interp.txt","r") as f:
    l1 = f.readline()
    l1 = l1.strip('\n')
    width = int(l1)
    l2 = f.readline().strip('\n')
    height = int(l2)
    newImg = Image.new("RGB",(width,height))
    for j in range(height):
        for i in range(width):
            line = f.readline().strip('\n')
            line = line.strip('(')
            line = line.strip(')')
            rgb = line.split(',')
            newImg.putpixel((i,j),(int(rgb[0]),int(rgb[1]),int(rgb[2])))
    newImg.show()
    newImg.save("BGGR2RGB.png")
    
