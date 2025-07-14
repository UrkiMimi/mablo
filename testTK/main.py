import tkinter as tk
import os, ctypes

# gui part
def mainGUI(root, reason):
    #setup
    win = tk.Tk()
    win.resizable(False,False)
    win.geometry("300x300")
    win.title("The FitnessGram pacer test")

    # first border
    border = tk.Label(win)
    border.pack(pady=30)

    #small text
    smText = tk.Label(win, text='Do I have root?', font=("Arial", 16))
    smText.pack()

    bgText = tk.Label(win, text=root, font=("Arial", 50))
    bgText.pack()

    reasonText = tk.Label(win, text=f'Reason: {reason}')
    reasonText.pack(pady=20)

    # persistence
    win.mainloop()

def raisePrivs():
    try:
        # specify ntdll
        ntdl = ctypes.windll.ntdll

        # adjust privileges to do funny
        funny = ntdl.RtlAdjustPrivilege(19, True, False, ctypes.pointer(ctypes.c_bool()))

        #do the funny
        response = ctypes.c_ulong()
    except:
        print('you win!')

def altCheck():
    try:
        with open("\\Windows\\System32\\balls.sys", "w") as f:
            f.write('hi')
        return True
    except:
        return False
        

# region main program
# vars
#text
reasonTex = ''
rootAcc = 'No.'

# admin
admCheck = ctypes.windll.shell32.IsUserAnAdmin()


### tests
if (os.name == 'nt'):
    # go to next test
    if admCheck:
        rootAcc = 'Yes.'
        reasonTex = 'None. Enjoy your root :D'
    else:
        raisePrivs()
        admCheck = ctypes.windll.shell32.IsUserAnAdmin()

        # redo check
        if altCheck():
            rootAcc = 'Yes.'
            reasonTex = 'Root access as a result of UAC bypass.'
        else:
            reasonTex = "No UAC :("
else:
    reasonTex = "You're using linux, dumbass." 


mainGUI(rootAcc, reasonTex)