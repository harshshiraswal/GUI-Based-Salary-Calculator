import tkinter as tk

# === Functions ===

def exit():
    window.destroy()

def clear_all():
    e1.delete(0, tk.END)
    e3.delete(0, tk.END)
    e4.delete(0, tk.END)
    e5.config(state='normal')
    e5.delete(0, tk.END)
    e5.config(state='disabled')

def compare():
    # Net Pay
    e5.config(state='normal')
    e5.delete(0, tk.END)
    e5.config(state='disabled')

    savings = int(e1.get()) + (int(e1.get()) * (int(e3.get()) / 100)) + (int(e4.get()) * 2250) + 0.27 * int(e1.get())
    e5.config(state='normal')
    e5.insert(0, savings)
    e5.config(state='disabled')

    # DA
    da = int(e3.get())
    e6.config(state='normal')
    e6.delete(0, tk.END)
    e6.insert(0, da)
    e6.config(state='disabled')

    # HRA
    hra = round(0.27 * int(e1.get()), 2)
    e7.config(state='normal')
    e7.delete(0, tk.END)
    e7.insert(0, hra)
    e7.config(state='disabled')

    # TPT
    tpt = 2556  # manipulate here
    e8.config(state='normal')
    e8.delete(0, tk.END)
    e8.insert(0, tpt)
    e8.config(state='disabled')

    # CEA
    noofkids = int(e4.get())
    cea = noofkids * 2250
    e9.config(state='normal')
    e9.delete(0, tk.END)
    e9.insert(0, cea)
    e9.config(state='disabled')

    # Newspaper
    newspaper = 0  # manipulate here
    e10.config(state='normal')
    e10.delete(0, tk.END)
    e10.insert(0, newspaper)
    e10.config(state='disabled')

    # Telephone Allowance
    telAll = 0  # manipulate here
    e11.config(state='normal')
    e11.delete(0, tk.END)
    e11.insert(0, telAll)
    e11.config(state='disabled')

    # Total Existing (Without LTC)
    totalExisting = int(e1.get()) + da + hra + tpt + cea
    e12.config(state='normal')
    e12.delete(0, tk.END)
    e12.insert(0, totalExisting)
    e12.config(state='disabled')

    # New Basic Pay
    ida = 38.3
    nbp = round(int(e1.get()) * ((100 + da) / (100 + ida)), -1)
    e13.config(state='normal')
    e13.delete(0, tk.END)
    e13.insert(0, nbp)
    e13.config(state='disabled')

    # IDA
    idavalue = round((nbp * (ida / 100)), -1)
    e14.config(state='normal')
    e14.delete(0, tk.END)
    e14.insert(0, idavalue)
    e14.config(state='disabled')

    # I HRA
    ihra = nbp * (hra / 100)
    e15.config(state='normal')
    e15.delete(0, tk.END)
    e15.insert(0, ihra)
    e15.config(state='disabled')

    # Cafeteria Allowance
    cafe = 35
    cafevalue = nbp * (cafe / 100)
    e16.config(state='normal')
    e16.delete(0, tk.END)
    e16.insert(0, cafevalue)
    e16.config(state='disabled')

    # Special Compliance Allowance
    if (tpt + cea) > cafevalue:
        sca = (tpt + cea) - cafevalue
    else:
        sca = 0
    e17.config(state='normal')
    e17.delete(0, tk.END)
    e17.insert(0, sca)
    e17.config(state='disabled')

    # Total Proposed
    totalProposed = nbp + idavalue + ihra + cafevalue + sca
    e20.config(state='normal')
    e20.delete(0, tk.END)
    e20.insert(0, totalProposed)
    e20.config(state='disabled')

# === GUI Setup ===

window = tk.Tk()
window.geometry("1000x800")
window.config(bg="Light Blue")
window.resizable(width=False, height=False)
window.title('Savings Calculator')

# === Widgets ===

l1 = tk.Label(window, text="Enter the Values", font=("Arial", 20), fg="Black", bg="White")
l2 = tk.Label(window, text="Basic Pay:", font=("Arial", 10), fg="Black", bg="White")
e1 = tk.Entry(window, font=("Arial", 11))

l3 = tk.Label(window, text="Select Pay Level", font=("Arial", 10), fg="Black", bg="White")
list_of_level = ("1st Level", "2nd Level", "3rd Level", "4th Level", "5th Level", "6th Level", "7th Level", "8th Level", "9th Level", "10th Level")
v3 = tk.StringVar()
drplist = tk.OptionMenu(window, v3, *list_of_level)
drplist.config(width=10)

