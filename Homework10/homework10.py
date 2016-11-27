#! python2.7
import sys
import math
import time
from visual import *
from matplotlib import pyplot

m = 100
d = 100.
beta = 2.05
v_0 = 10*math.sqrt(4*pow(math.pi,2)/(pow(d,beta)))
a = 0.95

earth = sphere(pos=( d,0,0), radius=3, color=color.blue)
sun   = sphere(pos=(0,0,0), radius=8, color=color.yellow, material=materials.emissive)
earth.velocity = a*vector(0,v_0,0)
sun.velocity = vector(0,0,0)
earth.trail = curve(color=color.white)


def updatePosition(earth, dt = 0.1):
    d = mag(earth.pos - sun.pos)
    earth.velocity -= earth.pos * (4*math.pi**2/d**(beta+1)) * dt
    earth.pos += earth.velocity * dt

for i in range(300000):
    rate(300000)
    earth.trail.append(pos=earth.pos)
    updatePosition(earth)

fig = pyplot.figure(figsize=(12,12))
max_x, max_y = d,d
ax = fig.add_subplot(111, xlim=(-max_x,max_x), ylim=(-max_y,max_y), autoscale_on=False)
ax.set_title(r"Simulation of elliptical orbit: $V_{init}=$" + str(a) + "$V_0$")
ax.set_xlabel(r'$x(AU)$', fontsize=16)
ax.set_ylabel(r'$y(AU)$', fontsize=16)
pyplot.scatter(earth.trail.x, earth.trail.y, s = 0.1, c = "k", )
pyplot.savefig("Simulation of elliptical orbit:" + str(a)+".png",dpi=72)
pyplot.show()