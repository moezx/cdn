import os
from os import listdir
from os.path import isfile, join

path = 'js/'


onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]

str = ''

for f in onlyfiles:
    with open(path + f, 'r') as file:
        data = file.read()
    str = str + data
    print(f)
        
with open("lib.js", "w") as text_file:
    print(str, file=text_file)