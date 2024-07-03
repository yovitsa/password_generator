import random
import string

def generate_password(min_length, numbers=True, special_charcters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    char = letters
    if numbers:
        char += digits
    if special_charcters:
        char += special

    pwd = " "
    meet_critieria = False
    has_number = False
    has_special = False

    while not meet_critieria or len(pwd) < min_length:
        new_char = random.choice(char)
        pwd += new_char
        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meet_critieria = True
        if numbers: 
            meet_critieria = has_number
        if special_charcters:
            meet_critieria = meet_critieria and has_special
        
    return pwd


min_lenght = int(input("Enter the minimum lenght: "))
has_number = input("Do you want to have numbers(y/n)?").lower() == "y"
has_special = input("Do you want to have special char (y/n)?").lower() == "y"

pwd = generate_password(min_lenght, has_number, has_special)
print("Your generated password is: ",pwd)