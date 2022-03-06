# 
import sys
import pyautogui
import time
import pyperclip

def log(tolog):
    with open("..\\WorkFlow\\"+TASKNAME+"\\"+TASKNAME+".log",'a') as f:
        f.write(tolog)


def findLocation(img,conf):
    location = pyautogui.locateCenterOnScreen(img,confidence=conf) # confidence=0.9
    if location :
        print(img,location.x, location.y)
        return(location)
    else:
        return(0)


def mouseClick(img, LR, clicktimes,shiftx, shifty):
    location = findLocation(img,0.9)
    if location:
        pyautogui.click(location.x+shiftx, location.y+shifty, clicks=clicktimes, interval=0.2, duration=0.2,button=LR)
    else:
        log(img+" not found\n")
    time.sleep(0.8)


def judgeClick(img1, img2, LR, clicktimes,shiftx, shifty):
    location1 = findLocation(img1,0.9)
    if location1:
        return()
    else:
        mouseClick(img2,LR, clicktimes,shiftx, shifty)
    time.sleep(0.8)


def inputValue(value):
    pyperclip.copy(value)
    pyautogui.hotkey('ctrl','v')
    time.sleep(0.8)

def pressKey(key):
    pyautogui.press(key) # "enter"


def runList(inputlist):
    working_dir="..\\WorkFlow\\"+TASKNAME+"\\"
    listlen=len(inputlist)
    i=-1
    while i < listlen-1:
        i += 1 
        line=inputlist[i].strip().split()    # get str  and  remove \n whitespace  and  split
        if line==[]:    # skip empty line
            continue

        if line[0] == "Loop":
            try:
                last_end = listlen - inputlist[::-1].index("End\n") - 1    # last "End" line number
            except ValueError:
                log("Loop without End\n")
                return()
            #print(inputlist[i+1: last_end])
            for j in range(int(line[1])):
                runList(inputlist[i+1: last_end])
            i=last_end
        elif line[0] == 'Wait':
            time.sleep(float(line[1]))
        elif line[0] == 'Click':
            mouseClick(working_dir+line[1], line[2], int(line[3]), int(line[4]), int(line[5]))
        elif line[0] == 'Judgeclick':
            judgeClick(working_dir+line[1], working_dir+line[2], line[3], int(line[4]), int(line[5]), int(line[6]))
        elif line[0] == 'Input':
            inputValue(line[1])
        elif line[0] == 'Key':
            pressKey(line[1])
        elif line[0] == 'Halt':
            h=input("Press any key to continue")
        elif line[0][0]=="#":
            continue
        else:
            log("Check your list file")
        

def main():
    try:   
        global TASKNAME
        TASKNAME=sys.argv[1]
        log("\n%s\n%s   Flow Name: %s\n"%("-"*30,time.strftime("%Y-%m-%d %H:%M:%S"),TASKNAME))
        f=open("..\\WorkFlow\\"+TASKNAME+"\\"+TASKNAME+".list",'r')
        print("111")
        runList(f.readlines())
        
        log("Executed to end\n%s\n"%("-"*30))
    except FileNotFoundError:
        log("No Flow or *.list file found\n")
    except KeyboardInterrupt:
        log("Keyboard Interrupted\n")


if __name__ == "__main__":
    main()
