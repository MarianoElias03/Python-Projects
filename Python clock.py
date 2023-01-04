import datetime
from datetime import time, datetime
from time import strftime
from tkinter import *
import time as t
from tkinter import messagebox

def clock():
    current_time = datetime.datetime.now().strftime("%H: %M: %S")
def showFrame(frame):
    frame.tkraise()

now = datetime.now()

hours = 0
minutes = 0
seconds = 0
milliseconds = 0



currentTime= '%02d:%02d:%02d' % (now.hour, now.minute, now.second)

#root layout
root = Tk()
root.geometry('900x500')
root.title("Python Clock")
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)

countHour =StringVar()
countMinute =StringVar()
countSecond =StringVar()

countHour2 = 0
countMinute2 = 0
countSecond2 = 0

countHour.set('00')
countMinute.set('00')
countSecond.set('00')

#clock pages
clockFace = Frame(root, bg='black' )
timerFace = Frame(root, bg='red')
countDown = Frame(root, bg='blue')
for frame in (clockFace, timerFace, countDown):
    frame.grid(row=0, column=0, sticky='nsew')
#======clockFace stuff (DONE)
clockFaceTitle = Label(clockFace, text='current time', bg='white').pack(fill='x')
clockFaceBtn = Button(clockFace, height=2, width=10, text='Clock', bg='white', command=lambda: showFrame(clockFace)).place(x=50, y=425)
timerBtn = Button(clockFace, height=2, width=10, text='Timer', bg='white', command=lambda: showFrame(timerFace)).place(x=400, y=425)
countDownBtn=Button(clockFace, height=2, width=10, text='Countdown', bg='white', command=lambda: showFrame(countDown)).place(x=800, y=425)
clockFaceTime = Label(clockFace, font = ('calibri', 50, 'bold'), background = 'black', foreground = 'white')
def clock():
    string = strftime('%I:%M:%S %p')
    clockFaceTime.config(text = string)
    clockFaceTime.after(1000, clock)

clockFaceTime.place(relx=0.3, rely=0.35)
clock()
#================Timer Face (WIP)
running= False
def startButton():
    global running
    if not running:
        updater()
        running=True
def resetButton():
    global running
    if running:
        stopWatch.after_cancel(updateWatch)
        running = False
    global hours, minutes, seconds, milliseconds
    hours, minutes, seconds, milliseconds = 0, 0, 0, 0
    stopWatch.config(text='00:00:00.000')
def stopButton():
    global running
    if running:
        stopWatch.after_cancel(updateWatch)
        running = False
def updater():
    global hours, minutes, seconds, milliseconds
    milliseconds +=1
    if milliseconds == 1000:
        milliseconds = 0
        seconds += 1
    if seconds ==60:
        seconds=0
        minutes+=1
    if minutes==60:
        hours+=1
        minutes=0
    
    hoursString = f'{hours}' if hours > 9 else f'0{hours}'
    minutesString = f'{minutes}' if minutes > 9 else f'0{minutes}'
    secondsString = f'{seconds}' if seconds > 9 else f'0{seconds}'
    millisecondsString = f'{milliseconds}' if milliseconds > 9 else f'000{milliseconds}'


    stopWatch.config(text=hoursString + ':' + minutesString + ":"+ secondsString + "." + millisecondsString)
    global updateWatch
    updateWatch = stopWatch.after(1, updater)

timerFaceTitle = Label(timerFace, text='General Timer', bg='white', ).pack(fill='x')
stopWatch = Label(timerFace, text="00:00:00.00", font=('calibri', 50, 'bold'), bg='white', fg='black')
timerFaceBtn = Button(timerFace, height=2, width=10, text='Clock', bg='white', command=lambda: showFrame(clockFace)).place(x=50, y=425)
timerBtn2 = Button(timerFace, height=2, width=10, text='Timer', bg='white', command=lambda: showFrame(timerFace)).place(x=425, y=425)
countDownBtn=Button(timerFace, height=2, width=10, text='Countdown', bg='white', command=lambda: showFrame(countDown)).place(x=800, y=425)
startBtn = Button(timerFace, height = 2, width=10, text="start", bg='white', command = lambda: startButton()).place(x=175, y=200)
stopBtn = Button(timerFace, height = 2, width=10, text="Stop", bg='white', command= lambda: stopButton()).place(x=675, y=200)
resetBtn = Button(timerFace, height = 2, width=10, text="reset", bg='white', command= lambda: resetButton()).place(x=425, y=300)

