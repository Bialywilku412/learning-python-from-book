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

'''print(list(range(5)))             # Output: [0, 1, 2, 3, 4]
print(list(range(1, 10)))         # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(range(-3, 10, 20)))    # Output: [-3]
print(list(range(100, -50, -20))) # Output: [100, 80, 60, 40, 20, 0, -20, -40]'''

'''
print(any([False, False, False]))  # Output: False
print(any([False, True, False]))   # Output: True
print(any([]))                     # Output: False
print(any((0, 3)))                 # Output: True
print(any('abc'))                  # Output: True'''
'''
print(all([False, False, False]))  # Output: False
print(all([False, True, False]))   # Output: False
print(all([]))                     # Output: True
print(all((0, 3)))                 # Output: False
print(all('abc'))                  # Output: True'''
'''
print([])                               # Output: []
print([1, 2, 3, 4, 5])                  # Output: [1, 2, 3, 4, 5]
print([(1, 2), 'Ewa', 3, ['a', 'b', 'c']])  # Output: [(1, 2), 'Ewa', 3, ['a', 'b', 'c']]'''
'''
print(list())                               # Output: []
print(list('abc'))                          # Output: ['a', 'b', 'c']
print(list((1, 2, 3, 4, 5)))                # Output: [1, 2, 3, 4, 5]
print(list(set([1, 2, 3, 4])))              # Output: [1, 2, 3, 4] (order may vary)
print(list({1: 2, 3: 4}))                   # Output: [1, 3]
print(list(enumerate(['a', 'b', 'c', 'd']))) # Output: [(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]'''
'''
numb = [4, 8, 19, 0]
numb[1] = 27
print(numb)  # Output: [4, 27, 19, 0]'''
'''
L = [1, 2, 3]
L.append(4)
L.append([5, 6, 7])
print(L)  # Output: [1, 2, 3, 4, [5, 6, 7]]'''
'''
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list1.append([4, 5, 6])
list2.extend([4, 5, 7])
print(list1)  # Output: [1, 2, 3, [4, 5, 6]]
print(list2)  # Output: [1, 2, 3, 4, 5, 7]'''
'''
a_list = [1, 2, 3]
a_list.append([1, 2, 3])
print(a_list)  # Output: [1, 2, 3, [1, 2, 3]]'''
'''
def list21listlist(L, m, n):
    # Returns a list of lists where each sublist contains `m` elements
    return [[L[i + k * m] for i in range(m)] for k in range(n)]

# Test the function
print(list21listlist([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 5, 4))
print(list21listlist([0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0], 3, 3))'''
'''
L = ['a', 'b', 'b']
L.insert(1, 'x')
print(L)  # Output: ['a', 'x', 'b', 'b']
L.insert(0, 'y')
print(L)  # Output: ['y', 'a', 'x', 'b', 'b']
L.insert(5, 'z')
print(L)  # Output: ['y', 'a', 'x', 'b', 'b', 'z']'''
'''
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(lista[1], lista[-3], lista[2:6], lista[::-2])
# Output: 2 7 [3, 4, 5, 6] [0, 8, 6, 4, 2]'''
'''
L = ['a', 'b', 'c', 'd']
L.remove('d')
print(L)'''

'''L = ['a', 'b', 'c', 'd']
print(L.pop(1))
print(L)'''

'''d_list = [1, 2, 3]
d_list.reverse()
print(d_list)  # Output: [3, 2, 1]'''

'''e_list = [2, 1, 3, 2]
e_list.sort()
print(e_list)  # Output: [1, 2, 2, 3]'''

'''from operator import mul
def kw_list1(num):
    res = []
    for n in num:
        res.append(n * n)
    return res
print(kw_list1([4, 5, -2]))

def kw_list2(num):
    return[n**2 for n in num if n ** 2 < 20]
print(kw_list2([4, 5, -2]))'''

'''def dod_list_list(lists):
    return list(map(sum, lists))

# Correct function call
print(dod_list_list([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 2, 4], [1, 1, 1, 1]]))'''

'''from operator import mul
def il_list_list(a1,a2):
    return(map(mul,a1,a2))
print(list(il_list_list([1,2,3,4], [5,6,7,8])))'''

'''def ranges(N):
    return N[0] >= 0 and N[0] <= 100 and N[1] >= 0 and N[1] <= 100

def ranges1(M):
    res = []
    for N in M:
        if ranges(N):
            res.append(N)
    return res

print(ranges1([[-5, 40], [30, 20], [70, 140], [60, 150]]))'''

'''print([1, 24, 76])
print("red", "yellow", "blue")
print(["red", 24, 79.6])
print([1, [5, 6, 7], 8]); print([])

for i in [1, 2, 3, 4]:
    print (i)

fs = ['Adam', 'Ewa', 'Ola']
for f in fs:
    print(u"Szczesliwego Nowego Roku", f)

print(fs[1])
print(len(fs))
print(range(len(fs)))

for i in range(len(fs)):
    friend = fs[i]
    print(u"Szczesliwego Nowego Roku:", f)'''


























