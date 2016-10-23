#coding=utf8
import os
import math
import matplotlib.pyplot as plt


class cannon:
	"""模拟炮弹轨迹"""
	def __init__(self, x = 0, y = 0, t = 0, angle = 30, dt = 0.005, v = 700, b2_m = 0.04, target_altitude = 0.0,v_wind = -20, a = 6.5, alfha = 2.5, T0 = 300):
		self.x = [float(x)] # km
		self.y = [float(y)] # km
		self.t = [t] # s
		self.dt = dt # s
		self.v = v # m/s
		self.v_w = v_wind # m/s
		self.angle = math.radians(angle) # degree
		self.vx = [float(v) * math.cos(self.angle)] # m/s
		self.vy = [float(v) * math.sin(self.angle)] # m/s
		self.ax_drag = 0 # m/s
		self.ay_drag = 0 # m/s
		self.b2_m = b2_m # /km
		self.a = a # K/km
		self.alfha = alfha # ---
		self.T0 = 300 # K
		self.y_t = float(target_altitude) # km

	def calculate(self):
		while (self.y[-1] >= self.y_t) :
			self.x.append(self.x[-1] + self.vx[-1]* self.dt* 0.001)
			self.y.append(self.y[-1] + self.vy[-1]* self.dt* 0.001)
			self.v = math.sqrt( math.pow(self.vx[-1], 2) + math.pow(self.vy[-1], 2) )
			self.ax_drag = -0.001* self.b2_m* self.v* (self.vx[-1] - self.v_w)* math.pow((1 - self.a*self.y[-1] / self.T0) , self.alfha)
			self.ay_drag = -0.001* self.b2_m* self.v* self.vy[-1]* math.pow((1 - self.a*self.y[-1] / self.T0) , self.alfha)
			self.vx.append(self.vx[-1] + self.ax_drag* self.dt)
			self.vy.append(self.vy[-1] + (self.ay_drag - 9.8)* self.dt)
			self.t.append(self.t[-1] + self.dt)
		r = - (self.y[-2] - self.y_t) / (self.y[-1] - self.y_t)
		self.x[-1] = (self.x[-2] + r * self.x[-1]) / (r + 1)
		self.y[-1] = self.y_t

def get(msg,default = 0):
    r = raw_input(msg)
    if r == '':
        return default
    return r


if raw_input("use the default config?(Y/N)\n") in ["N","n"] :
	#angle = get("launch_angle[degree] =\n",30)
	v = get("launch_velocity[m/s] =\n",700)
	y_t = get("relative altitude of target[km] =\n",0)
	v_w = get("head_wind speed[m/s] (leave the sign negative if it is upwind) =\n",-20)
else:
	v = 700
	y_t = 0
	v_w = -20

theta = 30
while (theta <= 60):
	a = cannon(angle=theta, v=v, target_altitude=y_t, v_wind=v_w)
	a.calculate()
	plt.plot(a.x,a.y,label = theta)
	theta += 5
b = [0,y_t]
sorted(b)
ylimit = float(b[-1])
plt.title("Cannon shell trajectory")
plt.ylim(ylimit, 20 + ylimit)
plt.xlabel('x($km$)')
plt.ylabel('y($km$)')
plt.text(40,10,'Initial Speed=%dm/s'%(v))
plt.text(25,5,'angle($degree$)')
plt.legend()
plt.savefig('Cannon shell trajectory.png')
plt.show()
