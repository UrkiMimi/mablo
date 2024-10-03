### Unused test file for the corruption algorithm
import random as rand

with open('testFile.bmp','rb') as bFile:
    arrayList = list(bFile.read())


# This try and except thing is pretty stupid since this shouldn't go out of range but I'm still adding it here
#This for loop swaps values with neighboring ones
try:
    for i in range(round(len(arrayList)/10)):
        arrayList[rand.randint(0,len(arrayList)-1)] = rand.choice(arrayList)
except:
    print('failed to shift file')

#convert b64 list to string
byteArray = bytearray(arrayList)

#export file
finalFile = open('testRuined.bmp', 'wb')
finalFile.write(bytes(byteArray))
finalFile.close()