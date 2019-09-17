from tkinter import *
#from tkinter import messagebox

class Stack(Frame):
    def __init__(self,master):
        Frame.__init__(self,master)
        self.grid()
        self.text = StringVar()
        self.create_widget()
        
    def create_widget(self):
        self.lb = Listbox(self)
        self.lb.grid()
        self.text2 = Entry(textvariable=self.text)
        self.text2.grid()
        self.btn1 = Button(text ="Push",command = self.pushOp)
        self.btn1.grid()
        self.btn2 = Button(text ="Pop",command = self.popOp)
        self.btn2.grid()
        self.btn3 = Button(text ="Print",command = self.printOp)
        self.btn3.grid()
    def pushOp(self):
        pass
    def popOp(self):
        pass
    def printOp(self):  
        pass

root = Tk()
root.geometry("150x330")
app = Stack(root)
root.mainloop()

# window.geometry("400x400")
# window.mainloop()
# window = Tk()
# b = StringVar()

# listbox = Listbox(window)
# listbox.pack()

# text2 = Entry(textvariable=b) 
# text2.pack()


# def push():
#     listbox.insert(END,b.get()) 
# def pop():
#     listbox.delete(first=0,last=0)
    
# btn1 = Button(window, text ="Push",command =lambda: push())
# btn1.pack()
# btn2 = Button(window, text ="Pop",command = lambda: pop())
# btn2.pack()
# btn3 = Button(window, text ="Print")   
# btn3.pack()