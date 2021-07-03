set1 = {'A','B','C','D'}
set2 = {'C','D','E','F'}
set3 = {}
set4 = {}
set5 = {}

print(f'\nSet1 = {set1} \nSet2 = {set2}')
set3 = set1 | set2
#set3 = set1.union(set2)
print(f'União = {set3}')

set4 = set1 & set2
#set4 = set1.intersection(set2)
print(f'Intersecção = {set4}')

set5 = set1 - set2
#set5 = set1.difference(set2)
print(f'Diferença = {set5}\n')