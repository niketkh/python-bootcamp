
# coding: utf-8

# # [Blackjack ](https://en.wikipedia.org/wiki/Blackjack) 

# In[1]:

# Used For Card Shuffle
import random

# Boolean used to know if hand is in play
playing = False

chip_pool = 100 

bet = 0

restart_phrase = "Press 'd' to deal the cards again, or press 'q' to quit: "
# Hearts, Diamonds, Clubs, Spades
suits = ('H','D','C','S')

# Possible Card Ranks
ranks = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

# Card Values
# Note: Aces can also be 11, check self.ace for details)
card_val = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}


# In[2]:

# Card Class
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.suit + self.rank
    
    def get_suit(self):
        return self.suit
    
    def get_rank(self):
        return self.rank
    
    def draw(self):
        print (self.suit + self.rank),
        
        
# Deck Class
class Deck:
    
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
                
    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        top_card = self.deck.pop()
        return top_card
    
    def __str__(self):
        deck_composition = ""
        for card in self.deck:
            deck_composition += " " + card.__str__()
        return "The deck has" + deck_composition
    
# Test Deck Class : Uncomment below code
# deckA = Deck()
# print deckA


# In[3]:

# Hand Class 
class Hand:
    
    def __init__(self):
        self.cards = []
        self.value = 0
        # Aces can be 1 or 11 so need to define it here
        self.ace = False
        
    def __str__(self):
        hand_composition = ""
        
        for card in self.cards:
            hand_composition += " " + card.__str__()
            
        return 'The hand has %s' %hand_composition
        
    def add_card(self,card):
        self.cards.append(card)
        
        # Check for Aces
        if card.rank == 'A':
            self.ace = True
        self.value += card_val[card.rank]
        
    def calc_val(self):
        if (self.ace == True and self.value < 12):
            return self.value + 10
        else:
            return self.value
        
    def draw(self,hidden):
        if hidden == True and playing == True:
            #Don't show first hidden card in case of dealer
            starting_card = 1
        else:
            starting_card = 0
        for x in range(starting_card,len(self.cards)):
            self.cards[x].draw()


# In[4]:

# First Bet
def make_bet():
    ''' Ask the player for the bet amount and '''
    
    global bet, chip_pool
    bet = 0
    print " -------------------------------------------------------------------------------"
    print '    Available Chips: ', chip_pool
    print '    What number of chips would you like to bet?: ',
    
    while bet == 0:
        bet_comp = raw_input() # Use bet_comp as a checker
        bet_comp = int(bet_comp)
        # Check to make sure the bet is within the remaining amount of chips left.
        if bet_comp >= 1 and bet_comp <= chip_pool:
            bet = bet_comp
        else:
            print "Invalid bet, you only have " + str(chip_pool) + " remaining"
    print "-------------------------------------------------------------------------------"


# In[5]:

def deal_cards():
    ''' This function deals out cards and sets up round '''
    
    # Set up all global variables
    global result, playing, deck, player_hand, dealer_hand, chip_pool, bet
    
    # Create a deck
    deck = Deck()
    
    #Shuffle it
    deck.shuffle()
    
    #Set up bet
    make_bet()
    
    # Set up both player and dealer hands
    player_hand = Hand()
    dealer_hand = Hand()
    
    # Deal out initial cards
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
    
    result = "    Hit or Stand? Press either h or s: "
    
    if playing == True:
        print 'Fold, Sorry'
        chip_pool -= bet
    
    # Set up to know currently playing hand
    playing = True 
    game_step()


# In[6]:

def hit():
    ''' Implement the hit button '''
    global result, playing, deck, player_hand, dealer_hand, chip_pool, bet
    
    # If hand is in play add card
    if playing:
        if player_hand.calc_val() <= 21:
            player_hand.add_card(deck.deal())
        
        if player_hand.calc_val() > 21:
            result = '    Busted! '+ restart_phrase
            chip_pool -= bet
            playing = False
    else:
        result = "    Sorry, can't hit" + restart_phrase
    
    game_step()


# In[7]:

def stand():
    ''' This function will now play the dealers hand, since stand was chosen '''
    global result, playing, deck, player_hand, dealer_hand, chip_pool, bet
    
    if playing == False:
        if player_hand.calc_val() > 0:
            result = "    Sorry, you can't stand!"
            
    # Now go through all the other possible options
    else:
        
        # Soft 17 rule
        while dealer_hand.calc_val() < 17:
            dealer_hand.add_card(deck.deal())
            
        # Dealer Busts    
        if dealer_hand.calc_val() > 21:
            result = '    Dealer busts! You win!\n    ' + restart_phrase
            chip_pool += bet
            playing = False
            
        #Player has better hand than dealer
        elif dealer_hand.calc_val() < player_hand.calc_val():
            result = '    You beat the dealer, you win!\n    ' + restart_phrase
            chip_pool += bet
            playing = False
        
        # Push
        elif dealer_hand.calc_val() == player_hand.calc_val():
            result = '    Tied up, push!\n    ' + restart_phrase
            playing = False
        
        # Dealer beats player
        else:
            result = '    Dealer Wins!\n    ' + restart_phrase
            chip_pool -= bet
            playing = False
    game_step()


# In[8]:

def game_step():
    'Function to print game step/status on output'
    
    #Display Player Hand
    print ""
    print('    Player Hand is: '),
    player_hand.draw(hidden =False)
    print ""
    
    print '    Player hand total is: '+str(player_hand.calc_val())
    print ""
    #Display Dealer Hand
    print('    Dealer Hand is: '),
    dealer_hand.draw(hidden=True)
    
    # If game round is over
    if playing == False:
        print ""
        print "    Dealer hand total is " + str(dealer_hand.calc_val() )
        print "    Chip Total: " + str(chip_pool)
    # Otherwise, don't know the second card yet
    else: 
        print " with another card hidden upside down"
        print ""
    print " -------------------------------------------------------------------------------"
    # Print result of hit or stand.
    print result,
    player_input()


# In[9]:

def game_exit():
    print '    Thanks for playing!'
    exit()


# In[10]:

def player_input():
    ''' Read user input, lower case it just to be safe'''
    input = raw_input().lower()
    
    
    if input == 'h':
        hit()
    elif input == 's':
        stand()
    elif input == 'd':
        deal_cards()
    elif input == 'q':
        game_exit()
    else:
        print "    Invalid Input...Enter h, s, d, or q: "
        player_input()


# In[11]:

def intro():
    statement = '''
    |=========================================================================|
    |                      Welcome to BlackJack!!!                            |
    |         Get as close to 21 as you can without going over!               |
    |        Dealer hits until she reaches 17. Aces count as 1 or 11.         |
    |   Card output goes a letter followed by a number of face notation       |
    |=========================================================================|
    '''
    print statement
    print "\n"


# In[12]:

'''The following code will initiate the game! (Note: Need to Run all Cells)'''

#Print the intro
intro()
print "H => Hearts, D => Diamonds, C => Clubs, S => Spades"
# Deal out the cards and start the game!
deal_cards()

