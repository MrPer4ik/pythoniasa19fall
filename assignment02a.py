"""
Assignment 2-A
==============

Wrap Assignment 1-A in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('data/poem-en.txt').read_text()
True
"""

def poem():
    result = ''
    base = [["the house that Jack built", "lay in"],
            ["the malt", "ate"],
            ["the rat", "killed"],
            ["the cat", 'worried'],
            ["the dog", "tossed"],
            ["the cow with the crumpled horn", "milked"],
            ["the maiden all forlorn", "kissed"],
            ["the man all tattered and torn", 'married'],
            ["the priest all shaven and shorn", "waked"],
            ["the cock that crowed in the morn", "kept"],
            ["the farmer sowing his corn", 'is']]

    for i in range(len(base)):
        for j in range(i, 0, -1):
            if j == i:
                result += f'This is {base[j][0]}'
            else:
                result += f'That {base[j][1]} {base[j][0]}'
            result += ',\n' if j > 1 else '\n'
        result += f'This is {base[i][i]}.\n\n' if i == 0 else f'That {base[0][1]} {base[0][0]}.\n\n'
    return result[:-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
