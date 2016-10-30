# Homework 7
---
##1.摘要
用Euler-cromer法模拟了含驱动力及阻尼的物理摆，并画出了运动的庞加莱截面(Poincare section)

##2.背景介绍
物理摆的运动微分方程:

![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%20%5Comega%7D%7Bdt%7D%3D-%20%5Cfrac%7Bg%7D%7Bl%7Dsin%28%5Ctheta%29-q%20%5Cfrac%7Bd%5Ctheta%7D%7Bdt%7D&plus;F_D%20sin%28%5COmega_d%20t%29)

![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5Ctheta%7D%7Bdt%7D%3D%5Comega)

##3.正文

使用Euler-cromer法计算物理摆运动轨迹：

![](http://latex.codecogs.com/gif.latex?%5Comega_%7Bi&plus;1%7D%3D%5Comega_i-%5B%5Cfrac%7Bg%7D%7Bl%7Dsin%5Ctheta_i%20-q%5Comega_i%20&plus;F_Dsin%28%5COmega_Dt_i%29%5D%5CDelta%20t)

![](http://latex.codecogs.com/gif.latex?%5Ctheta_%7Bi&plus;1%7D%3D%5Ctheta_i&plus;%5Comega_%7Bi&plus;1%7D%5CDelta%20t)

如果![](http://latex.codecogs.com/gif.latex?%5Ctheta_%7Bi&plus;1%7D)超过范围![](http://latex.codecogs.com/gif.latex?%5B-%20%5Cpi%2C%5Cpi%5D)，
令其加（或减）![](http://latex.codecogs.com/gif.latex?2%5Cpi)

![](http://latex.codecogs.com/gif.latex?t_%7Bi&plus;1%7D%3Dt_i%20&plus;%5CDelta%20t)

循环执行

##4.结果

