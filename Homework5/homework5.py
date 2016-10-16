#coding=utf8
import os
import math
import matplotlib.pyplot as plt


class cannon:
	"""模拟炮弹轨迹"""
	def __init__(self, x = 0, y = 0, t = 0, angle = 30, dt = 0.005, v = 700, b2_m = 0.04):
		self.x = [float(x)] # km
		self.y = [float(y)] # km
		self.t = [t] # s
		self.dt = dt #s
		self.v = v # m/s
		self.angle = math.radians(angle) # degree
		self.vx = [v * math.cos(self.angle)] # m/s
		self.vy = [v * math.sin(self.angle)] # m/s
		self.ax_drag = 0 # m/s
		self.ay_drag = 0 # m/s
		self.b2_m = b2_m # /km
		self.y0 = 10 # km
	def calculate_simple(self):
		while (self.y[-1] >= 0):
			self.x.append(self.x[-1] + self.vx[-1]* self.dt* 0.001)
			self.y.append(self.y[-1] + self.vy[-1]* self.dt* 0.001)
			self.vx.append(self.vx[-1])
			self.vy.append(self.vy[-1] - 9.8* self.dt)
			self.t.append(self.t[-1] + self.dt)
		r = - (self.y[-2] / self.y[-1])
		self.x[-1] = (self.x[-2] + r * self.x[-1]) / (r + 1)
		self.y[-1] = 0
	def calc_with_drag(self):
		while(self.y[-1] >= 0):
			self.x.append(self.x[-1] + self.vx[-1]* self.dt* 0.001)
			self.y.append(self.y[-1] + self.vy[-1]* self.dt* 0.001)
			self.v = math.sqrt( math.pow(self.vx[-1], 2) + math.pow(self.vy[-1], 2))
			self.ax_drag = -0.001* self.b2_m* self.v* self.vx[-1]
			self.ay_drag = -0.001* self.b2_m* self.v* self.vy[-1]
			self.vx.append(self.vx[-1] + self.ax_drag* self.dt)
			self.vy.append(self.vy[-1] + (self.ay_drag - 9.8)* self.dt)
			self.t.append(self.t[-1] + self.dt)
		r = - (self.y[-2] / self.y[-1])
		self.x[-1] = (self.x[-2] + r * self.x[-1]) / (r + 1)
		self.y[-1] = 0

	def calc_with_density(self):
		while (self.y[-1] >= 0) :
			self.x.append(self.x[-1] + self.vx[-1]* self.dt* 0.001)
			self.y.append(self.y[-1] + self.vy[-1]* self.dt* 0.001)
			self.v = math.sqrt( math.pow(self.vx[-1], 2) + math.pow(self.vy[-1], 2) )
			self.ax_drag = -0.001* self.b2_m* self.v* self.vx[-1]* math.exp(- self.y[-1] / self.y0)
			self.ay_drag = -0.001* self.b2_m* self.v* self.vy[-1]* math.exp(- self.y[-1] / self.y0)
			self.vx.append(self.vx[-1] + self.ax_drag* self.dt)
			self.vy.append(self.vy[-1] + (self.ay_drag - 9.8)* self.dt)
			self.t.append(self.t[-1] + self.dt)
		r = - (self.y[-2] / self.y[-1])
		self.x[-1] = (self.x[-2] + r * self.x[-1]) / (r + 1)
		self.y[-1] = 0

	def save_to_file(self, label = 'x'):
		filename = 'cannon_shell_trajrctory_' + label + '_.txt'
		file = open(filename, 'w')
		for i in range(len(self.t)):
		    print >> file, ' %10.6f\t %10.6f\t %10.3f' % (self.x[i], self.y[i], self.t[i])
		file.close()

def get(msg,default = 0):
    r = raw_input(msg)
    if r == '':
        return default
    return r

print('----Compare three different simulation modes----\n')
#三种模拟方式对比
v = get('Input the initial velocity (default: 700):\n', 700)
angle = get('Input the initial angle (default: 30):\n', 30)

a = cannon(v = v, angle = angle)
b = cannon(v = v, angle = angle)
c = cannon(v = v, angle = angle)
a.calculate_simple()
b.calc_with_drag()
c.calc_with_density()
a.save_to_file('simple')
b.save_to_file('with-air-drag')
c.save_to_file('with_density_correction')

p1, = plt.plot(a.x,a.y, color = 'black')
p2, = plt.plot(b.x,b.y, color = 'blue')
p3, = plt.plot(c.x,c.y, color = 'red')
plt.title('Cannon shell trajectory')
plt.xlabel('x($km$)')
plt.ylabel('y($km$)')
plt.legend([p1,p2,p3], ['simplest', 'air drag', 'air density'])
plt.savefig('Cannon shell trajectory.png')
plt.show()

print('----Determine the maximum range----')
#特定模拟方式的多角度模拟并求最优
i = raw_input('Please choose the simulation mode\n\
(1:simple, 2:with air drag, 3:with density correction)\n\
Input the mode number to choose:\n')
	
v = get('Input the initial velocity (default: 700):\n', 700)
theta = 30
range = [['angle'],['range']]
print 'angle\trange\n'
if i == '1':
	mode = 'Cannon shell trajectory without air drag'
	while (theta <= 60):
		a = cannon(v = v, angle = theta)
		a.calculate_simple()
		plt.plot(a.x,a.y,label = theta)
		print theta,'\t',a.x[-1],'\n'
		range[0].append(theta)
		range[1].append(a.x[-1])
		theta += 5
elif i == '2':
	mode = 'Cannon shell trajectory with air drag'
	while (theta <= 60):
		a = cannon(v = v, angle = theta)
		a.calc_with_drag()
		plt.plot(a.x,a.y,label = theta)
		print theta,'\t',a.x[-1],'\n'
		range[0].append(theta)
		range[1].append(a.x[-1])
		theta += 5
else:
	mode = 'Cannon shell trajectory with air density correction'
	while (theta <= 60):
		a = cannon(v = v, angle = theta)
		a.calc_with_density()
		plt.plot(a.x,a.y,label = theta)
		print theta,'\t',a.x[-1],'\n'
		range[0].append(theta)
		range[1].append(a.x[-1])
		theta += 5


plt.title(mode)
plt.xlabel('x($km)')
plt.ylabel('y($km)')
plt.text(40,10,'Initial Speed=%dm/s'%(v))
plt.text(20,6,'angle($degree$)')
plt.legend()
plt.savefig(mode + ' (different angles).png')
plt.show()
