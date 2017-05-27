import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

pullData = open("out.txt","r").read()
lines = pullData.split('\n')

plt.figure(0)
style.use("ggplot")
fig = plt.figure(0)
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    xar = []
    yar = []
    
    x = 0
    y = 0

    for l in lines:
        x += 1
        if "pos" in l:
            y += 1
        elif "neg" in l:
            y -= 1

        xar.append(x)
        yar.append(y)
        
    ax1.clear()
    ax1.plot(xar,yar)
ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.figure(1)
pos = 0
neg = 0

for l in lines:
    if "pos" in l:
        pos += 1
    elif "neg" in l:
        neg += 1

slices = [pos,neg]
activities = ['Positive','Negative']
cols = ['g','r']
plt.pie(slices,
        labels=activities,
        colors=cols,
        startangle=90,
        shadow= True,
        explode=(0.1,0),
        autopct='%1.1f%%')

plt.title('Interesting Graph\nCheck it out')

plt.show()