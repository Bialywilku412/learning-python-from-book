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

#print("abc")
#print("""cde""")
#print('abc')
#print('''efghi''')
#print("")
#print(r"abcd")
#print(r'abcg')
#print(r"""xyz""")
#print(r'''xyz''')

'''print(','.join('abcd'))
print('  '.join(['a', 'bc', 'd']))
print(''.join(['a', 'bc', 'd']))
print('x'.join(['a', 'bc', 'd']))
print(' '.join({'a': 'x', 'b': 'y'}))
print('     '.join(set(['a', 'b'])))'''

#print('pEAr'.capitalize())
'''print('abc123DEF'.upper())
print('abc123DEF'.lower())'''
'''
print('abcdabcd'.replace('bc', 'f'))
print('abcd abcd'.replace('bc', 'f', 1))
print('abcdabcdef'.replace('g', 'f'))
print('aaaaa'.replace('aa', 'f'))'''
'''
import time
print(time.strftime('%Y.%m.%d-%H:%M:%S'))'''


'''print('aabcdabcdabc'.find('bc'))
print('abcdabcd'.find('bc', 3))
print('abcdabcd'.rfind('bc'))
print('abcdabcd'.rfind('bc', 3))
print('abcdabcd'.find('f'))
print('abcdabcd'.rfind('f'))
print('abcdabcd'.find('bc', 6))
print('abcdabcd'.rfind('bc', 6))
print('abcdabcd'.find('bc', 3, 6))'''

'''
print(list('funkcja'))  # ['f', 'u', 'n', 'k', 'c', 'j', 'a']
print(tuple('funkcja')) # ('f', 'u', 'n', 'k', 'c', 'j', 'a')'''

'''
print('a b c'.partition('  '))
print('a b c'.partition(' '))
print('a b c'.rpartition('  '))
print('a b c'.rpartition(' '))'''

'''
print('a  bc d'.split())
print('a  bc d'.split(None))
print('a  bc d'.split(' '))
print('a  bc d'.split('  '))
print('a  bc d'.split('b'))
print('a  bc d'.split('bc'))'''
'''
print(''.isdigit())
print('1234'.isdigit())
print('1234abc'.isdigit())'''

'''
print('*' + 'abcd'.center(30) + '*')
print('abcd'.ljust(30) + '*')
print('abcd'.rjust(30))
print('*' + 'abcd'.ljust(30, '=') + '*')
print('abcd'.ljust(30, '_')+ '*')
print('abcd'.rjust(30, '-'))'''

'''print('zabawny string'.startswith('zab'))
print('zabawny string'.startswith('ing'))'''

'''print('zabawny string'.endswith('zab'))
print('zabawny string'.endswith('ing'))'''

'''print('     cde     fgh     '.strip())
print('     cde     fgh     '.strip(None))
print('aaababcdeababfghbaba'.strip('ab'))
print('     cde     fgh     '.lstrip())
print('aababcdeababfghbaba'.lstrip('ab'))
print('     cde     fgh     '.rstrip())
print('aababcdeababfghbaba'.rstrip('ab'))'''
'''
str1 = 'Hello'
str2 = ' There'
jn = str1 + str2
print(jn)'''
'''
str3 = '123'
x = int(str3) + 1
print(x)'''
'''
owoc = input('Enter: ')
x = int(owoc)- 10
print(x)'''
'''
owoc = "banan"
print(len(owoc))'''
'''
owoc = 'banan'
x = 0

# This will print each character of 'banan' with its index
while x < len(owoc):
    let = owoc[x]
    print(x, let)  # Prints index and letter
    x = x + 1

# After exiting the while loop, this will print each character of 'banan' on a new line
for let in owoc:
    print(let)  # Prints each letter on a new line'''
'''
word = 'banan'
ct = 0
for let in word:
    if let == 'a':
        ct = ct + 1
print(ct)'''





