num = input("Enter the number = ")
#"12345"
sum=0
for x in num:
    if x.isdigit():
        sum = sum+int(x)

print(sum)




'''num = int(input("Enter num "))
sum = 0

while num>0:
    r = num%10
    sum = sum+r
    num = num//10
print("Sum of dig =",sum)
'''
