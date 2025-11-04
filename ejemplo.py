from tkinter import *
from tkinter import ttk


raiz=Tk()

def abrir():
    new=Toplevel(raiz)
    new.title("This is new")
    new.geometry("300x200")
    Label(new,text="Hello").pack(pady=20)
    Button(new,text="Previous" , command=new.destroy).pack(pady=10)

raiz.geometry("400x300")

notebook=ttk.Notebook(raiz)
notebook.pack(expand=True,fill='both')

tab1=ttk.Frame(notebook)
tab2=ttk.Frame(notebook)

notebook.add(tab1,text="Tab 1")
notebook.add(tab2,text="Tab 2")


btn=Button(tab1,text="abrir",command=open)
btn.pack(pady=50)
raiz.mainloop()