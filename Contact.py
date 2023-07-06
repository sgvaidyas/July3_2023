records = []
def insert():
    name = input("Enter name")
    phone = input("Enter phone")
    rec = [name,phone]
    records.append(rec)

def display():
    print("------RECORDS-------")
    for x in records:
        print(x)
        print("-------------------")


def search():
    key = input("enter the name of contact = ")
    flag = 0
    for x in records:
        if x[0]==key:
            print("Search Record found!!!!")
            print(x)
            flag=1
            break
    if flag==0:
        print("Not found!")

def edit():
    key = input("enter the name of contact = ")
    flag = 0
    for i in range(len(records)):
        if records[i][0]==key:
            print("Search Record found!!!!")
            records[i][1]=input("Change phone num ")
            flag=1
            break
    if flag==0:
        print("Contact Not found!")

while True:
    print("1 Insert 2 SEARCH 3 EDIT 4 Display 5 Exit")
    ch = int(input("Enter choice = "))
    if(ch==1):
        insert()
    elif(ch==2):
        search()
    elif(ch==3):
        edit()
    elif(ch==4):
        display()
    elif(ch==5):
        break
    else:
        print("consult doc!")
