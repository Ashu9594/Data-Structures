class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.start = None
    def insert_end(self,value):
        newNode = node(value)
        if (self.start == None):
            self.start = newNode
        else:
            val = self.start
            while val.next != None:
                val = val.next
            val.next = newNode
    def delete(self):
        if self.start==None:
            print("Linked list is empty")
        else:
            self.start = self.start.next
    def viewList(self):
        if self.start == None:
            print("Linked list is empty")
        else:
            val = self.start
            while val != None:
                print(val.data, " ",end=' ')
                val = val.next
mylist = LinkedList()
choice = 0
while(1):
    print("\n Select Operations")
    print("1) insert at End")
    print("2) delete")
    print("3) data")
    print("4) Exit")
    try:
        print(mylist.viewList())
        choice = int(input("Your Choice: "))
    except:
        print("Please enter valid Input")
    if(choice == 1):
        print(mylist.viewList())
        number = int(input("Insert Number: "))
        mylist.insert_end(number)
    elif(choice == 2):
        mylist.delete()
    elif(choice == 3):
        print(mylist.viewList())
    elif (choice == 4):
        break
    else:
        continue