stopWatch.place(relx=0.325, rely=0.35)


#========================Countdown Face (WIP)
counter = False
global timeFormat


def oneMinButton():
    global countHours, countMinutes, countSeconds
    countHour.set('00')
    countMinute.set('01')
    countSecond.set('00')
    countDownLabel.config(text = countHour.get() + ':' + countMinute.get() + ':' + countSecond.get())
def twoMinButton():
    global countHours, countMinutes, countSeconds
    countHour.set('00')
    countMinute.set('02')
    countSecond.set('00')
    countDownLabel.config(text = countHour.get() + ':' + countMinute.get() + ':' + countSecond.get())
def threeMinButton():
    global countHours, countMinutes, countSeconds
    countHour.set('00')
    countMinute.set('03')
    countSecond.set('00')
    countDownLabel.config(text = countHour.get() + ':' + countMinute.get() + ':' + countSecond.get())
def fourMinButton():
    global countHours, countMinutes, countSeconds
    countHour.set('0')
    countMinute.set('04')
    countSecond.set('00')
    countDownLabel.config(text = countHour.get() + ':' + countMinute.get() + ':' + countSecond.get())
def fiveMinButton():
    global countHours, countMinutes, countSeconds
    countHour.set('00')
    countMinute.set('5')
    countSecond.set('00')
    countDownLabel.config(text = countHour.get() + ':' + countMinute.get() + ':' + countSecond.get())
def tenMinButton():
    global countHours, countMinutes, countSeconds
    countHour.set('00')
    countMinute.set('10')
    countSecond.set('00')
    countDownLabel.config(text = countHour.get() + ':' + countMinute.get() + ':' + countSecond.get())
def fifteenMinButton():
    global countHours, countMinutes, countSeconds
    countHour.set('00')
    countMinute.set('15')
    countSecond.set('00')
    countDownLabel.config(text = countHour.get() + ':' + countMinute.get() + ':' + countSecond.get())
def twentyMinButton():
    global countHours, countMinutes, countSeconds
    countHour.set('00')
    countMinute.set('20')
    countSecond.set('00')
    countDownLabel.config(text = countHour.get() + ':' + countMinute.get() + ':' + countSecond.get())
def tweFivMinButton():
    global countHours, countMinutes, countSeconds
    countHour.set('00')
    countMinute.set('25')
    countSecond.set('00')
    countDownLabel.config(text = countHour.get() + ':' + countMinute.get() + ':' + countSecond.get())
def thirtyMinButton():
    global countHours, countMinutes, countSeconds
    countHour.set('00')
    countMinute.set('30')
    countSecond.set('00')
    countDownLabel.config(text = countHour.get() + ':' + countMinute.get() + ':' + countSecond.get())
#--------------------------------------------------
def forfiveMinButton():
    global countHours, countMinutes, countSeconds
    countHour.set('00')
    countMinute.set('45')
    countSecond.set('00')
    countDownLabel.config(text = countHour.get() + ':' + countMinute.get() + ':' + countSecond.get())
def sixtyMinButton():
    global countHours, countMinutes, countSeconds
    countHour.set('01')
    countMinute.set('00')
    countSecond.set('00')
    countDownLabel.config(text = countHour.get() + ':' + countMinute.get() + ':' + countSecond.get())
def sevFivMinButton():
    global countHours, countMinutes, countSeconds
    countHour.set('01')
    countMinute.set('15')
    countSecond.set('00')
    countDownLabel.config(text = countHour.get() + ':' + countMinute.get() + ':' + countSecond.get())
def nintyMinButton():
    global countHours, countMinutes, countSeconds
    countHour.set('01')
    countMinute.set('30')
    countSecond.set('00')
    countDownLabel.config(text = countHour.get() + ':' + countMinute.get() + ':' + countSecond.get())
def twohrButton():
    global countHours, countMinutes, countSeconds
    countHour.set('02')
    countMinute.set('00')
    countSecond.set('00')
    countDownLabel.config(text = countHour.get() + ':' + countMinute.get() + ':' + countSecond.get())

