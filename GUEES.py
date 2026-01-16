import random

computer = random.randint(1, 50)

guesses = []

player = int(input("enter a number between 1 -  50: "))
guesses.append(player)

while player != computer:
    if player > computer:
        print('Number is too high')

    elif player < computer:
        print('Number is too low')
    
        
    player = int(input("enter a number between 1 -  50: "))
    guesses.append(player)
    if player == computer:
        print('You have guessed it right')
        
    
print(f"your guesses {guesses}")