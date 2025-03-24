# Joshua Dinis
# Randomly Generated List Assignment
# March 24th 2025
# generates a list of 100 variables, and then calculates the average

import random

randNums = []

for index in range (100):
    randNums.append(random.randint(1,100))

avg = (sum(randNums))/100    
avgStr = str(avg)
randNumsStr = str(randNums)
print ("The list of 100 randomly generated numbers is: \n" + randNumsStr)

print ("The average of the list of numbers is:  " + avgStr)