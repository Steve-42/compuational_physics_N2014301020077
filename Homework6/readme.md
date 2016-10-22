# Homework 5
---
##1.摘要
用Euler法模拟了炮弹在    
(1)考虑绝热模型的空气阻力   
(2)考虑迎面风速   
(3)考虑海拔差异    
三种情况下的运动路径, 并分别求了不同初始角度下的射程.

##2.背景介绍
炮弹的运动微分方程:

![](http://latex.codecogs.com/gif.latex?%5Cdfrac%20%7Bd%5E%7B2%7Dx%7D%7Bdt%5E%7B2%7D%7D%3Da_x%3D%5Cdfrac%20%7BF_%7Bdrag%2Cx%7D%7D%7Bm%7D)

![](http://latex.codecogs.com/gif.latex?%5Cdfrac%20%7Bd%5E%7B2%7Dy%7D%7Bdt%5E%7B2%7D%7D%3Da_y%3D%5Cdfrac%20%7BF_%7Bdrag%2Cy%7D%7D%7Bm%7D%20-%20g)

考虑绝热模型下的空气阻力

![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%2Cx%7D%3D-B_%7B2%7Dvv_%7Bx%7D%5Cfrac%7B%5Crho%20%7D%7B%5Crho_0%7D%3D-B_%7B2%7Dvv_%7Bx%7D%281-%5Cfrac%7Bay%7D%7BT_0%7D%29%5E%7B%5Calpha%7D)

![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%2Cy%7D%3D-B_%7B2%7Dvv_%7By%7D%5Cfrac%7B%5Crho%20%7D%7B%5Crho_0%7D%3D-B_%7B2%7Dvv_%7By%7D%281-%5Cfrac%7Bay%7D%7BT_0%7D%29%5E%7B%5Calpha%7D)

由于存在迎面风速，将式中 v_x 替换为 (v_x - v_wind):

![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%2Cx%7D%3D-B_%7B2%7Dv%28v_%7Bx%7D-v_%7Bwind%7D%29%5Cfrac%7B%5Crho%20%7D%7B%5Crho_0%7D%3D-B_%7B2%7Dv%28v_%7Bx%7D-v_%7Bwind%7D%29%281-%5Cfrac%7Bay%7D%7BT_0%7D%29%5E%7B%5Calpha%7D)

![](http://latex.codecogs.com/gif.latex?F_%7Bdrag%2Cy%7D%3D-B_%7B2%7Dvv_%7By%7D%5Cfrac%7B%5Crho%20%7D%7B%5Crho_0%7D%3D-B_%7B2%7Dvv_%7By%7D%281-%5Cfrac%7Bay%7D%7BT_0%7D%29%5E%7B%5Calpha%7D)







##3.正文

使用Euler法计算炮弹运动轨迹

![](http://latex.codecogs.com/gif.latex?x_%7Bi&plus;1%7D%20%3D%20x_i%20&plus;%20v_%7Bx%2Ci%7D%20dt)

![](http://latex.codecogs.com/gif.latex?y_%7Bi&plus;1%7D%20%3D%20y_i%20&plus;%20v_%7By%2Ci%7D%20dt)

![](http://latex.codecogs.com/gif.latex?v_%7Bx%2Ci&plus;1%7D%20%3D%20v_%7Bx%2Ci%7D%20&plus;%20a_%7Bx%2Ci%7D%20dt)

![](http://latex.codecogs.com/gif.latex?v_%7By%2Ci&plus;1%7D%20%3D%20v_%7By%2Ci%7D%20&plus;%20a_%7By%2Ci%7D%20dt)

[完整代码]()

##4.结果

