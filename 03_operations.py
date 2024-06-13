from tkinter import *
from tkinter import ttk

root = Tk()
root.title("03 Operaciones con conjuntos")
frm = ttk.Frame(root, padding=10)
frm.grid()

set_a = {'col', 'mex', 'bol'}
set_b = {'pe', 'bol'}

# union de conjuntos, 
set_c = set_a.union(set_b)
print(set_a | set_b)

# Intersection de conjuntos
set_d = set_a.intersection(set_b)
print(set_a & set_b)

# Diferencias entre conjuntos
set_e = set_a.difference(set_b)
print(set_a - set_b)

# Symetric Difference entre conjuntos
set_f = set_a.symmetric_difference(set_b)



ttk.Label(frm, text=set_c).grid(column=0, row=0)
ttk.Label(frm, text=set_d).grid(column=0, row=1)
ttk.Label(frm, text=set_e).grid(column=0, row=2)
ttk.Label(frm, text=set_f).grid(column=0, row=3)

# El metodo loop siempre al final
root.mainloop()
