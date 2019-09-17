class Stack():
    def __init__(self):
        self.stack = []
    def push(self,item):
        self.stack.append(item)
    def pop(self):
        if self.stack == []:
            return -1
        else:
            return self.stack.pop() 
    def display(self):
        return self.stack
    def topData(self):
        try:
            n = len(self.stack)
            return self.stack[n-1]
        except:
            print("First Add Data")

stack = Stack()
choice = 0
while(1):
    print(" Select Operations")
    print("1) Push")
    print("2) Pop")
    print("3) TopData")
    print("4) Exit")
    try:
        print(stack.display())
        choice = int(input("Your Choice: "))
    except:
        print("Please enter valid Input")
    if(choice == 1):
        print(stack.display())
        number = int(input("Push Number: "))
        stack.push(number)
    elif(choice == 2):
        number = stack.pop()
        if (number == -1):
            print ("stack is empty")
        else:
            print("Popped Number is : ", number)
    elif(choice == 3):
        print('Top eliment is : ', stack.topData())
    elif (choice == 4):
        break
    else:
        continue



    # def pushOp():
    #     num = input("Insert a number:")
    #     if num.isdigit():
    #         global stack
    #         stack.push(num)
    #     else:
    #         print("invalid input")
    # def popOp():
    #     global stack
    #     n = stack.pop()
    #     if n != -1: 
    #         print(f"deleted data: {n}")
    # def displayOp():
    #     global stack
    #     stack.display()
    # def exitOp():