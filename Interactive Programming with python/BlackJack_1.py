# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0
dealer = 0
player = 0
roll = 0
first_card = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.hand_cards = list()
        self.hand_value = 0

    def __str__(self):
        str1 = "Hand Contains "
        str2 = str(self.hand_cards)
        return str1 + str2

    def add_card(self, card):
        hand = ""
        self.hand_cards.append(str(card))
        for i in range(len(self.hand_cards)):
            hand += self.hand_cards[i]
        return hand
        
    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        count_A = 0
        if len(self.hand_cards)>0:
            self.hand_value = 0
            for card in self.hand_cards:
                cl = list(card)
                if cl[1] in VALUES:
                    if cl[1] == 'A':
                        count_A+=1
                    self.hand_value += VALUES[cl[1]]
        if(count_A<1):
            return self.hand_value
        else:
            if self.hand_value+10<=21:
                return self.hand_value+10
            else:
                return self.hand_value
   
    def draw(self, canvas, pos):
        pass	# draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.deck_cards = []
        for suit in SUITS:
            for rank in RANKS:
                self.deck_cards.append(str(suit)+str(rank))
        
    def shuffle(self):   
        return random.shuffle(self.deck_cards)    

    def deal_card(self):
        deal = random.choice(self.deck_cards)
        return deal
    
    def __str__(self):
        str1 = "Deck Contains "
        str2 = str(self.deck_cards)
        return str1+str2

#define event handlers for buttons
def deal():
    global outcome, in_play, dealer, roll, player, first_card

    # your code goes here
    in_play = False
    outcome = ""
    #score = 0
    first_card = 0
    dealer = 0
    player = 0
    roll = 0
    
    roll = Deck()
    player = Hand()
    dealer = Hand()
    roll.shuffle()
    i = 0
    for i in range(4):
        card = roll.deal_card()
        if(i==0 or i==2):
            player.add_card(card)
        else:            
            dealer.add_card(card)
            
    print player
    print dealer
    outcome = ""
    in_play = True

def hit():
    #pass	# replace with your code below
    global player, roll, outcome, in_play, score, first_card
    # if the hand is in play, hit the player
    if in_play:
        if(player.get_value()<=21):
            player.add_card(roll.deal_card())
            print player
            if(player.get_value()>21):
                outcome = "You Have busted"
                in_play = False
                score-=1
                
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    #pass	# replace with your code below
    global outcome, in_play, dealer, roll, player, score, first_card
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        dealer.add_card(first_card)
        while(dealer.get_value()<=17):
            dealer.add_card(roll.deal_card())
                
        if dealer.get_value()>21:
            outcome = "Dealer is busted"
            score+=1
            
        elif dealer.get_value()>=player.get_value():
            outcome = "Dealer Wins"
            score-=1
        else:
            outcome = "Player wins"
            score+=1
            
        dealer.hand_cards.pop(1)    
        in_play = False
     
    print player
    print dealer
    print score
    print outcome
    # assign a message to outcome, update in_play and score

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global player, dealer, CARD_SIZE, outcome, first_card 
    #card = Card("S", "A")
    #card.draw(canvas, [300, 300])
    
    if len(player.hand_cards)>0:
        i, j = 100, 300
        for pick in player.hand_cards:
            cd = list(pick)
            card = Card(str(cd[0]), str(cd[1]))
            card.draw(canvas, [i, j])
            i += CARD_SIZE[0] - CARD_SIZE[0]/2
            
    if outcome!="":
        back_card = list(first_card)
        card = Card(back_card[0], back_card[1])
        card.draw(canvas, [100, 100])
        
    if len(dealer.hand_cards)>0:
        if first_card == 0:
            first_card = dealer.hand_cards.pop(0)
            #print first_card
        
        if first_card!=0 and outcome=="":
            canvas.draw_image(card_back, (72+36, 48), CARD_BACK_SIZE, (100+CARD_SIZE[0]/2, 149), CARD_BACK_SIZE)
        
        i, j = 100+CARD_SIZE[0]/2, 100
        for pick in dealer.hand_cards:
            cd = list(pick)
            card = Card(str(cd[0]), str(cd[1]))
            card.draw(canvas, [i, j])
            i += CARD_SIZE[0] - CARD_SIZE[0]/2
            
    canvas.draw_text(outcome, (250, 250), 40, 'White')
    canvas.draw_text("Dealer", (100, 80), 25, 'White')
    canvas.draw_text("Player", (100, 280), 25, 'White')
    canvas.draw_text("Score = "+str(score), (400, 100), 25, 'White')

# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()

# remember to review the gradic rubric
