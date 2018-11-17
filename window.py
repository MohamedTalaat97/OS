from tkinter import *
import tkinter.ttk as ttk

class Window:
    def __init__(self,r):
        self.AlgoLabel=Label(r, text='Choose Algo')
        self.FileLabel = Label(r, text='File Name')
        self.ErrorLabel = Label(r, text='')
        self.FileEntry = Entry(r)
        self.ContextLabel = Label(r, text='context')
        self.ContextEntry = Entry(r)
        self.QuantumLabel = Label(r, text='RR quantum')
        self.QuantumEntry = Entry(r)
        self.combo =  ttk.Combobox(root, values=("FCFS", "HPF", "RR", "STRF"))
        self.combo.bind('<<ComboboxSelected>>', self.callback)
        self.bt = Button(r, text='ok')
        self.AlgoLabel.grid(row=2)
        self.combo.grid(row=2,column=1)
        self.FileLabel.grid(row=3)
        self.FileEntry.grid(row=3, column=1)
        self.ContextLabel.grid(row=4)
        self.ContextEntry.grid(row=4, column=1)
        self.bt.grid(row=6)
        self.ErrorLabel.grid(row=6,column=1)
        self.bt.bind("<Button-1>", self.done)
        self.data=[]
    

    def callback(self,event):
        if self.combo.get() == 'RR':
            self.QuantumLabel.grid(row=5)
            self.QuantumEntry.grid(row=5, column=1)
        else:
            self.QuantumLabel.grid_forget()
            self.QuantumEntry.grid_forget()
        
    def done(self, event):
        if self.FileEntry.get() == '' or self.ContextEntry.get() == '' or self.combo.get() == '' :
           self.ErrorLabel['text'] = 'please enter all fileds '
        elif not str.isdigit(self.ContextEntry.get()):
            self.ErrorLabel['text'] = 'please enter a valid context '
        elif (not str.isdigit(self.combo.get())) and self.combo.get() == 'RR':
            self.ErrorLabel['text'] = 'please enter a valid Quantum '    
            
        else:
             if self.combo.get() == 'RR':
                 '''
                 call functions
                 '''
        

     
        

   


root = Tk()
w=Window(root)















root.mainloop()
print(len(d))


