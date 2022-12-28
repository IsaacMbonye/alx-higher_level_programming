#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

number = str(number)



if int(number[-1])  > 5:
   print("Last digit of {:s} the string is {:s} and is greater than 5".format(number, number[-1]))
elif int(number[-1]) == 0:
   print("Last digit of {:s} the string is {:s} and is 0".format(number, number[-1]))
elif int(number[-1]) < 6 and not int(number[-1]) == 0:
   print("Last digit of {:s} the string is {:s} and is less than 6 and not 0".format(number, number[-1]))
