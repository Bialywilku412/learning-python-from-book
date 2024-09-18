'''lot = [32, 7, 67, 89, 4]
print(lot)
lot[2] = 21
print(lot)'''

'''a = 42
b = list(a + i for i in range(10))
print(b)'''

'''przedmiot = ['wazon', 'szklanka', 'laska', 'okulary']
cena = [10, 4, 32, 68]
print(cena[przedmiot.index('szklanka')])'''

'''print({})
print({1:'a', 2:'b', 9:'c'})
print({1:'a',
(5,'item'):[100],
'key':{'True':'hello', 9:0}})'''

'''print(dict())
print(dict([(1, 'a'), (2, 'b'), (3, 'c')]))
print(dict(((1, 'a'), (2, 'b'), (3, 'c'), (3, 'd'))))
print(dict(set([(1, 'a'), (2, 'b'), (3, 'c')])))
print(dict({1:'a', 2:'b', 3: 'c'}))
print(dict(enumerate(['a', 'b', 'c', 'd'])))'''

'''print({1: 'a', 2: 'b', 3: 'c'}[2])

print({1: 'a', 2: 'b', 3: 'c'}.get(2))
print({1: 'a', 2: 'b', 3: 'c'}.get(7))

print({1: 'a', 2: 'b', 3: 'c'}.get(7, 'xyz'))

d = {1: 'a', 2: 'b', 3: 'c'}
d[2] = 'd'
print(d)
d[5] = 'e'
print(d)'''

'''przedmiot_cena = dict((('wazon', 10), ('szklanka', 4), ('laska', 32), ('okulary', 65)))
print(przedmiot_cena)

przedmiot = ['wazon', 'szklanka', 'laska', 'okulary', 'rower']
nowa_cena = [11, 4, 36, 69, 300]
przedmiot_nowa_cena = (dict(zip(przedmiot, nowa_cena)))
przedmiot_cena.update(przedmiot_nowa_cena)
print(przedmiot_cena)

print({}.fromkeys(przedmiot, 12))
komentarz = ''Podajemy aktualne ceny. Wazon kosztuje %(wazon)s rower kosztuje %(rower)s''
print(komentarz % przedmiot_nowa_cena)'''

'''print(2 in {1: '1', 2: 'b', 3: 'c'})
print(4 in {1: '1', 2: 'b', 3: 'c'})'''

'''print({1: 'a', 2: 'b', 3: 'c'}.items())
s_dict = {1: 'a', 2: 'b', 3: 'c'}
for key, value in s_dict.items():
    print( key, 'maps to', value)'''

'''print({1: 'a', 2: 'b', 3: 'c'}.keys())'''
# -*- coding: utf-8 -*-

'''print({1: 'a', 2: 'b', 3: 'c'})
s_dict = {1: 'ab', 2: 'bc', 3: 'cd'}
for value in s_dict.values():
    print(value, u'jest wartoscia w slowniku')'''

'''def listrange2dict(L):
    return {i : L[i] for i in range(len(L))}
print(listrange2dict(['acs', 1, 2, 3, 'abv']))'''

'''p = dict()
p['moneta'] = 12
p['banknot'] = 3
p['cena'] = 2
print(p)

print(p['cena'])

p['banknot'] = p['banknot'] + 2
print(p)'''

'''cs = dict()
ns = ['aa', 'bb', 'cc', 'aa', 'bb', 'bb']

for n in ns:
    if n not in cs:
        cs[n] = 1  # Initialize count to 1 if the string is not already in the dictionary
    else:
        cs[n] = cs[n] + 1  # Increment the count by 1 if the string is already in the dictionary
    print(cs)
    
    if n in cs:
        print(cs[n])  # Print the current count of the string
    else:
        print(0)  # This won't execute because the key will always exist due to the previous code
    
    print(cs.get(n, 0))  # Print the value of the key using the .get() method, with 0 as the default if not found'''

'''rok = {'Sty':1, 'Lut':2, 'Mar':3, 'Kwi':4, 'm':'x'}
print(rok)
print(list(rok))
print(rok.values())
print(rok.keys())
print(rok.items())'''

