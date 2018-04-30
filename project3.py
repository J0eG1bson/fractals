import numpy as np
import matplotlib.pyplot as plt

##########################################################################
#circle things
def circles(x,y,radius):
    plt.axes()
    circle = plt.Circle((x, y), radius=radius, fc='none')
    plt.gca().add_patch(circle)
    if(radius>0.1):
        radius=radius*0.75
        circles(x,y,radius)

def circles2(x,y,radius):
    plt.axes()
    circle = plt.Circle((x, y), radius=radius, fc='none')
    plt.gca().add_patch(circle)
    if(radius>0.02):
        circles2(x+radius,y,radius/2)
        circles2(x-radius,y,radius/2)
        circles2(x,y+radius,radius/2)
        circles2(x,y-radius,radius/2)
def main():
    circles(0,0,10)
    plt.axis([-10,10,-10,10])
    plt.axes().set_aspect('equal')
    plt.show()
    circles2(0,0,1)
    plt.axis([-1.5,1.5,-1.5,1.5])
    plt.axes().set_aspect('equal')
    plt.show()
#main()
######################################################################
#cantor lines
def cantor(y,x,l):
    if(l>1):
        plt.hlines(y, x, x+l,lw=60,color='r')
        y=y-0.01

        cantor(y,x,l/3)
        cantor(y,x+l*2/3,l/3)
def main2():
    cantor(0,0,3000)
    #plt.axis([-10,10,-10,10])
    #plt.axes().set_aspect('equal')
    plt.show()
#main2()
#########################################################3\
# Koch snow flake

class Kochline:
    def __init__(self,start=[0.0,0.0],end=[100.0,0.0]):
        self.start=np.array(start).tolist()
        self.end=np.array(end).tolist()
        #print(self.start)
        self.x=[self.start[0],self.end[0]]
        self.y=[float(start[1]),float(end[1])]
        self.a=np.asarray(self.start)
        self.b=np.asarray(self.end)
        self.dist=np.linalg.norm(self.a-self.b)
        self.xt=self.b[0]-self.a[0]
        self.yt=self.b[1]-self.a[1]
        self.ang=np.arctan2(self.yt,self.xt)
        self.distdiv3=self.dist/3
        self.xc=np.cos(self.ang)
        self.yc=np.sin(self.ang)

    def kochA(self):
        return self.start
    def kochE(self):
        return self.end
    def kochB(self):
        xn=self.distdiv3*self.xc
        yn=self.distdiv3*self.yc
        v=[self.x[0]+xn,self.y[0]+yn]
        return v
    def kochD(self):
        xn=2*self.distdiv3*self.xc
        yn=2*self.distdiv3*self.yc
        v=[self.x[0]+xn,self.y[0]+yn]
        return v
    def kochC(self):
        xc=np.cos(self.ang+np.pi/3)
        yc=np.sin(self.ang+np.pi/3)
        xn=self.distdiv3*xc
        yn=self.distdiv3*yc
        arr=self.kochB()
        v=[arr[0]+xn,arr[1]+yn]
        return v
def pointbf(radius):
    x=radius*np.cos(np.pi/3)
    y=radius*np.sin(np.pi/3)
    p=[x,y]
    p2=[x,-y]
    return p,p2
def pointce(radius):
    x=radius*np.cos(2*np.pi/3)
    y=radius*np.sin(2*np.pi/3)
    p=[x,y]
    p2=[x,-y]
    return p,p2
def setup(lines,radius):
    a=[radius,0]
    d=[-radius,0]
    b,f=pointbf(radius)
    c,e=pointce(radius)
    start=[0,0]
    arr=[[start,a],[a,b],[b,start]]
    for i in arr:
        lines.append(Kochline(i[1],i[0]))
    return lines


def draw(lines):
    for line in lines:
        plt.plot(line.x,line.y,'ro-',linewidth=4)

def generate(lines):
    nextl = []
    for line in lines:
        a=line.kochA()
        b=line.kochB()
        c=line.kochC()
        d=line.kochD()
        e=line.kochE()

        nextl.append(Kochline(a,b))
        nextl.append(Kochline(b,c))
        nextl.append(Kochline(c,d))
        nextl.append(Kochline(d,e))
    lines=nextl
    return lines
