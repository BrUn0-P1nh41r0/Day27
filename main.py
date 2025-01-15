import tkinter

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height= 300)
window.config(padx= 100, pady=200)

#label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.grid(column = 0, row=0)
my_label.config(padx=50, pady=50)

#button

button = tkinter.Button(text="Click Me", command=button_clicked)
button.grid(column=1, row=1)

button2 = tkinter.Button(text="Click me 2")
button2.grid(column = 2, row=0)

#Entry
input = tkinter.Entry(width=10)
input.grid(column = 3, row = 2)



window.mainloop()
