from tkinter import *
import tkinter.ttk as ttk

class Window:
    def __init__(self,r):
        self.AlgoLabel=Label(r, text='Choose Algo')
        self.FileLabel = Label(r, text='File Name')
        self.FileEntry = Entry(r)
        self.ContextLabel = Label(r, text='context')
        self.ContextEntry = Entry(r)
        self.QuantumLabel = Label(r, text='RR quantum')
        self.QuantumEntry = Entry(r)
        self.combo =  ttk.Combobox(root, values=("FCFS", "HPF", "RR", "STRF"))
        self.bt = Button(r, text='ok')
        self.AlgoLabel.grid(row=2)
        self.combo.grid(row=2,column=1)
        self.FileLabel.grid(row=3)
        self.FileEntry.grid(row=3, column=1)
        self.ContextLabel.grid(row=4)
        self.ContextEntry.grid(row=4, column=1)
        self.QuantumLabel.grid(row=5)
        self.QuantumEntry.grid(row=5, column=1)
        self.bt.grid(row=6)
        # self.cb.bind('<<ComboboxSelected>>', self.on_select)


root = Tk()
w=Window(root)
root.mainloop()