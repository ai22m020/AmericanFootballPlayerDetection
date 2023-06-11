from os import listdir
from os.path import isfile, join
from PIL import Image
import os, sys

# Resize player images
path = "../../MegaFootballPlayer-3/train/images/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((640,640), Image.ANTIALIAS)
            imResize.save(f + '.jpg', 'JPEG', quality=90)

resize()


def join_string(list_string):
    # Join the string based on '-' delimiter
    string = ' '.join(list_string)

    return string

folder = "../American-Football-Player/test/labels"
#
#
onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
for fileName in onlyfiles:
    newLines = []
    with open(file=folder+'/'+fileName, encoding='utf8') as f:
        for line in f:
            newLine = ""
            parts = line.split(" ")
            if parts[0] == "5":
                parts[0] = "0"
                newLine = join_string(parts)
                newLines.append(newLine)
            elif parts[0] == "7":
                parts[0] = "1"
                newLine = join_string(parts)
                newLines.append(newLine)
            elif parts[0] == "8":
                parts[0] = "2"
                newLine = join_string(parts)
                newLines.append(newLine)

    f = open(folder+'/'+fileName, "r+")
    f.truncate(0)
    for newLine in newLines:
        f.write(newLine)
    f.close()
