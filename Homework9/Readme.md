
# Homework 9
---
##1.摘要
用VPython模拟了小球在方形边框内中间存在环形墙壁时的运动状况，对不同的环形墙壁半径及是否偏离中心作了讨论，并用VPython作了简单演示。

##2.背景介绍
小球在规则的正方形边框内做无耗散的匀速运动时，将以不同的初速度和初始位置得到不同的固定轨迹。
在有微小扰动的情况下，在固定纵坐标时![](http://latex.codecogs.com/gif.latex?v_x)的值将保持不变；而小球在规则的圆形边框内做无耗散匀速运动时，
也具有稳定的![](http://latex.codecogs.com/gif.latex?v_x%20-%20x)相图，
而当圆形渐渐趋于田径场形状（对称性破坏）时，其相图趋于混沌。

##3.正文

[完整代码](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework9/homework9.py)

###模型构建

小球，边框等的模拟调用python-visual中的函数即可实现。

###边框碰撞修正

设正方形中心位置为坐标原点，以右边框为例，当检测到小球x位置ball.pos.x大于右边框x坐标table_right.x时，
小球的正确位置应该位于右边框镜像对称位置，位置修正为ball.pos.x = 2 * table_right.x - ball.pos.x，
速度修正为ball.velocity.x = -ball.velocity.x

###圆环碰撞修正

详见源码functionfixCollision(obj, pos)


##4.结果

简单的VPython演示

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework9/c.gif)

对于不同的圆环半径(![](http://latex.codecogs.com/gif.latex?radius)),
以及是否偏移中心(![](http://latex.codecogs.com/gif.latex?%5Calpha)),
相图如下：

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework9/billiard_0.0_0.0.png)

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework9/billiard_0.0_5.0.png)

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework9/billiard_0.1_5.0.png)

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework9/billiard_0.0_10.0.png)

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework9/billiard_0.1_10.0.png)

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework9/billiard_0.0_20.0.png)

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework9/billiard_0.1_20.0.png)

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework9/billiard_0.0_50.0.png)

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework9/billiard_0.1_50.0.png)

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework9/billiard_0.0_80.0.png)

![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework9/billiard_0.1_80.0.png)

##5.致谢

代码部分参考了13级刘文焘学长的代码。
