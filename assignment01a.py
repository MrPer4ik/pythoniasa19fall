"""
Assignment 1-A
==============

Write fuction that generates the text below; use at least variables and f-strings.
For those who are already familiar with Python – write the best code you can to conform to the Zen of Python.

>>> print(poem())
This is the house that Jack built.
---
This is the malt
That lay in the house that Jack built.
---
This is the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the man all tattered and torn,
That kissed the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the priest all shaven and shorn,
That married the man all tattered and torn,
That kissed the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the cock that crowed in the morn,
That waked the priest all shaven and shorn,
That married the man all tattered and torn,
That kissed the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
---
This is the farmer sowing his corn,
That kept the cock that crowed in the morn,
That waked the priest all shaven and shorn,
That married the man all tattered and torn,
That kissed the maiden all forlorn,
That milked the cow with the crumpled horn,
That tossed the dog,
That worried the cat,
That killed the rat,
That ate the malt
That lay in the house that Jack built.
<BLANKLINE>
"""

def poem():
    return ''


base = [["the house that Jack built", "lay in"],
       ["the malt", "ate"],
       ["the rat", "killed"],
       ["the cat", 'worried'],
       ["the dog", "tossed"],
       ["the cow with the crumpled horn", "milked"],
       ["the maiden all forlorn", "kissed"],
       ["the man all tatter'd and torn", 'married'],
       ["the priest all shaven and shorn", "waked"],
       ["the cock that crow'd in the morn", "kept"],
       ["the farmer sowing his corn", 'is']]

for i in range(len(base)):
    for j in range(i, -1, -1):
        if j == i:
            print("This is " + base[j][0] + ",")
        else:
            print("That " + base[j][1] + " " + base[j][0], end="")
            print('.' if j == 0 else ',')
    print()
