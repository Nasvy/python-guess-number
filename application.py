print "Welcome\n"
from random import randrange 
number = input("Insert a number\n")  
ran_num = randrange(1,20) 
if  number > ran_num : 
	print "You guess to high please try again"
elif number < ran_num:
	print "you guess too low, please try again"