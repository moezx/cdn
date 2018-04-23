#coding=utf-8
from PIL import Image
import os
from os import listdir
from os.path import isfile, join
import datetime

def convert_to_webp(filename):
    im = Image.open('gallary/' + filename).convert("RGB")
    im.save('webp/' + filename + ".webp", "WEBP")

# Get Date
now = datetime.datetime.now()

mypath = 'gallary'

# Get a list of all file names
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
#print(str(onlyfiles))

id = 1

for f in onlyfiles:
    convert_to_webp(f)
    print(str(id) + '/' + str(len(onlyfiles)))
    id += 1
	
print('Done.')

key = input('Press any key to quit') 
quit()