def snowflake():
    lines=[]
    radius=20
    lines=setup(lines,radius)
    for i in range(0,5):
        lines=generate(lines)
    draw(lines)
    xcenter=radius/2
    xlims=1.1*xcenter
    ycenter=np.sqrt(3)/4*radius

    plt.axis([xcenter-xlims,xcenter+xlims,ycenter-1.5*xlims,ycenter+xlims])
    plt.axes().set_aspect('equal')
    plt.show()
snowflake()
#################################################################################
#tree

class Kochline:
    def __init__(self,ang=0,start=[0.0,0.0],end=[100.0,0.0]):
        self.start=np.array(start).tolist()
        self.end=np.array(end).tolist()
        self.ang=ang
        #print(self.start)*0.75
        self.x=[self.start[0],self.end[0]]
        self.y=[self.start[1],self.end[1]]
        self.a=np.asarray(self.start)
        self.b=np.asarray(self.end)
        self.dist=np.linalg.norm(self.a-self.b)
        self.distend=self.dist*0.66
        self.xt=self.a[0]-self.b[0]
        self.yt=self.a[1]-self.b[1]
        self.ang2=np.arctan2(self.yt,self.xt)

    def kochA(self):

        return self.start
    def kochB(self):
        xc=np.cos(self.ang+self.ang2)
        yc=np.sin(self.ang+self.ang2)
        xn=self.distend*xc
        yn=self.distend*yc
        arr=self.start
        v=[arr[0]+xn,arr[1]+yn]
        return v
    def kochC(self):
        xc=np.cos(-self.ang+self.ang2)
        yc=np.sin(-self.ang+self.ang2)
        xn=self.distend*xc
        yn=self.distend*yc
        arr=self.start
        v=[arr[0]+xn,arr[1]+yn]
        return v
        return v


def setup(lines,radius):
    a=[0,200]
    start=[0,0]
    arr=[[start,a]]
    for i in arr:
        lines.append(Kochline(radius,i[1],i[0]))
    return lines


def draw(lines):
    for line in lines:
        # print(line.ang/np.pi)
        # print(line.ang2/np.pi)
        plt.plot(line.x,line.y,'ro-',linewidth=4)
def generate(lines,ang):
    nextl = []
    for line in lines:
        a=line.kochA()
        b=line.kochB()
        c=line.kochC()
        # print("hey")
        # print(a)
        # print(b)
        # print(c)

        nextl.append(Kochline(ang,b,a))
        nextl.append(Kochline(ang,c,a))

    lines=nextl
    return lines

def tree():
    lines=[]
    totallines=[]

    radius=np.pi/6
    lines=setup(lines,radius)
    totallines=lines
    for i in range(0,6):
        lines=generate(lines,radius)
        totallines=totallines+lines
    draw(totallines)

    plt.axis([-400,400,0,600])
    plt.axes().set_aspect('equal')
    plt.show()
tree()
################################################################################
#triangle
class Kochline:
    def __init__(self,ang=0,start=[0.0,0.0],end=[100.0,0.0]):
        self.start=np.array(start).tolist()
        self.end=np.array(end).tolist()
        self.ang=ang
        #print(self.start)*0.75
        self.x=[self.start[0],self.end[0]]
        self.y=[self.start[1],self.end[1]]
        self.a=np.asarray(self.start)
        self.b=np.asarray(self.end)
        self.dist=np.linalg.norm(self.a-self.b)
        self.distend=self.dist*0.5
        self.xt=self.a[0]-self.b[0]
        self.yt=self.a[1]-self.b[1]
        self.ang2=np.arctan2(self.yt,self.xt)

    def kochA(self):

        return self.start
    def kochB(self):
        xc=np.cos(self.ang+self.ang2)
        yc=np.sin(self.ang+self.ang2)
        xn=self.distend*xc
        yn=self.distend*yc
        arr=self.start
        v=[arr[0]+xn,arr[1]+yn]
        return v
    def kochC(self):
        xc=np.cos(-self.ang+self.ang2)
        yc=np.sin(-self.ang+self.ang2)
        xn=self.distend*xc
        yn=self.distend*yc
        arr=self.start
        v=[arr[0]+xn,arr[1]+yn]
        return v
    def kochD(self):
        xc=np.cos(self.ang2)
        yc=np.sin(self.ang2)
        xn=self.distend*xc
        yn=self.distend*yc
        arr=self.start
        v=[arr[0]+xn,arr[1]+yn]
        return v


def setup(lines,radius):
    a=[0,200]
    start=[0,0]
    arr=[[start,a]]
    for i in arr:
        lines.append(Kochline(radius,i[1],i[0]))
    return lines