def submit():
    try:
        temp = int(countHour.get())*3600 + int(countMinute.get())*60 + int(countSecond.get())
    except:
        print("Please input the right value")
    while temp >-1:
        
        mins,secs = divmod(temp,60)
  
        hours=0
        if mins >60:
             
            hours, mins = divmod(mins, 60)
         
        
        countHour.set("{:02d}".format(hours))
        countMinute.set("{:02d}".format(mins))
        countSecond.set("{:02d}".format(secs))
        countDownLabel.config(text = countHour.get() + ':' + countMinute.get() + ':' + countSecond.get())
        
        countDown.update()
        countDown.after(100000, submit)
        
        if (temp == 0):
            print('done')
         
        temp -= 1

countDownTitle = Label(countDown, text='Countdown Timer', bg='white', ).pack(fill='x')
countDownBtn = Button(countDown, height=2, width=10, text='Clock', bg='white', command=lambda: showFrame(clockFace)).place(x=50, y=425)
countDownLabel = Label(countDown, bg='black',height = 2, width=8, font=('calibri', 50, 'bold'), fg='white')
timerBtn3 = Button(countDown, height=2, width=10, text='Timer', bg='white', command=lambda: showFrame(timerFace)).place(x=400, y=425)
countDownBtn=Button(countDown, height=2, width=10, text='Countdown', bg='white', command=lambda: showFrame(countDown)).place(x=800, y=425)

minBtn = Button(countDown, height=2, width = 10, text='1:00', bg='white', command=lambda: oneMinButton()).place(x=50, y=125) 
minBtn = Button(countDown, height=2, width = 10, text="2:00", bg='white',command=lambda: twoMinButton()).place(x=50, y=175) 
minBtn = Button(countDown, height=2, width = 10, text="3:00", bg='white', command=lambda: threeMinButton()).place(x=50, y=225)
minBtn = Button(countDown, height=2, width = 10, text="4:00", bg='white', command=lambda: fourMinButton()).place(x=50, y=275)
minBtn = Button(countDown, height=2, width = 10, text="5:00", bg='white', command=lambda: fiveMinButton()).place(x=50, y=325)

minBtn = Button(countDown, height=2, width = 10, text="10:00", bg='white', command=lambda: tenMinButton()).place(x=150, y=125) 
minBtn = Button(countDown, height=2, width = 10, text="15:00", bg='white', command=lambda: fifteenMinButton()).place(x=150, y=175) 
minBtn = Button(countDown, height=2, width = 10, text="20:00", bg='white', command=lambda: twentyMinButton()).place(x=150, y=225)
minBtn = Button(countDown, height=2, width = 10, text="25:00", bg='white', command=lambda: tweFivMinButton()).place(x=150, y=275)
minBtn = Button(countDown, height=2, width = 10, text="30:00", bg='white', command=lambda: thirtyMinButton()).place(x=150, y=325)

minBtn = Button(countDown, height=2, width = 10, text="45:00", bg='white', command=lambda: forfiveMinButton()).place(x=250, y=125) 
minBtn = Button(countDown, height=2, width = 10, text="60:00", bg='white', command=lambda: sixtyMinButton()).place(x=250, y=175) 
minBtn = Button(countDown, height=2, width = 10, text="75:00", bg='white', command=lambda: sevFivMinButton()).place(x=250, y=225)
minBtn = Button(countDown, height=2, width = 10, text="90:00", bg='white', command=lambda: nintyMinButton()).place(x=250, y=275)
minBtn = Button(countDown, height=2, width = 10, text="2:00:00", bg='white', command=lambda: twohrButton()).place(x=250, y=325)

startCountBtn = Button(countDown, height = 2, width=10, text="start", bg='white', command=submit).place(x=440, y=350)
stopCountBtn = Button(countDown, height = 2, width=10, text="Stop", bg='white', command=lambda: stopCountDown()).place(x= 565, y=350)
resetCountBtn = Button(countDown, height = 2, width=10, text="reset", bg='white', command = lambda: resetCountDownButton()).place(x=700, y=350)


countDownLabel.place(relx=0.475, rely=0.325)

showFrame(clockFace)
root.mainloop()

