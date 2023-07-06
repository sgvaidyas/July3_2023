master = {}
while True:
    ch = input("Press 1 to enter record ")
    if ch == "1":
        roll=input("Enter roll = ")
        name=input("Enter name = ")
        marks=eval(input("Enter marks = "))
        total=sum(marks)
        avg = total/(len(marks))
        master[roll] =[name,marks,total,avg]
    else:
        print(master)
        for k,v in master.items():
            print("Roll = ",k," = ",v)
        break

'''
master = []
while True:
    ch = input("Press 1 to enter record ")
    if ch == "1":
        roll=input("Enter roll = ")
        name=input("Enter name = ")
        marks=eval(input("Enter marks = "))
        total=sum(marks)
        avg = total/(len(marks))
        l =[roll,name,marks,total,avg]
        master.append(l)
    else:
        for x in master:
            print(x)
        break


'''
