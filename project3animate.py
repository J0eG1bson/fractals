import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation


###############################################################################
#plants

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
        self.dist=1
        self.angrot=np.pi/4

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


    # def kochD(self):
    #     xc=np.cos(self.ang2)
    #     yc=np.sin(self.ang2)
    #     xn=self.distend*xc
    #     yn=self.distend*yc
    #     arr=self.start
    #     v=[arr[0]+xn,arr[1]+yn]
    #     return v
def func1(line,lines,drawlines):
    line.cmdf()
    return lines,drawlines
def func0(line,lines,drawlines):
    line.cmdplus()
    return lines,drawlines
def minusfunc(line,lines,drawlines):
    line.cmdf()
    return lines,drawlines
def savefunc(line,lines,drawlines):
    start=line.endreturn()
    ang=line.angreturn()
    lines.append(branch(ang,start))
    line=lines[-1]
    line.cmdplus()
    return lines,drawlines
def removefunc(line,lines,drawlines):
    drawlines.append(line)
    lines.remove(line)
    line=lines[-1]
    line.cmdminus()
    return lines,drawlines

def setup():
    lines=[]
    scurrent="0"
    lines.append(branch(np.pi/2,[0,0]))
    return scurrent,lines

def generation(scurrent):
    snext=""
    read={"1":"11","0":"1[0]0","[":"[","]":"]"}
    for i in scurrent:
        snext+=read.get(i)
    return snext

def read(scurrent,lines):
    funcs={"1":func1,"0":func0,"[":savefunc,"]":removefunc}
    countdict={"1":"0","0":"0","[":"1","]":"-1"}
    drawlines=[]
    count=0
    for i in scurrent:
        line=lines[count]
        #print(i)
        lines,drawlines=funcs[i](line,lines,drawlines)
        if (i == "[" or i=="]"):
            count+=int(countdict.get(i))
        #print(count)
        #print(line.x)
        #print(len(lines))
    return drawlines

def draw(drawlines):
    datax=[]
    datay=[]
    for line in drawlines:
        #print(line.x)
        #print(line.y)
        for j in line.x:
            datax.append(j)
        for k in line.y:
            datay.append(k)
    return datax,datay

def Lsystem(iterate):
    drawlines=[]
    scurrent,lines=setup()
    for i in range(0,iterate):
        snext=generation(scurrent)
        scurrent=snext
        #print(scurrent)
    drawlines=read(scurrent,lines)
    drawlines=lines+drawlines

    datax,datay=draw(drawlines)
    #plt.axis([-50,10,-1,200])

    return datax,datay
#Lsystem()

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(-500,500), ylim=(-1, 1000))
line, = ax.plot([], [],'ro',lw=2)

# initialization function: plot the background of each frame
def init():
    line.set_data([], [])
    return line,

# animation function.  This is called sequentially
def animate(i):
    if i < 11:
        datax,datay=Lsystem(i)
        line.set_data(datax,datay)
    if i>=11:
        datax,datay=Lsystem(21-i)
        line.set_data(datax,datay)
    return line,

# call the animator.  blit=True means only re-draw the parts that have changed.
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=22, interval=200, blit=False,repeat=True)
                               #pause
anim.event_source.stop()

#unpause
anim.event_source.start()

plt.show()
