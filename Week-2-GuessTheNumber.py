# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random

secret_number=0
num_range=100
guesses=7

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global guesses 
    if num_range==100:
        guesses=7
        secret_number= random.randrange(0, 100)
        print ""
        print "New game, Range is from o to 100"
        print "Number of remaining guesses is", guesses     
    elif num_range==1000:
        guesses=10
        secret_number= random.randrange(0, 1000) 
        print" "
        print "New game, Range is from o to 1000"
        print "Number of remaining guesses is", guesses
        
    print " "
    
    # remove this when you add your code    
    pass


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global num_range
    num_range=100
    new_game()
    # remove this when you add your code    
    pass

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    num_range=1000
    new_game()
    pass
    
def input_guess(guess):
    # main game logic goes here	
    guess_number=int(guess)
    global guesses
    print 'Guess was ',guess_number
    guesses=guesses-1
    print "Number of remaining guesses is", guesses
    
   
    if(guess_number>secret_number and guesses>0):        
        print 'Lower'
    elif(guess_number<secret_number and guesses>0):
        print 'Higher!'        
    elif(guess_number==secret_number ):
        print 'Correct!'
        new_game()
    if guesses==0:
        print "Secret Number was: ",secret_number
        new_game()
    
    # remove this when you add your code
    print ""
    pass

    
# create frame
f = simplegui.create_frame("Guess Number", 200, 200)

# register event handlers for control elements and start frame
f.add_button("Range is [0,100)",range100, 200)
f.add_button("Range is [0,1000)",range1000, 200)
f.add_input("Enter a guess",input_guess,200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
f.start()