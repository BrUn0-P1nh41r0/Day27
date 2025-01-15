import tkinter

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height= 300)

#label
my_label = tkinter.Label(text="I Am a Label", font=("Arial", 24, "bold"))
my_label.pack()

#button

button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()

#Entry
input = tkinter.Entry(width=10)
input.pack()



window.mainloop()
