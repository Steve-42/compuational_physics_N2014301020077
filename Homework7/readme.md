# Homework 7
---
##1.摘要
用Euler-cromer法模拟了含驱动力及阻尼的物理摆，并画出了运动的庞加莱截面(Poincare section)

##2.背景介绍
物理摆的运动微分方程:

![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%20%5Comega%7D%7Bdt%7D%3D-%20%5Cfrac%7Bg%7D%7Bl%7Dsin%28%5Ctheta%29-q%20%5Cfrac%7Bd%5Ctheta%7D%7Bdt%7D&plus;F_D%20sin%28%5COmega_d%20t%29)

![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5Ctheta%7D%7Bdt%7D%3D%5Comega)

##3.正文

[完整代码](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework7/homework7.py)

使用Euler-cromer法计算物理摆运动轨迹：

![](http://latex.codecogs.com/gif.latex?%5Comega_%7Bi&plus;1%7D%3D%5Comega_i&plus;%5B-%28g/l%29sin%5Ctheta_i-q%5Comega_i&plus;F_Dsin%28%5COmega_Dt_i%29%5D%5CDelta%20t)

![](http://latex.codecogs.com/gif.latex?%5Ctheta_%7Bi&plus;1%7D%3D%5Ctheta_i&plus;%5Comega_%7Bi&plus;1%7D%5CDelta%20t)

如果![](http://latex.codecogs.com/gif.latex?%5Ctheta_%7Bi&plus;1%7D)超过范围![](http://latex.codecogs.com/gif.latex?%5B-%20%5Cpi%2C%5Cpi%5D)，
令其加（或减）![](http://latex.codecogs.com/gif.latex?2%5Cpi)

![](http://latex.codecogs.com/gif.latex?t_%7Bi&plus;1%7D%3Dt_i%20&plus;%5CDelta%20t)

循环执行

##4.结果

模拟时间为5000秒

![](http://latex.codecogs.com/gif.latex?g%3D9.8%2C%20l%3D9.8%20%2C%20F_D%3D1.2%2C%20%5COmega_D%3D2/3)

对于所有对应![](http://latex.codecogs.com/gif.latex?t%5Capprox%202%5Cpi%20n/%5COmega%20_D)的点，绘图如下

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework7/Poincare%20section%20of%20the%20pendulum.png)

对于所有对应![](http://latex.codecogs.com/gif.latex?t%5Capprox%20%282%5Cpi%20n%20&plus;%5Cfrac%7B%5Cpi%7D%7B4%7D%29/%5COmega%20_D)的点，绘图如下

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework7/Poincare%20section%20of%20the%20pendulum2.png)

