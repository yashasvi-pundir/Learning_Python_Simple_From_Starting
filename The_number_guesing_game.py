from random import randint

print("#############################\n#   N U M B E R   G U E S S I N G   G A M E   #\n#############################")
print("Welcome to the Number Guessing Game")
print("I'm thinking of a number between 1 and 100")

computer_choice = randint(1,100)
l = input("Choose a difficulty. Type hard or easy")
number_of_attempts=0

if l=="easy":
  number_of_attempts=10
  print("You have 10 attempts remaining to guess the number. ")
elif l=="hard":
    number_of_attempts=5
    print("You have 5 attempts to guess the number")
else:
    print("enter a valid option")
    
def  check_guess():
    global number_of_attempts
    guess=int(input("Enter your guess"))
    if guess==computer_choice:
        print(f"You win . The number is {computer_choice}")
    elif guess>computer_choice:
        print("Too High")
        number_of_attempts -=1
        print(f"you have {number_of_attempts} remaining")
    elif guess< computer_choice:
         number_of_attempts -=1
         print("Too low")
         print(f"you have {number_of_attempts} remaining")
         
while number_of_attempts!=0:
    check_guess()
else:
    print("Sorry you ran out of attempts.\n Better luck next time. \nThe number was {computer_choice}")
