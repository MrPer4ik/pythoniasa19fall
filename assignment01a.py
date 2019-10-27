"""
Assignment 1-A
==============

Write fuction that generates the text below; use at least variables and f-strings.
For those who are already familiar with Python – write the best code you can to conform to the Zen of Python.

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
                # print(f'This is {base[j][0]}', end='')
                result += f'This is {base[j][0]}'
            else:
                # print(f'That {base[j][1]} {base[j][0]}', end='')
                result += f'That {base[j][1]} {base[j][0]}'
            # print(',' if j > 1 else '')
            result += ',\n' if j > 1 else '\n'
        #print(f'This is {base[i][i]}.' if i == 0 else f'That {base[0][1]} {base[0][0]}.', end='\n\n')
        result += f'This is {base[i][i]}.\n\n' if i == 0 else f'That {base[0][1]} {base[0][0]}.\n\n'
    return result[:-1]

if __name__ == '__main__':
    print(poem())
