#coding=utf8
from pylab import *
#定义 类:原子核衰变
class nuclei_decay:
    def __init__(self, name, number_of_nuclei = 100, time_constant = 1, time_of_duration = 5,time_step = 0.05):
        self.name = name
        self.n = [number_of_nuclei]
        self.t = [0]
        self.tau = time_constant
        self.dt = time_step
        self.dn = 0 # 每一步衰变的个数
        self.time = time_of_duration
        self.nstep = int(time_of_duration // time_step + 1)
        print 'Initial number of nuclei ', self.name, ' ->', self.n[0]
        print 'Time constant ->' , time_constant
        print 'time step -> ' , time_step
        print 'total time -> ' , time_of_duration
    def calculate(self): #单独模拟
        for i in range(self.nstep):
            tmp = self.n[i] - self.n[i] / self.tau * self.dt
            self.n.append(tmp)
            self.t.append(self.t[i] + self.dt)
    def show_results(self): #输出图表
        pl.plot(self.t, self.n)
        pl.xlabel('time ($s$)')
        pl.ylabel('Number of Nuclei' + self.name)
        pl.show()
    def store_results(self): #存储数据
        filename = 'nuclei_'+self.name+'_decay_data.txt'
        file = open(filename, 'w')
        for i in range(len(self.t)):
            print >> file, ' %5.2f\t %10.6f' % (self.t[i],self.n[i])
        file.close()
    def step_begin(self): #计算单步衰变原子核数变化量
        self.dn = - self.n[-1] / self.tau  * self.dt
    def step_end(self, delta_N = 0): #存储单步衰变数据
        self.n.append(self.n[-1] + delta_N)
        self.t.append(self.t[-1] + self.dt)

#含缺省的输入函数
def get(msg,default = 0):
    r = raw_input(msg)
    if r == '':
        return default
    return r
#获取输入值
Na = get('Input the initial number of nuclei A (default: 100):\n',100)
Nb = get('Input the initial number of nuclei B (default: 0):\n',0)
tau_A = get('Input the time constant of nuclei A (default: 1):\n',1)
tau_B = get('Input the time constant of nuclei B (default: 1):\n',1)
t = get('Input the time of duration (default: 5)\n',5)
a = nuclei_decay(name = "A", number_of_nuclei = int(Na), time_constant = int(tau_A), time_of_duration = int(t))
b = nuclei_decay(name = "B", number_of_nuclei = int(Nb), time_constant = int(tau_B), time_of_duration = int(t))
#模拟衰变过程
for i in range(a.nstep): 
    a.step_begin()
    b.step_begin()
    delta_Na = a.dn - b.dn
    delta_Nb = -delta_Na
    a.step_end(delta_N = delta_Na)
    b.step_end(delta_N = delta_Nb)
a.store_results()
b.store_results()
# 绘图
p1, = plot(a.t,a.n, color = 'blue')
p2, = plot(b.t,b.n, color = 'red')
title('Transformation between A and B')
xlabel('time($s$)')
ylabel('Number of Nuclei')
legend([p1,p2], ['Nuclei A', 'Nuclei B'])
savefig('figure.png')
show()

