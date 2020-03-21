# template for "Stopwatch: The Game"
import simplegui
# define global variables

time="0:00.0"
time1="0:00.0"
point = 0
tried = 0
score = str(point)+ "/"+ str(tried) 
clock=1
b = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global time
    strtens=0
    millisec = t%10
    #print sec
    tens = (t//10)%60
    if(tens<10):
        strtens = "0"+str(tens)
    else:
        strtens=tens
    #print tens
    mins = t//600
    #print mins
    time = str(mins)+":"+str(strtens)+"."+str(millisec)
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start():
    global b
    b = True
    timer.start()

def stop():
    global b, time, score ,point , tried
    if b:
        tried+=1
        test = list(time.split("."))
        if test[-1] == "0":
            point+=1
        score = str(point)+"/"+str(tried)
    b = False   
    timer.stop()

def reset():
    global time, clock, point , tried
    point , tried = 0, 0
    timer.stop()
    clock = 1
    time = time1
    

# define event handler for timer with 0.1 sec interval
def watch():
    global clock
    clock+=1
    format(clock)

# define draw handler
def draw(canvas):
    canvas.draw_text(time, [80, 100], 30, "White")
    canvas.draw_text(score, [160, 20], 20, "Red")
    
# create frame
frame = simplegui.create_frame("Stop Watch!", 200,200)
timer = simplegui.create_timer(100,watch)

# register event handlers
frame.set_draw_handler(draw)
frame.add_button("Start", start, 100)
frame.add_button("Stop", stop, 100)
frame.add_button("Reset", reset, 100)

# start frame
frame.start()

# Please remember to review the grading rubric
