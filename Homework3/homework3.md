# Homework 3
---
##1.摘要
通过调用延时函数实现了字符画面的移动，并通过调用PIL模块中的图像处理函数实现了将简单动画转换为字符动画。
##2.背景介绍
作业要求：
作业L1 在屏幕上让你的英文名字水平移动起来
作业L2 在80*80点阵上用字符拼出你想画的东西，并让它旋转起来，希望脑洞大开！（比如字符、火柴人、火箭等等）
##3.正文
###(1)
对于作业L1，可以通过在字符画前添加空格' '实现字符画位置的变化。
再通过循环结构使每一帧中的空格数量依次增加或减少即可实现字符画的左右移动。
通过每一帧之间延时时间长度的变化可实现平移速度的变化。
见 [L1.py](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework3/L1.py)
###(2)
对于作业L2，尝试了直接将视频文件转化为字符动画。
首先将视频文件通过软件抓帧并依次保存为 320＊240 的bmp图片。
再通过调用PIL模块中的图像处理命令将图片转换为8-bit灰度图片，
读取每个单位(2*3像素)的平均灰度值，并按灰度值大小分别转换成"#&$*+:. "，
将转换后的字符依次存储于字符串 pic_str ，即为对应的8级灰度字符画。
对每一帧图片均转换为字符画并存储为txt文件(横160字符/纵80字符)，
存储于同目录下的ascii文件夹中。

见 [bmp_to_ascii.py](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework3/bmp_to_ascii.py)


再通过循环语句加延时函数依次打开每一帧txt文件，即可再控制台显示转换完成的字符动画

见 [play.py](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework3/play.py)

PS:
1. 由于控制台中的字符长宽不等，若严格按照80*80点阵得到的是细长的图像，故采用160*80
2. 原视频文件为 30帧/s ，但由于sleep函数精确度不佳再加上打开每一帧字符画需要时间，
故实际帧数飘忽不定Orz
3. 找视频的时候忘了原作业要求是旋转，不过好在视频结尾有一段太极图旋转的动画，
也算是完成了要求吧XD

##4.结果
![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework3/screenshot1.png)
![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework3/screenshot2.png)
![](https://github.com/Steve-42/compuational_physics_N2014301020077/blob/master/Homework3/screenshot3.png)
