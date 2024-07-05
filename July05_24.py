import random
import string

def generate_passsword(min_length, numbers=True, specail_charachters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    print(letters, numbers, special)

    char = letters
    if digits:
        char += digits
    if specail_charachters:
        char += special

    pwd= ' '
    meet_criteria = False
    has_numbers = False
    has_special = False

    while not meet_criteria or len(pwd) < min_length:
        new_char = random.choice(char)
        pwd += new_char
        if new_char:
            has_numbers = True
        elif new_char:
            has_special = True

        meet_criteria = True

        if numbers:
            meet_criteria = has_numbers
        elif specail_charachters:
            meet_criteria = meet_criteria and has_special
        
    return pwd

min_length = (int(input("Please enter the minuimum length: ")))
has_number = (input("Do you want your password ot have numbers (y/n)").lower == ('y'))
has_special = (input("Do you want special charchters (y/n)").lower == ('y'))

pwd = generate_passsword(min_length, has_number, has_special)
print(f'"Your auto generated password is: "{pwd}')
