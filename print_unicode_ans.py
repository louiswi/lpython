#!/usr/bin/python 
import sys
import unicodedata
words = []
def print_unicode_table(word):
    print('decimal    hex    chr    {0:^40}'.format('name'))
    print('-------    ---    ---    {0:->40}'.format(''))

    code = ord(' ')
    end = min(0xd800,sys.maxunicode)

    while code < end:
        c = chr(code)
        name = unicodedata.name(c,"***unknown***")
        test = True
        for word in words:
            if word not in name.lower():
                test = False
                break
        if test:
            print('{0:7}    {0:5X}    {0:^3c}    {1}'.format(code,name.title()))
        code += 1

if len(sys.argv) > 1:
    if sys.argv[1] in ('-h','--help'):
        print('usage:{0}[string]'.format(sys.argv[0]))
        words = None
    else:
        for each in sys.argv[1:]:
            words.append(each.lower())
if words is  not None:
    print_unicode_table(words)

