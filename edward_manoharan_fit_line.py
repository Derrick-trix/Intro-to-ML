from matplotlib import pyplot as plt
import numpy as np
button=1

def mylinfit(x,y) :
    n=len(x)
    sumx=np.sum(x)
    sumy=np.sum(y)
    xbar=sumx/n
    ybar=sumy/n
    sumxsq=np.sum(np.square(x))
    sumxy=np.dot(x,y)
    b=((sumxsq*ybar)-(xbar*sumxy))/(sumxsq+(xbar*sumx))
    a=(sumxy-(sumx*b))/sumxsq
    #a = ((n*sumxy)-(sumx*sumy))/(n*(sumxsq)-(sumx-sumx))
    #b = (sumy/n)-(a*(sumx/n))
    return a , b
class LineBuilder():
    def __init__(self, line):
        self.line = line
        self.x = list(line.get_xdata())
        self.y = list(line.get_ydata())
        self.cid = line.figure.canvas.mpl_connect('button_press_event', self)
    def __call__(self, event):
        if int(event.button)==1:
            self.x.append(event.xdata)
            self.y.append(event.ydata)
            plt.plot(event.xdata, event.ydata, 'kx')
            plt.draw()
        elif int(event.button)==3:
            a, b = mylinfit(np.array(self.x[1:]), np.array(self.y[1:]))
            xp = np.arange(0,5,0.1)
            ax.plot(xp, a * xp + b, 'r-')
            plt.draw()
            print("The value of a:",a," and b:",b)


fig, ax = plt.subplots()
ax.set_xlim(0, 5)
ax.set_ylim(0, 5)
line, = plt.plot([0],[0])
linebuilder = LineBuilder(line)
plt.show()
