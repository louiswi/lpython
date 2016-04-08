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
number_sort = number
nu = len(number) - 1
for i in range(nu):
    for each in range(nu):
        if number_sort[each] > number_sort[each+1]:
            t = number_sort[each]
            number_sort[each] = number_sort[each+1]
            number_sort[each+1] = t
mean = sum / count
middle_index = count // 2
if count%2:
    middle = number_sort[middle_index]
else:
    middle = (number_sort[middle_index] + number_sort[middle_index+1]) / 2
print('number:',number_sort)
print('count = %d sum = %d lowest = %d middle = %f highest = %d mean = %.12f' %
        (count,sum,lowest,middle,highest,mean))
