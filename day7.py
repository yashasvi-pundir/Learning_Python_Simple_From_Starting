# hangman
import random

word_list=["yashasui","tushar","pundirs"]
chosen_word = random.choice(word_list)
print(f"the solution is {chosen_word}") 
lives=6
endofgame=False
guesses=[]

while not endofgame:
    guess= input('guess the letter:').lower()
    worldlenghth = len(chosen_word)
    for i in range(worldlenghth):
       display = ["_"] * len(chosen_word)
    for position in range(worldlenghth):
        letter  = chosen_word[position]
        if letter==guess:
            display[position]=letter
            guesses.append(letter)
    print(display)
    
    if guess in guesses:
        print('You already guessed that letter.')
        
    if guess not in chosen_word:
        lives-=1
        print('wrong guess') 
        print('lives remaining:', lives) 
        print('_ _ _ _ _ _ _ _ _') 
        if lives==0:
          endofgame=True
          print("Youlose")
                  
    if "_" not in display:
        endofgame= True
        print("you win")

        







