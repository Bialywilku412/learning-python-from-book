'''comment'''
#comment

#import ...
#from... import*
#import...as...

#print(u'Hello\nWorld')


'''formatowanie'''
#a, b = 56.98432, 42
#print("liczba a wynosi %4.2f%%" % a)
#print("liczba a wynosi %d%%" % a)
#print("liczba a wynosi %d" % a)
#print('%s %d jest parzysta a liczba %g jest float.' \
#      % ('Liczba', b, a))


'''wyrazenia arytmetyczne'''
#print(5.04**-15)
#print(31 % 4)

'''string'''
#x = "Witam";
#y = "uczniowie";
#print(x, y)
#print("I wish I didn't have to work so hard")

'''porownania'''
#print (6==4)
#print(type(4==4))
#print(3 < 4 < 8 != 2)
#print('*****')

'''pętle'''
#x = -8
#y = 3
#print(2 **(y+1) if x+3<0 else 2 **y-1)

#A = 5
#k = 1
#while (k < 6):
    #A += k
    #k += 1
    #print(A)
#print('*****')
#A = 0
#k = 1
#while (k < 6):
    #A += k
    #if k == 3:
        #break
    #print('k=%d,A=%d' %(k,A))
    #k += 1
    #print(A)
#print('*****')
#A = 0
#k = 1
#while (k < 6):
    #A += k
    #k += 1
    #if k == 3:
        #continue
    #print('k=%d,A=%d' %(k,A))
    #print(A)
#for i in range (2,15,2):
    #print(i)
#print([i for i in range (2,15,3) if (i <= 10) \
        #& (i > 2)])