def draw(lines):
    for line in lines:
        # print(line.ang/np.pi)
        # print(line.ang2/np.pi)
        plt.plot(line.x,line.y,'ro',linewidth=4)
def generate(lines,ang):
    nextl = []
    for line in lines:
        a=line.kochA()
        b=line.kochB()
        c=line.kochC()
        d=line.kochD()
        # print("hey")
        # print(a)
        # print(b)
        # print(c)

        nextl.append(Kochline(ang,b,a))
        nextl.append(Kochline(ang,c,a))
        nextl.append(Kochline(ang,d,a))

    lines=nextl
    return lines

def tree2():
    lines=[]
    totallines=[]

    radius=2/3*np.pi
    lines=setup(lines,radius)
    totallines=lines
    for i in range(0,7):
        lines=generate(lines,radius)
        totallines=totallines+lines
    totallines.pop(0)
    draw(totallines)

    plt.axis([-200,200,50,450])
    plt.axes().set_aspect('equal')
    plt.show()
tree2()
################################################################################
#L-systems
flenght=5

def setup():
    scurrent="A"
    return scurrent

def generation(scurrent):
    snext=""
    read={"A":"AB","B":"A"}
    for i in scurrent:
        snext+=read.get(i)
    return snext

def Lsystem():
    scurrent=setup()
    for i in range(0,10):
        snext=generation(scurrent)
        scurrent=snext
    print(scurrent)
    pass
#Lsystem()
###############################################################################
#plants
###############################################################################
class branch:
    def __init__(self,ang=0,start=[0.0,0.0]):
        self.start=np.array(start).tolist()
        self.end=np.array(start).tolist()
        self.ang=ang
        #print(self.start)*0.75
        self.x=[self.start[0]]
        self.y=[self.start[1]]
        self.a=np.asarray(self.start)
        self.b=np.asarray(self.end)
        self.dist=5
        self.angrot=np.pi/6
    def cmdf(self):
        xc=np.cos(self.ang)
        yc=np.sin(self.ang)
        xn=self.dist*xc
        yn=self.dist*yc
        arr=self.start
        self.start=[arr[0]+xn,arr[1]+yn]
        self.x.append(self.start[0])
        self.y.append(self.start[1])
    def cmdminus(self):
        self.ang=self.ang-self.angrot
    def cmdplus(self):
        self.ang=self.ang+self.angrot
    def endreturn(self):
        return self.start
    def angreturn(self):
        return self.ang

def ffunc(line,lines,drawlines):
    line.cmdf()
    return lines,drawlines
def plusfunc(line,lines,drawlines):
    line.cmdplus()
    return lines,drawlines
def minusfunc(line,lines,drawlines):
    line.cmdminus()
    return lines,drawlines
def savefunc(line,lines,drawlines):
    start=line.endreturn()
    ang=line.angreturn()
    lines.append(branch(ang,start))
    return lines,drawlines
def removefunc(line,lines,drawlines):
    drawlines.append(line)
    lines.remove(line)
    return lines,drawlines

def setup():
    lines=[]
    scurrent="F"
    lines.append(branch(np.pi/2,[0,0]))
    return scurrent,lines

def generation(scurrent):
    snext=""
    read={"F":"FF+[+F-F-F]-[-F+F+F]","+":"+","-":"-","[":"[","]":"]"}
    for i in scurrent:
        snext+=read.get(i)
    return snext

def read(scurrent,lines):
    funcs={"F":ffunc,"+":plusfunc,"-":minusfunc,"[":savefunc,"]":removefunc}
    countdict={"F":"0","+":"0","-":"0","[":"1","]":"-1"}
    drawlines=[]
    count=0
    for i in scurrent:
        line=lines[count]
        #print(i)
        lines,drawlines=funcs[i](line,lines,drawlines)
        if (i == "[" or i=="]"):
            count+=int(countdict.get(i))

    return drawlines

def draw(drawlines):
    for line in drawlines:

        plt.plot(line.x,line.y,'g-',linewidth=1)

def Lsystem():
    drawlines=[]
    scurrent,lines=setup()
    for i in range(0,5):
        snext=generation(scurrent)
        scurrent=snext
        #print(scurrent)
    drawlines=read(scurrent,lines)
    draw(drawlines)

    draw(lines)


    #plt.axis([-50,10,-1,200])
    plt.axes().set_aspect('equal')
    plt.show()
    pass
Lsystem()

################################################################################
