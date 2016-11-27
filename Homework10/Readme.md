
# Homework 10
---
##1.摘要
用VPython模拟了引力的平方反比定律失效(![](http://latex.codecogs.com/gif.latex?%5Cbeta%20%3D%201))时，
在不同的初速度下行星的运动轨道。
验证了初始轨道离心率越大时平方反比定律失效后轨道越快地趋向于不稳定。

##2.背景介绍
Kepler三定律是引力的平方反比定律的必然结果，而当平方反比定律失效时，原有的椭圆轨道将变得不稳定。

##3.正文

[完整代码](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework10/homework10.py)

###模型构建

利用VPythong构建恒星与行星的模型。

###运动方程

经典力学给出了在引力作用下行星的运动方程：

![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E%7B_2%7Dx%7D%7Bdt%5E%7B_2%7D%7D%20%3D%20%5Cfrac%7BF_%7BG%2Cx%7D%7D%7BM_E%7D)

![](http://latex.codecogs.com/gif.latex?%5Cfrac%7Bd%5E%7B_2%7Dy%7D%7Bdt%5E%7B_2%7D%7D%20%3D%20%5Cfrac%7BF_%7BG%2Cy%7D%7D%7BM_E%7D)

###算法实现

通过Euler-Cromer方法，并取长度单位为天文单位(AU)，时间单位为年(yr)，得到:

![](http://latex.codecogs.com/gif.latex?r_i%20%3D%20%5Csqrt%7Bx_i%5E%7B_2%7D&plus;y_i%5E%7B_2%7D%7D)

![](http://latex.codecogs.com/gif.latex?v_%7Bx%2Ci&plus;1%7D%20%3D%20v_%7Bx%2Ci%7D%20-%20%5Cfrac%7B4%5Cpi%5E2x_i%7D%7Br_i%5E%7B_3%7D%7D%5CDelta%20t)

![](http://latex.codecogs.com/gif.latex?v_%7By%2Ci&plus;1%7D%20%3D%20v_%7By%2Ci%7D%20-%20%5Cfrac%7B4%5Cpi%5E2y_i%7D%7Br_i%5E%7B_3%7D%7D%5CDelta%20t)

![](http://latex.codecogs.com/gif.latex?x_%7Bi&plus;1%7D%20%3D%20x_i%20&plus;v_%7Bx%2Ci&plus;1%7D%20%5CDelta%20t)

![](http://latex.codecogs.com/gif.latex?y_%7Bi&plus;1%7D%20%3D%20y_i%20&plus;v_%7By%2Ci&plus;1%7D%20%5CDelta%20t)



##4.结果

设初速度为 V0 时轨道为正圆，初速度越小轨迹离心率越大。
    
###VPython 演示

初速度![](http://latex.codecogs.com/gif.latex?V_%7Binit%7D%3D0.95V_0%2C0.9V_0%2C0.8V_0%2C0.7V_0)时，行星运动情况如下：

0.95V0时(1.5倍速)

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework10/0.95(*10).gif)

0.9V0时(1.5倍速)

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework10/0.9(*10).gif)

0.8V0时

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework10/0.8.gif)

0.7V0时

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework10/0.7.gif)

###轨迹图

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework10/Simulation%20of%20elliptical%20orbit:1.0.png)

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework10/Simulation%20of%20elliptical%20orbit:0.95.png)

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework10/Simulation%20of%20elliptical%20orbit:0.9.png)

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework10/Simulation%20of%20elliptical%20orbit:0.8.png)

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework10/Simulation%20of%20elliptical%20orbit:0.7.png)

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework10/Simulation%20of%20elliptical%20orbit:0.5.png)


##5.致谢

代码部分参考了13级刘文焘学长的代码。
