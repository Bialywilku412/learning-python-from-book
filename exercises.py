
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