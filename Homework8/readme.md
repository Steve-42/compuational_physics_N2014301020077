# Homework 8
---
##1.摘要
用Euler-cromer法模拟了含驱动力及阻尼的物理摆，并画出了不同阻尼下运动的分岔图(Bifurcation diagram)

##2.背景介绍
物理摆的运动微分方程:

![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%20%5Comega%7D%7Bdt%7D%3D-%20%5Cfrac%7Bg%7D%7Bl%7Dsin%28%5Ctheta%29-q%20%5Cfrac%7Bd%5Ctheta%7D%7Bdt%7D&plus;F_D%20sin%28%5COmega_d%20t%29)

![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5Ctheta%7D%7Bdt%7D%3D%5Comega)

##3.正文

[完整代码](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework8/homework8.py)

使用Euler-cromer法计算物理摆运动轨迹：

![](http://latex.codecogs.com/gif.latex?%5Comega_%7Bi&plus;1%7D%3D%5Comega_i&plus;%5B-%28g/l%29sin%5Ctheta_i-q%5Comega_i&plus;F_Dsin%28%5COmega_Dt_i%29%5D%5CDelta%20t)

![](http://latex.codecogs.com/gif.latex?%5Ctheta_%7Bi&plus;1%7D%3D%5Ctheta_i&plus;%5Comega_%7Bi&plus;1%7D%5CDelta%20t)

如果![](http://latex.codecogs.com/gif.latex?%5Ctheta_%7Bi&plus;1%7D)超过范围![](http://latex.codecogs.com/gif.latex?%5B-%20%5Cpi%2C%5Cpi%5D)，
令其加（或减）![](http://latex.codecogs.com/gif.latex?2%5Cpi)

![](http://latex.codecogs.com/gif.latex?t_%7Bi&plus;1%7D%3Dt_i%20&plus;%5CDelta%20t)

循环执行

对不同的阻尼分别计算并汇总作图

##4.结果

分岔图如下：

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework8/Bifurcation%20diagram.png)
