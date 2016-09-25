#!/usr/bin/env python
#coding=utf-8

import os
import time

path=os.getcwd()
path += "\\ascii"
os.chdir( path )
filelist = os.listdir( path )
#print filelist
for file in filelist:
	f = open(path + '/' + file)
	str = f.read()
	time.sleep(0.02)
	os.system('cls')
	print (str)
