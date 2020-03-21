# Reflex tester

###################################################
# Student should add code where relevant to the following.

import simplegui
import time

total_ticks = 0
first_click = True
timeeeee=0
t1,t2=0,0

# Timer handler
def tick():
    global timeeeee
    timeeeee+=10
    
# Button handler
def click():
    global first_click,timeeeee,t1,t2
    if first_click:
        first_click=False
        timer.start()
        t1=time.time()
    else:
        first_click=True
        timer.stop()
        cal_time(timeeeee)
        timeeeee=0
        t2=time.time()
        print t2-t1

def cal_time(t):
    print "Time elapsed between two clicks " +str(t) + " milliseconds" 
    print ""

# Create frame and timer
frame = simplegui.create_frame("Counter with buttons", 200, 200)
frame.add_button("Click me", click, 200)
timer = simplegui.create_timer(10, tick)

# Start timer
frame.start()
