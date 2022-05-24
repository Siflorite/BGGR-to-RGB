import numpy as np
width=0
height=0
t=0
with open("bggr.txt","r") as ff:
    for l in ff.readlines():
        l = l.strip('\n')
        if(l[0]!="("):
            if(width!=0):
                height=int(l)
            else:
                width=int(l)
r = np.zeros([width,height],dtype=int)
g = np.zeros([width,height],dtype=int)
b = np.zeros([width,height],dtype=int)
with open("bggr.txt","r") as f:
    for l in f.readlines():
        l = l.strip('\n')
        if(l[0]=="("):
            l=l.strip('(')
            l=l.strip(')')
            arr_org = l.split(',')
            y = int(t/width)
            x = t%width
            r[x][y]=int(arr_org[0])
            g[x][y]=int(arr_org[1])
            b[x][y]=int(arr_org[2])
            t=t+1
r_new = np.zeros([width,height],dtype=int)
g_new = np.zeros([width,height],dtype=int)
b_new = np.zeros([width,height],dtype=int)

#2*2 interpolation
#lower case for the original
#UPPER CASE FOR NEW RGB
#[0,0][0,1]
#[1,0][1,1]
#R[0,0]=R[0,1]=R[1,0]=R[1,1](effective r[1,1])
#B[0,0](effective b[0,0])=B[0,1]=B[1,0]=B[1,1]
#G[0,0]=G[1,1]=(g[1,0]+g[1,1])/2
#G[1,0]=g[1,0] G[0,1]=g[0,1]
block_width = int(width/2)
block_height = int(height/2)
for block_x in range(block_width):
    for block_y in range(block_height):
        #block accordination:[2bx][2by](B),[2bx+1][2by](G),[2bx][2by+1](G),[2bx+1][2by+1](R)
        red = r[block_x*2+1][block_y*2+1]
        green_avg = int((g[block_x*2+1][block_y*2]+g[block_x*2][block_y*2+1])/2)
        blue = b[block_x*2][block_y*2]
        r_new[block_x*2][block_y*2]=r_new[block_x*2+1][block_y*2]=r_new[block_x*2][block_y*2+1]=r_new[block_x*2+1][block_y*2+1]=red
        b_new[block_x*2][block_y*2]=b_new[block_x*2+1][block_y*2]=b_new[block_x*2][block_y*2+1]=b_new[block_x*2+1][block_y*2+1]=blue
        g_new[block_x*2][block_y*2]=g_new[block_x*2+1][block_y*2+1]=green_avg
        g_new[block_x*2+1][block_y*2]=g[block_x*2+1][block_y*2]
        g_new[block_x*2][block_y*2+1]=g[block_x*2][block_y*2+1]
with open("rgb_interp.txt","w") as nf:
    nf.write(str(width)+"\n")
    nf.write(str(height)+"\n")
    for j in range(height):
        for i in range(width):
            rgb=(r_new[i][j],g_new[i][j],b_new[i][j])
            nf.write(str(rgb)+"\n")
