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



def print_pattern(pattern):
	for a in range(6):
		print('\n')
		for b in range(10):
			if pattern[a,b] > 0:
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

def calc_interaction_energy(pattern,J_x,a,b):
	tot = 0
	for i in range(6):
		for j in range(10):
			tot += - J_x[a,b,i,j] * pattern[a,b] * pattern[i,j] 
			pass
		pass
	return tot

def calc_total_energy(pattern,J_x):
	total = 0
	for a in range(6):
		for b in range(10):
			total += calc_interaction_energy(pattern,J_x,a,b)
	return total
	pass

def monte_carlo_sweep(pattern, J,n):
	for times in range(n):
		for a in range(6):
			for b in range(10):
				if calc_interaction_energy(pattern,J,a,b) > 0:
					sys.stdout.write(' * ')
					pattern[a,b] = - pattern[a,b]
					pass
				pass
			pass
		print_pattern(pattern)
		print calc_total_energy(pattern,J)

def pattern_generator(model,error):
	temp2 = model.copy()
	seq = random.sample(range(60),error)
	for i in range(error):
		temp2[seq[i]//10 , seq[i]%10] = 0 - temp2[seq[i]//10 , seq[i]%10]
		pass
	pass
	print_pattern(model)
	print_pattern(temp2)
	return temp2

def interaction_damage(J,rate,J_new):
	seq = random.sample(range(int(J.size)),int(J.size * rate))
	J_new.resize((1,1,1,J.size))
	for i in range(len(seq)):
		J_new[0,0,0,seq[i]] = 0
		pass
	J_new.resize(J.shape)
	return J_new

#参数设置
memory = numpy.array([a_m,i_m,o_m])
pattern_num = 1
pattern_error = 5
sweep_times = 5
damage_rate = 0.9

#计算相互作用能矩阵
J = calc_interaction_matrix(memory).copy()

#计算几个所存储的pattern各自的能量
for m in range(memory.shape[0]):
	sys.stdout.write('total energy = ')
	print calc_total_energy(memory[m],J)

#清除相互作用能矩阵的部分元素
J_new = J.copy()
seq = random.sample(range(int(J.size)),int(J.size * damage_rate))
J_new.resize((1,1,1,J.size))
for i in range(len(seq)):
	J_new[0,0,0,seq[i]] = 0
	pass
J_new.resize(J.shape)
print J_new.shape

#生成一个扰动后的pattern
pattern_x = pattern_generator(memory[pattern_num-1],pattern_error).copy()

#计算几个所存储的pattern各自的能量
for m in range(memory.shape[0]):
	sys.stdout.write('total energy now = ')
	print calc_total_energy(memory[m],J_new)

#对pattern进行蒙卡迭代
print calc_total_energy(pattern_x,J_new)
monte_carlo_sweep(pattern_x,J_new,sweep_times)

#print_pattern(pattern_x)

