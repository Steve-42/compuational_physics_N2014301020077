#coding=utf8
import sys
import math
import time
import numpy
import random
from matplotlib import pyplot



a_m = numpy.loadtxt('a.txt')
b_m = numpy.loadtxt('b.txt')
c_m = numpy.loadtxt('c.txt')
d_m = numpy.loadtxt('d.txt')
e_m = numpy.loadtxt('e.txt')
f_m = numpy.loadtxt('f.txt')
g_m = numpy.loadtxt('g.txt')
h_m = numpy.loadtxt('h.txt')
i_m = numpy.loadtxt('i.txt')
j_m = numpy.loadtxt('j.txt')
k_m = numpy.loadtxt('k.txt')
l_m = numpy.loadtxt('l.txt')
m_m = numpy.loadtxt('m.txt')
n_m = numpy.loadtxt('n.txt')
o_m = numpy.loadtxt('o.txt')
p_m = numpy.loadtxt('p.txt')
q_m = numpy.loadtxt('q.txt')
r_m = numpy.loadtxt('r.txt')
s_m = numpy.loadtxt('s.txt')
t_m = numpy.loadtxt('t.txt')
u_m = numpy.loadtxt('u.txt')
v_m = numpy.loadtxt('v.txt')
w_m = numpy.loadtxt('w.txt')
x_m = numpy.loadtxt('x.txt')
y_m = numpy.loadtxt('y.txt')
z_m = numpy.loadtxt('z.txt')

#memory = numpy.array([a_m, b_m, c_m, d_m, e_m, f_m, g_m, h_m, i_m, j_m, k_m, l_m, m_m, n_m, o_m, p_m, q_m, r_m, s_m, t_m, u_m, v_m, w_m, x_m, y_m, z_m])



def print_patten(patten):
	for a in range(6):
		print('\n')
		for b in range(10):
			if patten[a,b] > 0:
				sys.stdout.write('##')
			else :
				sys.stdout.write('..')
			pass
		pass
	print('\n')
	pass


def calc_interaction_matrix(memory):
	temp = numpy.zeros((6,10,6,10))
	M = float(memory.shape[0])
	for i in range(6):
		for j in range(10):
			for k in range(6):
				for l in range(10):
					tot = 0
					for m in range(memory.shape[0]):
						tot += memory[m,i,j]*memory[m,k,l]/M
						pass
					temp[i,j,k,l] = tot
					pass
				pass
			pass
		pass
	return temp
	pass

def calc_interaction_energy(patten,J,a,b):
	tot = 0
	for i in range(6):
		for j in range(10):
			tot += - J[a,b,i,j] * patten[a,b] * patten[i,j] 
			pass
		pass
	return tot

def calc_total_energy(patten,J):
	total = 0
	for a in range(6):
		for b in range(10):
			total += calc_interaction_energy(patten,J,a,b)
	return total
	pass

def monte_carlo_sweep(patten, J,n):
	for times in range(n):
		for a in range(6):
			for b in range(10):
				if calc_interaction_energy(patten,J,a,b) > 0:
					print 1
					patten[a,b] = - patten[a,b]
					pass
				pass
			pass
		print_patten(patten)
		print calc_total_energy(patten,J)

def patten_generator(model,error):
	temp2 = model.copy()
	seq = random.sample(range(60),error)
	for i in range(error):
		print seq[i]//10
		print seq[i]%10
		temp2[seq[i]//10 , seq[i]%10] = 0 - temp2[seq[i]//10 , seq[i]%10]
		pass
	pass
	print_patten(model)
	print_patten(temp2)
	return temp2

memory = numpy.array([a_m,m_m,o_m,i_m])
patten_num = 3
patten_error = 5
sweep_times = 1

J = calc_interaction_matrix(memory).copy()

for m in range(memory.shape[0]):
	print calc_total_energy(memory[m],J)

patten_x = patten_generator(memory[patten_num-1],patten_error).copy()

print calc_total_energy(patten_x,J)
monte_carlo_sweep(patten_x,J,sweep_times)

#print_patten(patten_x)

