#!/usr/bin/env python
#coding=utf-8


import os
import time

step = input('Input the step :\n')

x = 0
y = 35
for i in range(step):
	if( i % 70 < 35 ):
		x += 1
		y -= 1
	else:
		x -= 1
		y += 1
	time.sleep (1./(i+1))
	os.system('cls')
	print (x * ' ' + ' ###   #####  #####  #   #  #####' + y * ' ' + '|')
	print (x * ' ' + '#        #    #      #   #  #    ' + y * ' ' + '|')
	print (x * ' ' + ' ###     #    #####  #   #  #####' + y * ' ' + '|')
	print (x * ' ' + '    #    #    #       # #   #    ' + y * ' ' + '|')
	print (x * ' ' + ' ###     #    #####    #    #####' + y * ' ' + '|')



