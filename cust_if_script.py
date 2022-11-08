#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to make a decision."""


message = "As your score is :"

score = int(input( "Please enter your score :")) 

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
