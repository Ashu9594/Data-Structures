from tkinter import *

class Stack(Tk):
    def __init__(self):
        super().__init__()
        self.stack = []
        self.title = "Stack"
        self.geometry("400x400")

    def widgets(self):
        self.var = StringVar()
        #listbox
        self.lb = Listbox(self)
        self.lb.pack()
        #EntryBox
        self.text2 = Entry(textvariable=self.var)
        self.text2.pack()
        #buttonPush
        self.btn1 = Button(text ="Push",command = self.pushOp)
        self.btn1.pack()
        #buttonPop
        self.btn2 = Button(text ="Pop",command = self.popOp)
        self.btn2.pack()
        #buttonPrint
        self.btn3 = Button(text ="Print",command = self.printOp)
        self.btn3.pack()

    def pushOp(self):
        
    def popOp(self):
        pass
    def printOp(self):
        pass
stack = Stack()

if __name__ == "__main__":
    window = Stack()
    window.widgets()
    window.mainloop()
