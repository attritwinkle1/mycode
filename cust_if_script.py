#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = "As your score is :"

# the user might input ANYTHING
# 40
# WD40   <-- this should cause a graceful exit
# 40.5   <-- this should cause a graceful exit
score = input("Please enter your score: ")   # input always returns a string

#checking if integer is only sent as input
#if not type(score) == int:
#if type(score) != int:
if not score.isnumeric():
    print("Please enter a valid integer between 0-100")
    exit()  # exit the program only IF score is NOT an int

# now we KNOW that input (score) is a valid int... we can make the change
score = int(score)

#if elif for the score range
if score >= 90 and score <= 100:
     message = message + str(score) + ", " + "Your grade is A"
elif score >=80 and score <= 89:
     message = message + str(score) + ", " + "Your grade is B"
elif score >=70 and score <= 79:
     message = message + str(score) + ", " + "Your grade is C"
elif score >=60 and score <= 69:
     message = message + str(score) + ", " + "Your grade is D"
elif score <=59:
     message = message + str(score) + ", " + "Your grade is F"
else:
     message = "Your grade option doesn't exist"
print (message)
