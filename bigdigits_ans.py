#!/usr/bin/python 
import sys
import re
strsub = re.compile('\*')
Zero = ['  *  ',' * * ','*   *','*   *','*   *',' * * ','  *  ']
One = ['  *  ','***  ','  *  ','  *  ','  *  ','  *  ','*****']
Two = [' *** ','*   *','   * ','  *  ',' *   ','*    ','*****']
Three = ['*****','    *','    *','*****','    *','    *','*****']
Four = ['   * ','  ** ',' * * ','*****','   * ','   * ','   * ']
Five = ['*****','*    ','*    ','*****','    *','    *','*****']
Six = ['*****','*    ','*    ','*****','*   *','*   *','*****']
Seven = ['*****','    *','    *','    *','    *','    *','    *']
Eight = [' *** ','*   *','*   *',' *** ','*   *','*   *',' *** ']
Nine = ['*****','*   *','*   *','*****','    *','    *','    *']
Digits = [Zero,One,Two,Three,Four,Five,Six,Seven,Eight,Nine]
input = sys.argv[1]
for each in range(7):
    line = ''
    string = ''
    for every in range(len(input)):
        number = int(input[every])
        digit = Digits[number]
        mob = str(number)
        string = strsub.sub(mob,digit[each])
        line += string + '  '
    print(line)
