# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import randomrange

secret_number=0
guess=0


# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number, guess
    secret_number=0
    guess=0


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number,guess
    secret_number=random.randrange[0,100)
    guess=7
    print "Range is between 0 to 100"
    print "Guesses remaining", guess
    print ""

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number, guess
    secret_number=random.randrange[0,100)
    guess=10
    print "Range is between 0 to 1000"
    print "Guesses remaining", guess        
    
def input_guess(input_guess):
    # main game logic goes here
    g=int(input_guess)                              
    if(g==secret_number):
        print "Correct Guess"
        new_game()
    if(g>secret_number):
        print "Higher"
        print ""
    if(g<secret_number):
        print "Lower"
        print ""
    
    
# create frame
f=simplegui.create_frame("Guess the Number",200,200)
f.add_button("range - (0,100)",range100,100)
f.add_button("range - (0,1000)",range1000,100)                                   
f.add_input("Guess the number",input_guess,100)                                

# register event handlers for control elements and start frame
f.start()

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
