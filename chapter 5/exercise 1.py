# "Python Programming for the Absolute Beginner", Michael Dawson
#
# chapter 5, exercise 1

import random

words=['Adam', 'Basia', 'Celina', 'Damian', 'Edgar', 'Fikołek']

# oryginal list of words, in regular order
print("Oryginalna lista słów: ")
for i in words:
    print(i, end=' ')

# random order by using shuffle
print("\n\nWypisanie słów w losowym porządku, wykorzysując kopię i funkcję random.shuffle(list_name): ")
copy_words=words[:]
random.shuffle(copy_words)
for i in copy_words:
    print(i, end=' ')

# random order by random index and .pop() method
print("\n\nWypisanie słów w losowym porządku, wykorzysując kopię, losowy index i metodę .pop(): ")
copy_words=words[:]
while copy_words:
    number=random.randrange(len(copy_words))
    print(copy_words.pop(number), end=' ')

# random order by random.choice and .remove method (the slowest method)
print("\n\nWypisanie słów w losowym porządku, wykorzystując kopię, wylosowanie elementu poprzez \
\nrandom.choice i wykorzystanie metody .remove (najwolniejsze z zaprezentowanych losowań): ")
copy_words=words[:]
while copy_words:
    word=random.choice(copy_words)
    print(word, end=' ')
    copy_words.remove(word)


input()
