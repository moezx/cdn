# coding: utf-8
'''
Created on Apr 12, 2018
Update  on 2018-04-13
@author: Mashiro @ https://2heng.xin

Desc: Auto compress & minfy JavaScript codes and CSS style sheet
'''
import os
from os import listdir
from os.path import isfile, join
from jsmin import jsmin
from csscompressor import compress

pathJS = 'js/src/'
pathJSroot = 'js/'
pathCSS = 'css/src/'
pathCSSroot = 'css/'

jsfiles = [f for f in listdir(pathJS) if isfile(join(pathJS, f))]
cssfiles = [f for f in listdir(pathCSS) if isfile(join(pathCSS, f))]

strJS = ''
strCSS = ''

for f in jsfiles:
    with open(pathJS + f, 'r') as file:
        data = file.read()
    strJS = strJS + data
    print(f)
        
JSminified = jsmin(strJS)
        
with open(pathJSroot + "lib.js", "w") as text_file:
    print(JSminified, file=text_file)
    
    
print('------------------JS Done------------------')
    
for f in cssfiles:
    with open(pathCSS + f, 'r') as file:
        data = file.read()
    strCSS = strCSS + data
    print(f)
      
CSSminified = compress(strCSS)
      
with open(pathCSSroot + "lib.css", "w") as text_file:
    print(CSSminified, file=text_file)
    
print('------------------CSS Done------------------')

key = input('Press any key to quit') 
quit()