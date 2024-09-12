
'''print(123)
print(98,6)'''

'''x = 2
x = x + 2
print(x)
y = 440 * 12
print(y)
z = 4*33
print(z)'''

'''print(10/2)
print(9/2)
print(99/100)
print(10.0 / 3.0)
print(99.0 / 100.0)'''

'''print(10 *"? _ ?")
print(5 * "a @ b ")
   
def stringMultiply(a,b):
    print(a * b)
stringMultiply(5, "a")'''

#print(ord("b"))
#print(chr(97))

'''print(2, -1, 3,14, -2,8)
print(type(3), type(3.14), type(3.0))
print(int(3.14), int(-5.2))
print(float(3), float(-1))

print(5.0 / 2.0, 5/2, 5/2.0, 5.0/2,5.0 //\
      2.0)
print(-5 // 2, 5 // 2)'''

'''temp_F = 86
temp_C = 5.0 / 9.0 * (temp_F -32)
print(temp_C)
temp_F = 9.0 / 5.0 * temp_C + 32
print(temp_F)'''

'''def fahrenheit_to_celsius(f):
    return 5.0 / 9.0 * (f - 32)

def celsius_to_fahrenheit(c):
    return c * 9.0 / 5.0 + 32

fahrenheit_temps = [32, 68, 100]
celsius_temps = list(map(fahrenheit_to_celsius, fahrenheit_temps))
print(celsius_temps)

celsius_temps = [0, 20, 37]
fahrenheit_temps = list(map(celsius_to_fahrenheit, celsius_temps))
print(fahrenheit_temps)'''

'''print(isinstance(30.0,type(3.0)))
print(isinstance(30.1, type(3.1)))
print(isinstance('abc', type('aaa')))
print(isinstance([], type([10, 2, 30])))
print(isinstance({1:2}, type({30:40})))
print(isinstance(3,int))
print(isinstance('aaa', str))
print(isinstance([], list))
print(isinstance({1:2}, dict))
print(isinstance(set([1,4]), set))'''

'''print(type(30))
print(type(30.2))
print(type('As'))
print(type(True))
print(type(None))
print(type([1, 2, 3]))
print(type({1:20}))
print(type(set([10, 20, 30])))
print(type(int))
print(type(5==8))

def f():
    return 30
print (type(f))

def getType(a):
    print(type(a))

getType(10)'''

'''from functools import reduce
print(reduce(lambda x,y: x*y, [1,2,3]))'''  

#x<y, x<=y, x>y, x>=y, x!=y, x is y, x is not y

'''print(True and not(2==2))
print(20 < 30)
print(False < True)
print('abc' <= 'ad')
print(2 <= 2)
print([1, 3] > [1, 2, 3])
print(3 > 2)
print(set([1, 3, 4]) > set([3, 4]))
print('xyz' >= 'abc')   
print(2 == 2)
print(set([1, 5, 10]) == set([10, 1, 5]))
print(3 !=3)
s = set([1, 5, 10])
print(s is s)
print(set([1, 5, 10]) is not set([10, 1, 5]))'''

'''print(eval('4+5+2*10'))

def greet(name):
    return f"Hello, {name}!"
code = "greet('Alice')"
print(eval(code))'''

'''exec('for x in [3,4,5]: print(x)')'''


'''x = (1,2,3)
new_tuple = x + (10,20)
print (new_tuple)'''

'''print("Tuples")
x = ('Adam', 'Ewa', 'Jacek')
print(x[2])  # Drukuje 'Jacek'

y = (1, 9, 2)
print(y)  # Drukuje (1, 9, 2)
print(max(y))  # Drukuje maksymalną wartość z krotki y, czyli 9

for iter in y:
    print(iter)  # Drukuje wszystkie elementy z krotki y

(x, y) = (4, "Ewa")
print(y)  # Drukuje 'Ewa'

(a, b) = (98, 99)
print(b)  # Drukuje 99

a, b = (98, 99)
print(a)  # Drukuje 98

d = dict()
d['a'] = 2
d['b'] = 4

for (k, v) in d.items():
    print(k, v)  # Drukuje klucz i wartość z słownika

tups = d.items()
print(tups)  # Drukuje elementy słownika jako pary (klucz, wartość)

print(u"Tuples są porównywalne")
print((0, 1, 2) < (5, 1, 2))  # Porównanie krotek - zwróci True

# Poprawnie zdefiniowany słownik:
d = {'a': 10, 'b': 4, 'c': 90}

t = d.items()
print(t)  # Drukuje elementy słownika jako pary (klucz, wartość)

m = sorted(d.items())
print(m)  # Drukuje posortowane pary (klucz, wartość) według klucza

for k, v in sorted(d.items()):
    print(k, v)  # Drukuje posortowane klucze i wartości'''

'''print(tuple())
print(tuple('abc'))
print(tuple([1, 2, 3, 4, 5]))
print(tuple((1, 2, 3, 4, 5)))
print(tuple(set([1, 2, 3, 4])))
print(tuple({1:2, 3:4}))
print(tuple(enumerate(['a', 'b', 'c', 'd'])))'''

'''print(set())
print(set('abcd'))
print(set([1, 2, 3, 4, 5, 3 ,5]))
print(set((1, 2, 3, 4, 5)))
print(set(set([1, 2, 3, 4])))
print(set({1: 2, 3: 4}))
print(set(enumerate({'a', 'b', 'c', 'd'})))'''

'''result = set([1, 2, 3, 4, 5]).union(set([5, 6, 7]))
print(result)

result1 = set([1, 2, 3, 4, 5]).intersection(set([5, 6, 7]))
print(result1)

result2 = set([1, 2, 3, 4, 5]).difference(set([5, 6, 7]))
print(result2)

result3 = set([1, 2, 3, 4, 5]).symmetric_difference([5, 6, 7])
print(result3)'''


'''s = set([1, 2, 3, 4, 5])
s.update(set([5, 6, 7]))
print(s)

s1 = set([1, 2, 3, 4, 5])
s1.intersection_update(set([5, 6, 7]))
print(s1)

s2 = set([1, 2, 3, 4, 5])
s2.difference_update(set([5, 6, 7]))
print(s2)

s3 = set([1, 2, 3, 4, 5])
s3.symmetric_difference_update(set([5, 6, 7]))
print(s3)'''