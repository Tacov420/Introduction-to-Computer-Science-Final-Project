from PIL import Image
import numpy

def mapping(new,old):
    def m(o):
        n=o*new//old
        return n
    return m

newpicH,newpicW=60, 20
path="tor.jpg"
file=open(path.split('.')[0]+'drawcode.txt','w')
img=Image.open(path)

newImage=[[255 for i in range(newpicW)]for j in range(newpicH)]

for i in enumerate(map(mapping(img.width,newpicW),[l for l in range(newpicW)])):
    for j in enumerate(map(mapping(img.height,newpicH),[k for k in range(newpicH)])):
        if(img.getpixel((i[1],j[1]))[0]>128):
            newImage[j[0]][i[0]]=(255,255,255)
        else:
            newImage[j[0]][i[0]]=(0,0,0)
            file.write("    do TreeBoss.drawrectangle(x+"+str(2*i[0])+','+str(j[0])+"+y,x+"+str(2*i[0]+1)+','+str(j[0])+"+y);\n")
        
        

arr=numpy.array(newImage,dtype='uint8')
img2=Image.fromarray(arr)
img2.save(path.split('.')[0]+'new.'+path.split('.')[1])
file.close()
