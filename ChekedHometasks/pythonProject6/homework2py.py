school = {'1a': 24, '1b': 30, '10a': 16, '8a': 28, '6a': 32, '11a': 18, '4a': 34, '10b': 18, '6b': 24}
print(school['1a'])
school['1b'], school['10a'], school['6a'] = 26, 44, 12
school['4b'], school['2a'] = 22, 23
del school['10b']
print(school)
