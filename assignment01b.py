"""
Assignment 1-B (optional)
=========================

This assignment is similar to 1-A except that the poem is in Russian now.
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
            # print(data[i][i] + '\n')
            result += f'{data[i][i]}\n\n'
        else:
            for j in range(i, -1, -1):
                if j == i:
                    # print(data[j][0] + '\n' + re.sub(r'Лягнувшую(.+,)', r'Лягнувшая\1', data[j][1]))
                    result += f'{data[j][0]}\n' + re.sub(r'Лягнувшую(.+,)', r'Лягнувшая\1', data[j][1]) + '\n'
                else:
                    # print(data[j][1] + '\n' if j == 0 else data[j][1])
                    result += f'{data[j][1]}\n\n' if j == 0 else f'{data[j][1]}\n' 
    return result[:-1]
    
if __name__ == '__main__':
    print(poem())    
