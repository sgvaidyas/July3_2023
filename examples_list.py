'''
l=[11,22,"jhgjjhj",True]
print(len(l))
print("Elements = ")
for x in l:
    print(x)
'''

'''
l = []
num = int(input("Enter the no of ele "))
for i in range(num):
    ele = input("Enter ele = ")
    l.append(ele)

print(l)
'''

'''
l=[11,22,33]
for i in range(len(l)):
    print(l[i])
    l[i]=55

print(l)

'''

'''
a = [11,22,33,44]
b = [222,333]
c = a+b
print(c)


'''



'''l = [10,20,30,40,50,55,66,77,88,99,00,22,3,44,56,6,76,7,89]
print(len(l))
for i in range(-(len(l)),0):
    print(i," l[i] = ", l[i])

'''



   # 0  1  2  3  4  5  6  7  8
l = [11,22,33,44,55,66,77,88,99]
   # -9 -8 -7 -6 -5 -4 -3 -2 -1

print(l[-7:-3:-1])
'''print("l[::-1]           = ",l[::-1])
print("l[-1:-7:-1]       = ",l[-1:-7:-1])
print("l[-1:-7:-2]       = ",l[-1:-7:-2])
print("l[-1:-7]       = ",l[-1:-7])
print("l[:-7:-1]       = ",l[:-7:-1])
print("l[1:-5]       = ",l[1:-5])
print("l[-8:7]       = ",l[-8:7])'''









'''
print("l[:]       = ",l[:])
print("l[2:]      = ",l[2:])
print("l[2:7]     = ",l[2:7])
print("l[:7]      = ",l[:7])
print("l[2:8:2]     = ",l[2:8:2])
'''
'''
l=[11,22,33,44]
print(l.pop())
print(l)
print(l.pop(2))
print(l)
'''


l = [11,22,33,44,55,33,33]
print(l.index(33))
print(l.count((33)))

l.extend([999,666])
print(l)

l.append([1,2,3,4])
print(l)

a = [222,1,3,44,55]
a.sort()
print(a)
a.sort(reverse=True)
print(a)












