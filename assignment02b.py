"""
Assignment 2-B
==============

Wrap Assignment 1-B in function `poem()` that satisfies the doctest:

>>> from pathlib import Path
>>> poem() == Path('data/poem-ru.txt').read_text(encoding='utf8')
True
"""
import re

def poem():
    result = ''
    data = [['Вот дом, который построил Джек.', 'В доме, который построил Джек.'],
            ['А это пшеница,', 'Которая в тёмном чулане хранится'],
            ['А это весёлая птица-синица,', 'Которая часто ворует пшеницу,'],
            ['Вот кот,', 'Который пугает и ловит синицу,'],
            ['Вот пёс без хвоста,', 'Который за шиворот треплет кота,'],
            ['А это корова безрогая,', 'Лягнувшую старого пса без хвоста,'],
            ['А это старушка, седая и строгая,', 'Которая доит корову безрогую,'],
            ['А это ленивый и толстый пастух,', 'Который бранится с коровницей строгою,'],
            ['Вот два петуха,', 'Которые будят того пастуха,']]

    for i in range(len(data)):
        if i == 0:
            result += f'{data[i][i]}\n\n'
        else:
            for j in range(i, -1, -1):
                if j == i:
                    result += f'{data[j][0]}\n' + re.sub(r'Лягнувшую(.+,)', r'Лягнувшая\1', data[j][1]) + '\n'
                else:
                    result += f'{data[j][1]}\n\n' if j == 0 else f'{data[j][1]}\n' 
    return result[:-1]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
