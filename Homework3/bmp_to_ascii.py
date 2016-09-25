#!/usr/bin/env python
#coding=utf-8

#宽度 = 160 字符
#高度 = 80 字符 

from PIL import Image
import os

def ImageAscii(filepath):
    img = Image.open(filepath)
    img = img.convert('L')
    pix = img.load()
    width , height = img.size
    pic_str = ''
    for h in xrange(0,height,3):
        for w in xrange(0,width,2):
            p = pix[w,h]+pix[w,h+1]+pix[w,h+2]+pix[w+1,h]+pix[w+1,h+1]+pix[w+1,h+2]
            p = p / 6
            if (int(p) > 224):
		        pic_str += '#'
            elif (int(p) > 192):
				pic_str += '&'
            elif (int(p) > 160):
				pic_str += '$'
            elif (int(p) > 128):
				pic_str += '*'
            elif (int(p) > 96):
				pic_str += '+'
            elif (int(p) > 64):
				pic_str += ':'
            elif (int(p) > 32):
				pic_str += '.'
            else:
                pic_str += ' '
        pic_str += '\n'
    return pic_str

def save_txt(filename, pic_str):
	outfile = open(filename,'w')
	outfile.write(pic_str)
	outfile.close()


capturefolder = raw_input('Please input your BMP(320*240) file path:\n----End with "/"----\n')
#capturefolder = "C:/Users/think/Desktop/Workshop/images/"
filetype = "bmp"

filelist = os.listdir(capturefolder)
path=os.getcwd()
os.mkdir( path + "\\ascii" )
os.chdir( path + "\\ascii" )
for file in filelist:
	if file.split('.')[1] == filetype:
		img_str = ImageAscii(capturefolder + file)
		os.system('cls')
		print('saving file', file)
		save_txt(file.split('.')[0] + '.txt' , img_str)
		
print '---Done!---'
