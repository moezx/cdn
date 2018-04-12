import os
from os import listdir
from os.path import isfile, join

pathJS = 'js/'
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
        
with open("lib.js", "w") as text_file:
    print(strJS, file=text_file)
    
    
print('CSS############################')
    
for f in cssfiles:
    with open(pathCSS + f, 'r') as file:
        data = file.read()
    strCSS = strCSS + data
    print(f)
        
with open("css/lib.css", "w") as text_file:
    print(strCSS, file=text_file)
    
print('Done')