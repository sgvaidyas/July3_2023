'''t1 = (11,22,33,44,55)
t2 = (1,2,3)
#concat
t3 = t1+t2
print(t3)
#replication
t4 = t1*3
print(t4)
#membership operator
print(44 in t1)
print(44 not in t1)
print(144 in t1)
print(144 not in t1)
'''





t = (11,22,33,44,55,66,77,88)
print("Elements of the tuple")
for x in t:
    print(x)

print("Elements of the tuple using range")
for i in range(len(t)):
    print(t[i])

t = (11,22,33,44,55,66,77,88)
print("t[:]           = ",t[:])
print("t[2:]          = ",t[2:])
print("t[2:6]         = ",t[2:6])
print("t[2:6:2]       = ",t[2:6:2])
print("t[-2:-6:-1]    = ",t[-2:-6:-1])
print("t[::-1]        = ",t[::-1])













