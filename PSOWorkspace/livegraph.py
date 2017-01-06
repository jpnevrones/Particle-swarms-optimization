"""
__author__      = "Jithin Pradeep"
__version__     = "1.0"
__email__       = "jithinpr2@gmail.com"

"""
import matplotlib.pyplot as pyp
import matplotlib.animation as animate
import time

fig=pyp.figure()
ax1=fig.add_subplot(1,1,1)

def ani (i):
    fileobj=open('datainput','r').read()
    dataarray=fileobj.split('\n')
    Xarr=[]
    Yarr=[]
    for eachLine in dataarray:
        if len(eachLine)>1:
            x,y = eachLine.split(',')
            Xarr.append(int(x))
            Yarr.append(int(y))
    ax1.clear()
    ax1.plot(Xarr,Yarr)


gra = animate.FuncAnimation(fig,ani,interval=1000)
pyp.show()