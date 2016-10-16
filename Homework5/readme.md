# Homework 5
---
##1.摘要
用Euler法模拟了炮弹在 仅考虑重力/考虑空气阻力/考虑非均匀空气密度 三种情况下的运动路径, 并分别求了不同初始角度下的射程.

##2.背景介绍
炮弹的运动微分方程:

![](http://latex.codecogs.com/gif.latex?%5Cdfrac%20%7Bd%5E%7B2%7Dx%7D%7Bdt%5E%7B2%7D%7D%3Da_x%3D%5Cdfrac%20%7BF_%7Bdrag%2Cx%7D%7D%7Bm%7D)

![](http://latex.codecogs.com/gif.latex?%5Cdfrac%20%7Bd%5E%7B2%7Dy%7D%7Bdt%5E%7B2%7D%7D%3Da_y%3D%5Cdfrac%20%7BF_%7Bdrag%2Cy%7D%7D%7Bm%7D%20-%20g)

###(1)不考虑空气阻力时

![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%2Cx%7D%20%3D%200)

![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%2Cy%7D%20%3D%200)

###(2)考虑均匀空气的阻力：

![](http://latex.codecogs.com/gif.latex?%5Cfrac%7BF_%7Bdrag%2Cx%7D%20%7D%7Bm%7D%3D%20-%20%5Cfrac%7BB_2%7D%7Bm%7D%7Bv_x%7Dv)

![](http://latex.codecogs.com/gif.latex?%5Cfrac%7BF_%7Bdrag%2Cy%7D%20%7D%7Bm%7D%3D%20-%20%5Cfrac%7BB_2%7D%7Bm%7D%7Bv_y%7Dv)

###(3)考虑空气阻力随高度变化：

![](http://latex.codecogs.com/gif.latex?%5Cfrac%7BF_%7Bdrag%2Cx%7D%20%7D%7Bm%7D%3D%20-%20%5Cfrac%7BB_2%7D%7Bm%7D%7Bv_x%7Dv%5Ccdot%20exp%28%5Cfrac%7B-%20y%7D%7By_0%7D%29)

![](http://latex.codecogs.com/gif.latex?%5Cfrac%7BF_%7Bdrag%2Cy%7D%20%7D%7Bm%7D%3D%20-%20%5Cfrac%7BB_2%7D%7Bm%7D%7Bv_y%7Dv%5Ccdot%20exp%28%5Cfrac%7B-%20y%7D%7By_0%7D%29)

##3.正文

使用Euler法计算炮弹运动轨迹

![](http://latex.codecogs.com/gif.latex?x_%7Bi&plus;1%7D%20%3D%20x_i%20&plus;%20v_%7Bx%2Ci%7D%20dt)

![](http://latex.codecogs.com/gif.latex?y_%7Bi&plus;1%7D%20%3D%20y_i%20&plus;%20v_%7By%2Ci%7D%20dt)

![](http://latex.codecogs.com/gif.latex?v_%7Bx%2Ci&plus;1%7D%20%3D%20v_%7Bx%2Ci%7D%20&plus;%20a_%7Bx%2Ci%7D%20dt)

![](http://latex.codecogs.com/gif.latex?v_%7By%2Ci&plus;1%7D%20%3D%20v_%7By%2Ci%7D%20&plus;%20a_%7By%2Ci%7D%20dt)

[完整代码](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework5/homework5.py)

##4.结果

###(1)三种模拟方式对比

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework5/Cannon%20shell%20trajectory.png)

###(2)计算不同初始角度下的射程

不考虑空气阻力：

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework5/Cannon%20shell%20trajectory%20without%20air%20drag%20(different%20angles).png)

考虑均匀密度的空气：

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework5/Cannon%20shell%20trajectory%20with%20air%20drag%20(different%20angles).png)

考虑密度随高度变化的空气：

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework5/Cannon%20shell%20trajectory%20with%20air%20density%20correction%20(different%20angles).png)
