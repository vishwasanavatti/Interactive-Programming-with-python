# Ball grid slution

###################################################
# Student should enter code below

import simplegui

BALL_RADIUS = 20
GRID_SIZE = 10
WIDTH = 2 * GRID_SIZE * BALL_RADIUS
HEIGHT = 2 * GRID_SIZE * BALL_RADIUS

# define draw
def draw(canvas):
    for i in range(GRID_SIZE/2):
        for j in range(GRID_SIZE):
            canvas.draw_circle([2*BALL_RADIUS*i+BALL_RADIUS, 2*BALL_RADIUS*j+BALL_RADIUS], BALL_RADIUS, 1, "White", "White")
# create frame and register handlers
frame = simplegui.create_frame("Ball grid", WIDTH, HEIGHT)
frame.set_draw_handler(draw)

# start frame
frame.start()

