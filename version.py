import random
import string

def generate_password(min_length, numbers=True, special_charchters=True ):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    char = letters
    if digits:
        char += digits
    elif special:
        char +=special

    pwd= ' '
    meet_criteria = False
    has_numbers = False
    has_special = False

    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(char)
        pwd += new_char
         
        if new_char: 
            has_numbers =True
        elif new_char:
            has_special= True
       

        meet_criteria = True
        if new_char:
            meet_criteria = has_numbers
        elif new_char:
            meet_criteria = meet_criteria + has_special

    return pwd

min_length =(int(input("Enter the number of deisred charchters: ")))
has_numbers =(input("Do you want numbres (y/n):")).lower == ('y')
has_special= (input("Do you want special charchters (y/n):")).lower==('y')

pwd = generate_password(min_length, has_numbers, has_special)
print('Your new generated password is:', pwd)



