from IPython.display import clear_output
bid={}
bidding_finished=False
def find_highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for bidder in bidding_record:
        bid_amountt=int(bidding_record[bidder])
        if bid_amountt>highest_bid:
            highest_bid=bid_amountt
            winner=bidder
    print(f"the winner is {winner} with the bid of {highest_bid}")
while not bidding_finished:
    name=input(" What is your name.?")
    price=int(input("what is your bid?$"))
    bid[name]=price
    Should_continue=input("Are there any other biddders?Type yes or no.")
    if Should_continue=="no":
       find_highest_bidder(bid)
       bidding_finished=True
    elif Should_continue=="yes":
        clear_output(wait=True) # this how the out[put is cleared] 
    else:
        print("Enter a valid choice")      

