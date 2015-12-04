import random
# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def name_to_number(name):
    # delete the following pass statement and fill in your code below
    if(name=='rock'):
        return 0
    elif(name=='Spock'):
        return 1
    elif(name=='paper'):
        return 2
    elif(name=='lizard'):
        return 3
    elif(name=='scissors'):
        return 4
    else:
        '''if user passes choice which is not out of the rock, Spock,
        paper, lizard, scissors'''
        return 99

    # convert name to number using if/elif/else
    # don't forget to return the result!


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    if(number==0):
        return 'rock'
    elif(number==1):
        return 'Spock'
    elif(number==2):
        return 'paper'
    elif(number==3):
        return 'lizard'
    elif(number==4):
        return 'scissors'
    else:
        return 'Wrong input'
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    

def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
    
    
    # print a blank line to separate consecutive games
    print ''

    # print out the message for the player's choice
    
    print 'Player chooses', player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    
    player_number = name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    
    comp_number = random.randrange(0,5)
    #print comp_number
    # convert comp_number to comp_choice using the function number_to_name()
    
    comp_choice = number_to_name(comp_number)
    # print out the message for computer's choice
    
    print 'Computer chooses', comp_choice
    
    # compute difference of comp_number and player_number modulo five
    #in case 99 is returned because of the wrong choice entered by a player
    if player_number!= 99:
        diff_number = ( comp_number - player_number ) % 5
    else:
        print 'Player chose unavailable option!'
        return
    #print diff_number
    # use if/elif/else to determine winner, print winner message

    if diff_number == 1 or diff_number == 2:
        print 'Computer wins!'
    elif diff_number == 3 or diff_number == 4:
        print 'Player wins!'
    else: 
        print 'Player and computer tie!'	
        
        
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
#rpsls('asdf')
# always remember to check your completed program against the grading rubric


