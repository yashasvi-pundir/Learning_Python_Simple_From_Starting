alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's' , 't', 'u', 'v', 'w', 'x', 'y','z']

direction=input("Type encode to encrypt , type 'decode' to decrypt:/n")
text=input("Enter the text you want to ").lower()
shift=int(input("Enter shift value:"))

def caesar(start_text,shift_amount,shift_direction):
   end_text=""
   for i in start_text:
     position=alphabet.index(i)%26
     
     if shift_direction=="encode":
       new_position=(position+shift_amount)%26
       end_text+=alphabet[new_position]
       print(f"the encoded text is {end_text}")
       
     elif shift_direction=="decode":
      new_position=(position-shift_amount)%26
      end_text+=alphabet[new_position]
      print(f"the decoded text is {end_text}")
      
     else:
       print("Enter a valid input.")
       
caesar(start_text=text,shift_amount=shift,shift_direction=direction)

def encrypt(plain_text,shift_value):
    cypher_text=""
    for letter in plain_text:
      position = alphabet.index(letter)%26
      caesar_cipar=(position+shift_value)%26
      new_letter=alphabet[caesar_cipar]
      cypher_text+=new_letter
      print(f'the encoded is {cypher_text}')
      
def decrypt(cypher_text,shift_value):
  plain_text=""
  for i in cypher_text:
    position=alphabet.index(i)%26
    new_position=(position-shift)%26
    thetext=alphabet[new_position]
    plain_text+=thetext
    print(f'the decoded text is {plain_text}')
    
if direction == "encode":
  encrypt(plain_text=text,shift_value=shift)
elif direction == "decode":
  decrypt(cypher_text=text,shift_value=shift)
else:
  print("Enter the valid input.")
    
       
     
     
   

    
    
    
    
          
     
    


     
      
    
        
    