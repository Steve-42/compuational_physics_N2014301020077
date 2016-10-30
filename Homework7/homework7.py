#coding=utf8
import os
import math
import matplotlib.pyplot as plt


class pendulum:
	"""模拟物理摆混沌效应"""
	def __init__(self, theta = 0.2,delta_t = 0.04, time = 5000, omega = 0, g = 9.8, l = 9.8, q = 0.5, F_D = 1.2, Omega_D = 2.0/3):
		self.theta = [theta] # rad
		self.omega = [omega] # rad/s
		self.t = [0] # s
		self.delta_t = delta_t
		self.time = time
		self.g = g # m/s2
		self.l = l # m
		self.q = q # 1/s
		self.F_D = F_D # 1/s2
		self.Omega_D = Omega_D # rad/s
		self.section = []
		self.section_omega = []
		self.section_theta = []

	def calculate(self):
		while (self.t[-1] <= self.time) :
			delta_omega = self.delta_t * ( - (self.g / self.l) * math.sin(self.theta[-1]) - (self.q * self.omega[-1]) + self.F_D * math.sin(self.Omega_D * self.t[-1]))
			self.omega.append(self.omega[-1] + delta_omega)
			delta_theta = self.omega[-1] * self.delta_t
			theta = self.theta[-1] + delta_theta
			while (theta >= math.pi):
				theta -= 2 * math.pi
			
			while (theta < (-math.pi)):
				theta += 2 * math.pi
			
			self.theta.append(theta)
			self.t.append(self.t[-1] + self.delta_t)

	def poincare_section(self):
		routes = self.time // ((2 * math.pi) / self.Omega_D)
		print routes
		i = 0
		h = math.pi / self.Omega_D
		for n in range(int(routes)):
			j = i
			while (j >= i) :
				delta = abs(self.t[j] - (2 * n *math.pi)/self.Omega_D)
				if (delta <= h):
					self.section.append(j)
					i = j+1
				else:
					j += 1
		for k in self.section :
			self.section_theta.append(self.theta[k])
			self.section_omega.append(self.omega[k])

					

def get(msg,default = 0):
    r = raw_input(msg)
    if r == '':
        return default
    return r


a = pendulum()
a.calculate()
a.poincare_section()



plt.plot(a.section_theta,a.section_omega,'.')
#plt.plot(a.t,a.theta)
plt.title("Poincare section of the pendulum")
plt.xlabel('$\\theta$($radians$)')
plt.ylabel('$\\omega$($radians/s$)')
#plt.text(40,10,'Initial Speed=%dm/s'%(v))
#plt.text(25,5,'angle($degree$)')
plt.savefig('Poincare section of the pendulum.png')
plt.show()
