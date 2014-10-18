# Programmed by Jibin Liu
# implementation of card game - Memory
# Can be playd at http://www.codeskulptor.org/#user31_fnh07UjiVwkp95r.py

import simplegui
import random

# helper function to initialize globals
def new_game():
    global cards, exposed, state, turns
    cards = range(0, 8) * 2
    random.shuffle(cards)
    exposed = [False] * 16
    state = 0
    turns = 0
    label.set_text("Turns = 0")

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global cards, exposed, state, card1, card2, turns
    if state == 0:
        card1 = pos[0] // 50
        exposed[card1] = True
        state = 1
    elif state == 1:
        card2 = pos[0] // 50
        exposed[card2] = True
        state = 2
        turns += 1
        label.set_text("Turns = " + str(turns))
    else:
        if cards[card1] != cards[card2]:
            exposed[card1] = False
            exposed[card2] = False
            state = 1
            card1 = pos[0] // 50
            exposed[card1] = True
        else:
            card1 = pos[0] // 50
            exposed[card1] = True
            state = 1
    
                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards, exposed
    interval = 800 / 16
    position = [0, 100]
    for i in range(0, 16):
        if exposed[i] == True:
            canvas.draw_text(str(cards[i]), [position[0] + 15, 65], 40, "White")
            position[0] += interval
        else:
            canvas.draw_polygon([position, [position[0], 0],
                                [position[0] + interval, 0], [position[0] + interval, 100]],
                                2, "Black", "Green")
            position[0] += interval
            
                            

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()
