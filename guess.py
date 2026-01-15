import random

guesses = []
myComputer = random.randint(1, 50)

player = int(input('enter a number  between 1 - 50: '))

guesses.append(player)

while player != myComputer:
    if player > myComputer:
        print('Number is too high!')

    else: 
        print('Number is too low')

    player = int(input('enter a number  between 1 - 50: '))
    guesses.append(player)

else:
    print('you have guessed right! good job!')
    print('it took you %i guesses. ' % len(guesses) )
    print('these were your guesses: ')
    print(guesses)
