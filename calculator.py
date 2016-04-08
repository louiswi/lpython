#!/usr/bin/python 
number = []
count = 0
sum = 0
lowest = 100000000000
highest = 0
mean = 0
while(True):
    string = input("enter a number or Enter to finish:")
    if not string:
        break
    intin = int(string)
    number.append(intin)
    count += 1
    sum += intin
    if lowest > intin:
        lowest = intin
    if highest < intin:
        highest = intin

mean = sum / count
print('number:',number)
print('count = %d sum = %d lowest = %d highest = %d mean = %.12f' %
        (count,sum,lowest,highest,mean))
