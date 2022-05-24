width = 0
height = 0
t=0
#-----------BGGR Format--------#
#BGBGBGBGBGBGBGBG
#GRGRGRGRGRGRGRGR
#BGBGBGBGBGBGBGBG
#GRGRGRGRGRGRGRGR
#------------------------------#
#In conclusion,B when x is even and y is even
#R when x is odd and y is odd
with open("rgb.txt","r") as f:
    with open("bggr.txt","w") as nf:
        for line in f.readlines():
            line = line.strip('\n')
            if(line[0]!="("):
                if(width!=0):
                    height=int(line)
                    nf.write(str(height)+"\n")
                else:
                    width=int(line)
                    nf.write(str(width)+"\n")
            else:
                line = line.strip('(')
                line = line.strip(')')
                arr = line.split(',')
                y = int(t/width)
                x = t%width
                if(x%2==0 and y%2==0):
                    arr[0]=0
                    arr[1]=0#only blue
                elif(x%2==1 and y%2==1):
                    arr[1]=0
                    arr[2]=0#only red
                else:
                    arr[0]=0
                    arr[2]=0#green
                pixels = (int(arr[0]),int(arr[1]),int(arr[2]))
                nf.write(str(pixels)+"\n")
                t=t+1

