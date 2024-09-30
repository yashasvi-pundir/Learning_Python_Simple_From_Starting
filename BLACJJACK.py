import random  
print("############################\n#   B L A C K J A C K   #\n############################")

from IPython.display import clear_output

def deal_card(): 
    """Return a random card from the deck"""
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card

def calculate_score(cards): 
    """take a list of cardsand return a score calculated from that cards""" 
    if sum(cards)==21 and len(cards)==2:
        return 0
    if 11 in cards and sum(cards)==21: 
        cards.remove(11) 
        cards.append(1)
    return sum(cards)

def play_game():
    user_card=[]
    computer_card=[]
    is_game_over=False 
    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())
        
    while not is_game_over:
        user_score = calculate_score(user_card) 
        computer_score= calculate_score(computer_card)
        print(f" Your card : {user_card} and your score is {user_score}") 
        print(f" Computer's first card:{computer_card[0]}")
        user_should_deal= None
        
        if user_score==0 or computer_score==0 or user_score==21:
          is_game_over = True 
        else:
          user_should_deal = input("Type y to get another card or n to to pass:")
        if user_should_deal=="y":
            user_card.append(deal_card())
        else:
            is_game_over=True
            
    while  computer_score!=0 and computer_score<17:
        computer_card.append(deal_card)
        computer_score=calculate_score(computer_card)
        
while input("Do you want to play a game of Blackjack? Type yes or no:")=="yes":
    clear_output(wait =True)
    play_game()
    