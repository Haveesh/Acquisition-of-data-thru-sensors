import pyautogui, sys,time
from flask import Flask
from flask import  session
import sys
import time

log= sys.argv[1]
starttime = sys.argv[2]
endtime=sys.argv[3]


time.sleep(3)

starttime=0
endtime= 1739233
app = Flask(__name__)
#"C:\Users\C-C\PycharmProjects\mouse\subjects\\321$2017-04-24\\321quiz001.txt"
with open(log, "r") as ins:
    array = []
    for line in ins:
        array.append(line)

spl=[]
for i in array:
    spl.append(i.split(';'))
msg=[]
pos=[]
newpos=[]
msg.append([x[0] for x in spl])
msg.append([x[1] for x in spl])
msg.append([x[2] for x in spl])


pos=list(msg[2])
ntime=list(msg[1])
msgn= list(msg[0])

first=int(ntime[0])
ntime = list(map(lambda x: int(x)- first, ntime))

i=[ n for n,i in enumerate(ntime) if i>int(starttime) ][0]

end=[ n for n,z in enumerate(ntime) if z>int(endtime) ][0]


for x in pos:
    if(len(x)>2):
        newpos.append(x[1:-2])
    else:
        newpos.append(x[:-1])
fpos=[]
for x in newpos:
    if (x=="em_Perio"):
        fpos.append(".")
    elif (x=="em_"):
        fpos.append(":")
    elif (x=="etur"):
        fpos.append("enter")
    else:
        fpos.append(x)

print "i=",i
print "end=",end


while(i<end):
    print i
    if(msgn[i]=="mouse move"):
      xc,yc= fpos[i].split(",")
      xc = int(xc)
      yc = int(yc[1:])
      pyautogui.moveTo(xc,yc)
      i=i+1
      #time.sleep(delay)

    elif (msgn[i]=="mouse left down" and msgn[i+1] != "mouse left up"):

        i=i+1
        while(msgn[i]!="mouse left up"):
            print i
            delay = float(int(ntime[i + 1]) - int(ntime[i])) / 1000
            xc, yc = fpos[i].split(",")
            xc = int(xc)
            yc = int(yc[1:])
            pyautogui.dragTo(xc,yc,button="left")
            i=i+1

        print i
        if (msgn[i] == "mouse left up"):
            print "mouse upp now"
            i=i+1

        #time.sleep(delay)

    elif (msgn[i]=="mouse left down" and msgn[i+1]=="mouse left up"):

        xc, yc = fpos[i].split(",")
        xc=int(xc)
        yc=int(yc[1:])
        pyautogui.click()
        i=i+2
       # time.sleep(delay)

    elif (msgn[i] == "mouse right down" and msgn[i+1] == "mouse right up"):
        print i
        xc, yc = fpos[i].split(",")
        pyautogui.click()
        i = i + 2
     #   time.sleep(delay)

    elif (msgn[i]=="key down"):
        if(fpos[i]=="shif"):
            key= fpos[i+1]
            pyautogui.keyDown("shift")
            pyautogui.press(key)
            print ("pressed key :", pos[i])
            i=i+2

        else:
            pyautogui.press(fpos[i])
            print ("pressed key :",fpos[i])
            i=i+1
        #time.sleep(delay)

    else:
        i=i+1
        print "none of them"


