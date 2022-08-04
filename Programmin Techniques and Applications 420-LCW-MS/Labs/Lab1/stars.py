file = open('/Users/gordonng/Documents/Cegep/Programming/Labs/Lab1/stars.txt')
starStorage = {}
starSorter = []
for line in file:
    tempData = line.split()
    starStorage[tempData[1]] = tempData[4]
    starSorter.append([tempData[4],tempData[1]])


starSorter.sort()
print(starSorter[:-6:-1])
    


