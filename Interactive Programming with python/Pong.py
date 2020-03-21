# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
paddle2_pos = [[HALF_PAD_WIDTH,HEIGHT/2 - HALF_PAD_HEIGHT],[HALF_PAD_WIDTH,(HEIGHT/2 + HALF_PAD_HEIGHT)]]
paddle1_pos = [[WIDTH-HALF_PAD_WIDTH,HEIGHT/2 - HALF_PAD_HEIGHT],[WIDTH-HALF_PAD_WIDTH,(HEIGHT/2 + HALF_PAD_HEIGHT)]]
ball_pos = [WIDTH/2, HEIGHT/2]
ball_vel= [0, 0]
paddle1_vel, paddle2_vel = [0, 0], [0, 0]
player1 = 0
player2 = 0
acc1 = 0
acc2 = 0
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists    
    global acc1, acc2, RIGHT, LEFT 
    if direction == "right":
        print "5"
        ball_vel[0]+=acc1
        ball_vel[1]+=acc2
    elif direction == "left":
        print "6"
        ball_vel[0]-=acc1
        ball_vel[1]+=acc2
    if direction == "right1":
        print "7"
        ball_vel[0]+=acc1
        #ball_vel[1]+=acc2
    elif direction == "left1":
        print "8"
        ball_vel[0]-=acc1
        #ball_vel[1]-=acc2
    elif direction == "bottom" and RIGHT:
        print "9"
        ball_vel[1]+=acc2
    elif direction == "bottom" and LEFT:
        print "10"
        ball_vel[1]+=acc2
    elif direction == "top" and RIGHT:
        print "11"
        ball_vel[1]-=acc2
    elif direction == "top" and LEFT:
        print "12"
        ball_vel[1]-=acc2
        
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    #global player1, player2  # these are ints
    global RIGHT, LEFT, ball_pos, ball_vel
    global acc1, acc2
    #player1, player2 = 0, 0
    ball_pos = [WIDTH/2, HEIGHT/2]
    ball_vel= [0, 0]
    paddle2_pos = [[HALF_PAD_WIDTH,HEIGHT/2 - HALF_PAD_HEIGHT],[HALF_PAD_WIDTH,(HEIGHT/2 + HALF_PAD_HEIGHT)]]
    paddle1_pos = [[WIDTH-HALF_PAD_WIDTH,HEIGHT/2 - HALF_PAD_HEIGHT],[WIDTH-HALF_PAD_WIDTH,(HEIGHT/2 + HALF_PAD_HEIGHT)]]
    acc1=4
    acc2=random.randrange(0,3)
    x = random.randrange(1,3)
    if x==1:
        RIGHT = True
        LEFT = False
    else:
        RIGHT = False
        LEFT = True
       
    if RIGHT:
        spawn_ball("right")
    else:
        spawn_ball("left")
        
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel, BALL_RADIUS, player1, player2
    global RIGHT, LEFT, player1, player2    
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    ball_pos[0]+= ball_vel[0]
    ball_pos[1]+= ball_vel[1]
    
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 1, 'White', 'White')
    
    # update paddle's vertical position, keep paddle on the screen
    if(paddle1_pos[0][1]>0): 
        paddle1_pos[0][1]-= paddle1_vel[0]
        paddle1_pos[1][1]-= paddle1_vel[0]
 
    if(paddle1_pos[1][1]< HEIGHT):
        paddle1_pos[0][1]-= paddle1_vel[1]
        paddle1_pos[1][1]-= paddle1_vel[1]
         
    if(paddle2_pos[0][1]>0): 
        paddle2_pos[0][1]-= paddle2_vel[0]
        paddle2_pos[1][1]-= paddle2_vel[0]
 
    if(paddle2_pos[1][1]< HEIGHT):
        paddle2_pos[0][1]-= paddle2_vel[1]
        paddle2_pos[1][1]-= paddle2_vel[1]
    
    # draw paddles
    canvas.draw_line(paddle1_pos[0], paddle1_pos[1], PAD_WIDTH, "White")
    canvas.draw_line(paddle2_pos[0], paddle2_pos[1], PAD_WIDTH, "White")
    
    # determine whether paddle and ball collide 
    if(ball_pos[0]==PAD_WIDTH+BALL_RADIUS):
        if(ball_pos[1]> paddle2_pos[0][1] and ball_pos[1]< paddle2_pos[1][1]):           
            RIGHT = True
            LEFT = False
            print "1"
            spawn_ball("right1")
        else:
            player2+=1
            new_game()
                 
    if(ball_pos[0]==WIDTH-PAD_WIDTH-BALL_RADIUS):
        if(ball_pos[1]+BALL_RADIUS> paddle1_pos[0][1] and ball_pos[1]+BALL_RADIUS< paddle1_pos[1][1]):
            RIGHT = False
            LEFT = True
            print "2"
            spawn_ball("left1")
        else:
            player1+=1
            new_game()
    
    if(ball_pos[1]-BALL_RADIUS==0):
            print "3"
            spawn_ball("bottom")
       
    if(ball_pos[1]+BALL_RADIUS==HEIGHT):
            print "4"
            spawn_ball("top")
    
    # draw scores
    canvas.draw_text(str(player1), (200, 40), 25, 'White')
    canvas.draw_text(str(player2), (400, 40), 25, 'White')
        
def keydown(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos
    vel = 3 
    if key == simplegui.KEY_MAP["up"]:
            paddle1_vel[0]+= vel
    if key == simplegui.KEY_MAP["w"]:        
            paddle2_vel[0]+= vel
    if key == simplegui.KEY_MAP["down"]:
            paddle1_vel[1]-= vel
    if key == simplegui.KEY_MAP["s"]:        
            paddle2_vel[1]-= vel

def keyup(key):
    global paddle1_vel, paddle2_vel, paddle1_pos, paddle2_pos    
    paddle1_vel, paddle2_vel =[0, 0], [0, 0]

def game():
    global player1, player2
    player1 = 0
    player2 = 0
    new_game()
    
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Start", game, 200)
frame.add_button("Restart", game, 200)
#timer = simplegui.create_timer(5000, time)
# start frame
new_game()
frame.start()
#timer.start()
