import random
playing = True
number = str(random.randint(0,9))
print("Try to guess the number from 0 - 9 selected by the comupter!")
print("The game ends when you get it right!")
while playing:
    guess = input("Give your best guess! \n")
    if number == guess:
        print("You Win!")
        print("The number was: ",number)
        break
    else:
        print("You guessed wrong, try again. \n")