import fileinput
text = "t8.shakespeare.txt"
newDict = {}
with open('frenchdic.txt', 'r') as f:
        for line in f:
            splitLine = line.split()
            newDict[str(splitLine[0])] = ",".join(splitLine[1:])
for line in fileinput.input(text, inplace=True):
    line = line.rstrip()
    for field in newDict:
        if field in line:
            line = line.replace(field, newDict[field])

    print (line)
