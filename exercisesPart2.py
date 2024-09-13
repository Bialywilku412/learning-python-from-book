'''print(list())
print(list('abc'))
print(list([1, 2, 3, 4, 5]))
print(list((1, 2, 3, 4, 5)))
print(list(set([1, 2, 3, 4])))
print(list(enumerate(['a', 'b', 'c', 'd'])))'''

'''print(sum([10, 20, 30]))
print(sum((10, 20, 30)))
print(sum(set([10, 20, 30])))
print(sum([10, 20, 30], 2))'''

'''print(len(''))
print(len([2, 35, -2, 12]))
print(len((2, 35, -2, 2)))
print(len(set([12, 35, -2, 12])))'''

'''print(max(2, 35, -2, 12))
print(max('c', 'y', "Ewa", 'z', 'z'))
print(max([2, 35, -2, 12]))
print(max(['c', 'x', 'kot', 'pies']))
print(max((2, 35, -2, 12)))
print(max({1:2, 3:4}))
print(max(set([2, 35, -2, 12])))'''

'''print(min(2, 35, -2, 12))
print(min('c', 'x', 'kot', 'pies'))
print(min([2, 35, -2, 12]))
print(min(['a', 'x', 'kot', 'pies']))
print(min((2, 35 -2, 12)))
print(min(set([2, 35, -2, 12])))'''

'''a = ('abcd', '1234', (5, 6, 7, 8))
print(zip(a))
print(zip([1, 2, 3, 4], ['a', 'b', 'c']))
print(zip( {1:2,3:4}, set({5, 6})))
print(zip( [5, 6, 7, 8]))
print(zip())
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = ['z', 'y', 'x', 'w', 'v']
for letter1, letter2 in zip(list1, list2):
    print(letter1 + letter2)'''

'''def kwadrat(n):
    return n * n
print(list(map(kwadrat, [3, 11, 1])))'''

'''def dod(n):
    return n > 0
print(filter(dod, [3, -7, 1]))
print(filter(dod, (3, -7, 1)))
print(filter(dod, set([3, -7, 1])))

def a_lub_b(x):
    return x == 'a' or x == 'b'
print(filter(a_lub_b, 'acdba'))
print(filter (None, [set(), 3, {}, 0, False, '', -2, []]))'''

'''from functools import reduce
def add(x, y):
    return x + y
print(reduce(add, [3, -7, 1]))

print(reduce(add, (3, -7, 1), 12))

def maximum(x, y):
    if x >= y:
        return x
    else:
        return y
print(reduce(maximum, 'acdba', 'a'))

print(reduce(maximum, 'acdba', 'z'))
def sec(x, y):
    return y
print(reduce(sec, [3,5]))'''

'''print(list(enumerate(['a', 'b', 'c', 'd'])))
print(list(enumerate(['a', 'b', 'c', 'd'], 5)))'''

'''lista = [4,5,8,2]

szesciany = []
for liczba in lista:
    szescian = liczba ** 3
    szesciany.append(szescian)
print(szesciany)'''

'''lista = [4, 5, 8, 2]

# Używanie lambda z map do obliczenia sześcianów dla każdego elementu listy
sześciany = list(map(lambda x: x**3, lista))

print(sześciany)  # Wynik: [8, 64, 216, 512]'''

'''lista = [4, 5, 8, 2]

def szeciany(x):
    return x**3

szesciany = list(map(szeciany, lista))
print (szesciany)'''