l4 = tk.Label(window, text="DA Percentage:", font=("Arial", 10), fg="Black", bg="White")
e3 = tk.Entry(window, font=("Arial", 11))

l5 = tk.Label(window, text="No. of Child for CEA:", font=("Arial", 10), fg="Black", bg="White")
e4 = tk.Entry(window, font=("Arial", 11))

b1 = tk.Button(window, text="Compare!", font=("Arial", 15), command=compare)

l6 = tk.Label(window, text="Net Pay:", font=("Arial", 10), fg="Black", bg="White")
e5 = tk.Entry(window, font=("Arial", 11), state='disabled')

l7 = tk.Label(window, text="DA percentage:", font=("Arial", 10), fg="Black", bg="White")
e6 = tk.Entry(window, font=("Arial", 11), state='disabled')

l8 = tk.Label(window, text="HRA:", font=("Arial", 10), fg="Black", bg="White")
e7 = tk.Entry(window, font=("Arial", 11), state='disabled')

l9 = tk.Label(window, text="TPT:", font=("Arial", 10), fg="Black", bg="White")
e8 = tk.Entry(window, font=("Arial", 11), state='disabled')

l10 = tk.Label(window, text="CEA:", font=("Arial", 10), fg="Black", bg="White")
e9 = tk.Entry(window, font=("Arial", 11), state='disabled')

l11 = tk.Label(window, text="Newspaper:", font=("Arial", 10), fg="Black", bg="White")
e10 = tk.Entry(window, font=("Arial", 11), state='disabled')

l12 = tk.Label(window, text="Telephone allowance:", font=("Arial", 10), fg="Black", bg="White")
e11 = tk.Entry(window, font=("Arial", 11), state='disabled')

l13 = tk.Label(window, text="Total existing (Without LTC):", font=("Arial", 10), fg="Black", bg="White")
e12 = tk.Entry(window, font=("Arial", 11), state='disabled')

l14 = tk.Label(window, text="New Basic Pay:", font=("Arial", 10), fg="Black", bg="White")
e13 = tk.Entry(window, font=("Arial", 11), state='disabled')

l15 = tk.Label(window, text="IDA:", font=("Arial", 10), fg="Black", bg="White")
e14 = tk.Entry(window, font=("Arial", 11), state='disabled')

l16 = tk.Label(window, text="I HRA:", font=("Arial", 10), fg="Black", bg="White")
e15 = tk.Entry(window, font=("Arial", 11), state='disabled')

l17 = tk.Label(window, text="Cafeteria Allowance:", font=("Arial", 10), fg="Black", bg="White")
e16 = tk.Entry(window, font=("Arial", 11), state='disabled')

l18 = tk.Label(window, text="Special Comp. Allowance:", font=("Arial", 10), fg="Black", bg="White")
e17 = tk.Entry(window, font=("Arial", 11), state='disabled')

l21 = tk.Label(window, text="Total Proposed:", font=("Arial", 10), fg="Black", bg="White")
e20 = tk.Entry(window, font=("Arial", 11), state='disabled')

b2 = tk.Button(window, text="Clear Values", font=("Arial", 15), command=clear_all)
b3 = tk.Button(window, text="Exit Application", font=("Arial", 15), command=exit)

# === Placement ===

l1.place(x=150, y=20)
l2.place(x=20, y=70)
e1.place(x=220, y=70)
l3.place(x=20, y=100)
drplist.place(x=220, y=100)
l4.place(x=20, y=130)
e3.place(x=220, y=130)
l5.place(x=20, y=160)
e4.place(x=220, y=160)
b1.place(x=340, y=200)

l6.place(x=20, y=260)
e5.place(x=220, y=260)
l7.place(x=20, y=290)
e6.place(x=220, y=290)
l8.place(x=20, y=320)
e7.place(x=220, y=320)
l9.place(x=20, y=350)
e8.place(x=220, y=350)
l10.place(x=20, y=380)
e9.place(x=220, y=380)
l11.place(x=20, y=410)
e10.place(x=220, y=410)
l12.place(x=20, y=440)
e11.place(x=220, y=440)
l13.place(x=20, y=470)
e12.place(x=220, y=470)

l14.place(x=420, y=260)
e13.place(x=620, y=260)
l15.place(x=420, y=290)
e14.place(x=620, y=290)
l16.place(x=420, y=320)
e15.place(x=620, y=320)
l17.place(x=420, y=350)
e16.place(x=620, y=350)
l18.place(x=420, y=380)
e17.place(x=620, y=380)
l21.place(x=420, y=470)
e20.place(x=620, y=470)

b2.place(x=340, y=500)
b3.place(x=330, y=550)

# === Run App ===

window.mainloop()