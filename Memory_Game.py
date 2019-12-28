# implementation of card game - Memory

import simplegui
import random
d = {}
state = 0
a = []
value = False
select = []
selected = []
correct = []
turn = 0
label = 0

# helper function to initialize globals
def new_game():
    
    global d, select, turn, label, state, a, value, selected, correct
    i = 0
    select = []
    turn, state = 0, 0
    a = []
    value = False
    selected = []
    correct = []
    num_list = [1, 2, 3, 4, 5, 6, 7, 8]
    a = []
    random_list = []
    while len(random_list)<8:
        a = random.choice(num_list)
        if a in random_list:
            pass
        else:
            random_list.append(a)
    print random_list
    
    label.set_text("Turns = "+str(turn))
    for j in range(0, 800, 50):
        if j<=350:
            d[(j,0), (j+50,0), (j+50,100), (j,100)] = str(random_list[i])
            i+=1
            if j == 350:
                random.shuffle(random_list)                
        elif j>350:
            i-=1
            d[(j,0), (j+50,0), (j+50,100), (j,100)] = str(random_list[i])
                                 
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global value, turn, label
    global a, select                      
    global state, selected, correct
    
    if state == 0:
        state = 1
    elif state == 1:
        state = 2
    else:
        turn+=1
        label.set_text("Turns = "+str(turn))
        a = []
        flag = 0
        #print selected
        for s in selected:
            print selected
            a.append(d[tuple(s)])
            #print d[tuple(s)]
            if(len(a)>1):
                print a[0], a[1]
                if(a[0] == a[1]):
                    #selected = []
                    state = 1
                    flag = 1
                else:
                    selected = []
                                        
        if flag==1:
            print "hey"            
            for s in selected:
                correct.append(s)
            selected = []
                    
        if state == 2:
            print "here"
            #print correct
            select = []            
            if(len(correct)>1):                
                for a in correct:
                    select.append(a) 
                    #print select
            state = 1
         
    for j in range(0, 800, 50):
        if pos[0]> j and pos[0]< j+50:
            a =[(j, 0), (j+50, 0), (j+50, 100), (j, 100)]
            value = True
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global d, state, value, select, selected
    for j in range(0, 800, 50):
        canvas.draw_polygon([(j,0), (j+50,0), (j+50,100), (j,100)], 1, "Black", "Green")
                
    if value:
        for key in d:
            if a == list(key) and (state == 0 or state == 1 or state == 2):
                select.append(a)
                selected.append(a)
                
                value = False
                
    for sel in select:
        #print select
        canvas.draw_polygon(sel, 1, "Black", "Black")
        canvas.draw_text(d[tuple(sel)], (sel[0][0]+25, 50), 25, "White",)

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = " +str(turn))

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

# Always remember to review the grading rubric