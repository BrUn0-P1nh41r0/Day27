from tkinter import *

FONT = ("Arial", 14)

def button_clicked():
    miles_get = miles_inserted.get()
    if miles_get == "" or miles_get == 0:
        miles_get = 0
    total_km = float(miles_get) * 1.609
    value_kms.config(text=int(total_km))

window = Tk()
window.title("Miles to kilometer converter")
window.minsize(width=270, height= 150)
window.config(padx=30, pady=30)

#label
miles = Label(text="Miles", font=FONT)
miles.grid(column = 3, row=0)

kms = Label(text="Km", font=FONT)
kms.grid(column = 3, row = 1)

is_equal = Label(text="is equal to", font=FONT)
is_equal.grid(column=0, row=1)

value_kms = Label(text="0", font=FONT)
value_kms.grid(column = 1, row = 1)

#button

button = Button(text="Calculate", command=button_clicked)
button.grid(column = 1, row = 2)

#Entry
miles_inserted = Entry(width=10)
miles_inserted.grid(column = 1, row = 0)



window.mainloop()
