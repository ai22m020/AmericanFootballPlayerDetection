from os import listdir
from os.path import isfile, join

# Purpose of this class is to extract the player labels from shared project, so numers are not included anymore

folders = ["../American-Football-Player/test/labels"
          ,"../American-Football-Player/valid/labels",
           "../American-Football-Player/train/labels"
           ]

for folder in folders:
    onlyfiles = [f for f in listdir(folder) if isfile(join(folder, f))]
    for fileName in onlyfiles:
        newLines = []
        with open(file=folder+'/'+fileName, encoding='utf8') as f:
            for line in f:
                parts = line.split(" ")
                if parts[0] == "5" or parts[0] == "7" or parts[0] == "8":
                    newLines.append(line)
        f = open(folder+'/'+fileName, "r+")
        f.truncate(0)
        for newLine in newLines:
            f.write(newLine)
        with open(folder+'/'+fileName) as f_input:
            data = f_input.read().rstrip('\n')
        with open(folder+'/'+fileName, 'w') as f_output:
            f_output.write(data)
        f.close()



