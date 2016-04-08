#!/usr/bin/python 
import random
article = ['the','a','another']
subject = ['act','dog','man','women']
verb = ['sang','ran','jump']
adverb = ['loudly','quietly','well','badly']
for each in range(5):
    line = ''
    line = random.choice(article) + ' ' + random.choice(subject) + ' ' + random.choice(verb)
    if random.randint(0,1):
        line += ' ' + random.choice(adverb)
    print(line)
