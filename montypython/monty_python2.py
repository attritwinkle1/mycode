#!/usr/bin/env python3

#starting our loop
round = 0

#defining control staructure
while True:

    round = round + 1
    print('Finish the movie title, "Monty Python\'s The Life of ______"')
    answer = input("Your guess--> ")
    if answer == 'Brian':
        print('Correct')
        break
    elif round==3:
        print("Sorry, the answer was Brian.")
        break
    else:
        print("Sorry! Try again!")

