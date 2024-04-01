from tkinter import Button, Entry, Label, Tk

window = Tk()
window.geometry("450x800")
label1 = Label(text="Caden's Number Generator",
               width=20,
               bg="white",
               fg="blue")
label1.grid(row=0, column=4)
button1 = Button(text="2", fg="white", bg="lightgrey", width=2, height=1)

button1.grid(row=2, column=1)
button2 = Button(text="4", fg="white", bg="lightgrey", width=2, height=1)

button2.grid(row=2, column=2)
button3 = Button(text="6", fg="white", bg="lightgrey", width=2, height=1)

button3.grid(row=2, column=3)
button4 = Button(text="10", fg="white", bg="lightgrey", width=2, height=1)

button4.grid(row=3, column=4)
button5 = Button(text="12", fg="white", bg="lightgrey", width=2, height=1)

button5.grid(row=2, column=5)
button6 = Button(text="20", fg="white", bg="lightgrey", width=2, height=1)

button6.grid(row=2, column=6)
button7 = Button(text="100", fg="white", bg="lightgrey", width=2, height=1)

button7.grid(row=2, column=7)
#text1 = Entry(fg="white", bg="lightgrey", width=30)

#text1.place(x=65, y=50)
#text1.insert(0, "Please enter a number")
chosenNumber = 12
label2 = Label(text=chosenNumber,
               width=6,
               height=3,
               bg="white",
               fg="blue",
               font=("arial", 30))
label2.grid(row=6, column=4)
button8 = Button(text="Generate!", width=15, height=2, bg='white', fg="blue")

button8.grid(row=7, column=4)
#needs to be at end
window.mainloop()
