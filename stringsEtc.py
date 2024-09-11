#print ({1+2, 3, 'a'})
#print(len({'a', 'b', 'c' , 'a', 'a'}))
#print(sum({5,6,7}))


#A = {1,8,9}
#print(2 in A)
#print(2 not in A)

#b = {3,4,5,6}
#c = {5,6,7,8}
#print(b|c)
#print(b&c)

'''D = {3, 4, 5}
D.add(8)
D.remove(3)
D.intersection_update({10, 4, 5, 9})
print(D)
E = D
E.remove(5)
print(E,D)
F = D.copy()
D.add(7)
print(D,F)'''

"comprehension"
'''print({x**2 for x in {4,5,6,7}&{6,7} if x!=6})
print({x*y for x in{2,3} for y in {3,4}})
print({x*y for x in{2,3} for y in {3,4} if x != y})'''

"""print([1,1+10,4-10], {3*2,5,16}, "yes")
print(len([[1,1+10,4-10], {3*2,5,16}, "yes"]))
print(sum([2,3,4,5,6]))

print([10,20,30] + ['nasz', 'python'])
print([10,20,30] + [u"nasz", "python"])"""

'''print(sum([ [1,2,3], [4,5,6], [7,8,9] ], []))
print([3*y for y in {9,8,7,6}])
print([a*b for a in [1,2,3] for b in [2,3,4]])'''

'''lista = [1,2,3,4,5,6,7,8,9]
print(lista[:3])
print(lista[6:])
print(lista[::3])

[a,b,c,d,e,f,g,h,j] = lista
print(d, a)
print([d, a])

L1 = [[2,3],[5,1],[4,8],[0,9]]
print([y for [x,y] in L1])'''

'''print((1,2 +3,4))
print({3, (9,0)} | {(2, 1, 8)})'''

'''#a,b = 4,6
#a.b = (5,0)

print([b for (a,b) in [(5,'A'),(6,'B'), (7,'C')]])

print(set([1,3,5]))
print(list({1,3,5}))
print(tuple({1,3,5}))'''

'''print(range(4))
print(range(len([5,6,7,8])))
print(range(2,8,1))'''

'''print(list(zip([1,2,3], [4,5,6])))
print([x*x for x in reversed([1,2,3])])'''

'''fun = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, \
       'Z':25}
print (fun)

print(fun['F'])
print(fun.keys())
print(fun.values())'''

'''d1 = [{'Jan':'Kowalski','Jerzy':'Nowak'}]\
,{'Ewa':'Kot','Jan':'Burak'}
k = 'Jan'
print( [xx[k] for xx in d1])'''

'''def kwadrat(z): return z**2
print(kwadrat(2))'''