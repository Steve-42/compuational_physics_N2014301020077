# Homework 4
---
##1.摘要
类似于单对象衰变模拟，首先定义原子核衰变的类，然后创建A,B两个对象来模拟A与B之间的转换过程。
##2.正文
###(1)
首先定义一个原子核衰变的 *类* `nuclei_decay`,    
基础代码仿照课堂上的例子，定义了*初始化*`__init__`，*模拟计算*`calculate`， *输出图表*`show_results`，*存储数据*`store_results`等函数.    
通过创建特定对象并调用这些函数可以实现单个种类原子核的模拟.    
###(2)
为了实现 A 与 B 之间的相互转换，在'nuclei_decay'*类* 下附加了两个函数 `step_begin`和`step_end`.

`step_begin`计算单步模拟中原子核衰变个数并赋给`self.dn`.

`step_end`获取参数`delta_N`作为原子核个数改变量并保存结果到字符串.
```python
    def step_begin(self): #计算单步衰变原子核数变化量
        self.dn = - self.n[-1] / self.tau  * self.dt
    def step_end(self, delta_N = 0): #存储单步衰变数据
        self.n.append(self.n[-1] + delta_N)
        self.t.append(self.t[-1] + self.dt)
```
由于A与B相互转换，`a.dn-b.dn`即为A原子核个数变化量`delta_Na`，且`delta_Nb = -delta_Na`
```python
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
```
这样处理的好处在于 A 与 B 对称, 交换A B 并不会影响模拟结果.
###(3)
最后通过调用pylab中的函数绘图输出结果
```python
# 绘图
# 绘图
p1, = plot(a.t,a.n, color = 'blue')
p2, = plot(b.t,b.n, color = 'red')
title('Transformation between A and B')
xlabel('time($s$)')
ylabel('Number of Nuclei')
legend([p1,p2], ['Nuclei A', 'Nuclei B'])
savefig('figure.png')
show()
```
##3.结果
控制台截图

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/%E6%88%AA%E5%9B%BE.bmp)

图表（Na=100,Nb=0）

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework4/figure.png)

图表（Na=50,Nb=150）

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework4/figure2.png)
##4.致谢
代码参考了课上演示的示例.
