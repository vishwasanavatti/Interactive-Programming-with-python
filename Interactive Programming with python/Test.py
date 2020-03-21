# Move a ball

###################################################
# Student should add code where relevant to the following.


import simplegui 

# Define globals - Constants are capitalized in Python
HEIGHT = 400
WIDTH = 400
RADIUS_INCREMENT = 5
ball_radius = 20
pos = [10, 20]
# Draw handler
def draw(canvas):
    canvas.draw_circle((200,200),ball_radius,5,"Red")
    canvas.draw_polygon([(50, 50), (180, 50), (180, 140), (50, 140)], 5, 'Blue', 'White')
    canvas.draw_line((10, 20), pos, 5, 'Red')
# Event handlers for buttons
def increase_radius():
    global ball_radius
    ball_radius+=RADIUS_INCREMENT

def decrease_radius():
    global ball_radius
    if(ball_radius>5):
        ball_radius-=RADIUS_INCREMENT

def tick():
    global pos
    pos[0]+=3
    pos[1]+=0.7
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("Ball control", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.add_button("Increase radius", increase_radius)
frame.add_button("Decrease radius", decrease_radius)

timer = simplegui.create_timer(300, tick)
# Start the frame animation
frame.start()
timer.start()

