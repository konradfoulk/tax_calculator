from tkinter import *
from tkinter import ttk
from tax_calculator import find_required_income


def calculate():
    if desired_period.get() == 'annual':
        d = float(desired_income.get())
    elif desired_period.get() == 'monthly':
        d = float(desired_income.get())*12

    s = self_employed.get()
    i = find_required_income(d, s)

    if required_period.get() == 'annual':
        required_income.set(str(round(i, 2)))
    elif required_period.get() == 'monthly':
        required_income.set(str(round(i/12, 2)))

    etr.set(round(((i-d)/i)*100))


root = Tk()
root.title('Tax Calculator')
options = ['annual', 'annual', 'monthly']

self_employed = BooleanVar()
ttk.Checkbutton(root, text='Self employed',
                variable=self_employed).grid(column=1, row=0, columnspan=2, sticky=W)

desired_period = StringVar()
desired_income = StringVar()
ttk.Label(root, text='Desired').grid(column=0, row=1, sticky=E)
ttk.OptionMenu(root, desired_period,
               *options).grid(column=1, row=1)
ttk.Label(root, text='income:').grid(column=2, row=1)
ttk.Label(root, text='$').grid(column=3, row=1, sticky=E)
ttk.Entry(root, textvariable=desired_income).grid(column=4, row=1, sticky=W)

required_period = StringVar()
required_income = StringVar()
ttk.Label(root, text='Required').grid(column=0, row=2, sticky=E)
ttk.OptionMenu(root, required_period,
               *options).grid(column=1, row=2)
ttk.Label(root, text='income:').grid(column=2, row=2)
ttk.Label(root, text='$').grid(column=3, row=2, sticky=E)
ttk.Label(root, textvariable=required_income).grid(
    column=4, row=2, sticky=W)

etr = IntVar()
ttk.Label(root, text='Effective tax rate:').grid(
    column=0, row=3, columnspan=3, sticky=E)
ttk.Label(root, textvariable=etr).grid(column=4, row=3, sticky=E)
ttk.Label(root, text='%').grid(column=5, row=3, sticky=W)

ttk.Button(root, text='Calculate', command=calculate).grid(column=6, row=4)

root.mainloop()
