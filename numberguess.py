import random


number = random.randint(1, 100)

while (True):
    user_guess = int(raw_input("pick a number between 1 and 100:")) #think about what type the input is.
    
    print(number)    
    if user_guess > number:
        print("Lower\n")
    elif user_guess < number:
        print("Higher\n")
    else:
        print("Correct")
