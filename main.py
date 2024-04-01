from random import randint
from tkinter import Button, Entry, Label, Tk

window = Tk()
window.geometry("450x800")

#making initial variable, I am assuming the start a thread button is what you wanted
#for part 3
chosenNumber = 1
randomNumber = ""


def updateLabelText():
  label2.config(text=chosenNumber)
  label3.config(text=randomNumber)


#I dont fully understand how to use the grid() method so my buttons arent exactly how I
#would have wanted them to be
def add2():
  global chosenNumber
  chosenNumber = 2
  print("2 added")


def add4():
  global chosenNumber
  chosenNumber = 4
  print("4 added")


def add6():
  global chosenNumber
  chosenNumber = 6
  print("6 added")


def add10():
  global chosenNumber
  chosenNumber = 10
  print("10 added")


def add12():
  global chosenNumber
  chosenNumber = 12
  print("12 added")


def add20():
  global chosenNumber
  chosenNumber = 20
  print("20 added")


def add100():
  global chosenNumber
  chosenNumber = 100
  print("100 added")


def generate():
  global randomNumber
  randomNumber = randint(1, chosenNumber)
  print("number generated")
  print(randomNumber)


label1 = Label(text="Caden's Number Generator",
               width=20,
               bg="white",
               fg="blue")
label1.grid(row=0, column=4)
button1 = Button(text="2",
                 fg="white",
                 bg="lightgrey",
                 width=2,
                 height=1,
                 command=lambda: (add2(), updateLabelText()))

button1.grid(row=2, column=1)

button2 = Button(text="4",
                 fg="white",
                 bg="lightgrey",
                 width=2,
                 height=1,
                 command=lambda: (add4(), updateLabelText()))

button2.grid(row=2, column=2)
button3 = Button(text="6",
                 fg="white",
                 bg="lightgrey",
                 width=2,
                 height=1,
                 command=lambda: (add6(), updateLabelText()))

button3.grid(row=2, column=3)
button4 = Button(text="10",
                 fg="white",
                 bg="lightgrey",
                 width=2,
                 height=1,
                 command=lambda: (add10(), updateLabelText()))

button4.grid(row=3, column=4)
button5 = Button(text="12",
                 fg="white",
                 bg="lightgrey",
                 width=2,
                 height=1,
                 command=lambda: (add12(), updateLabelText()))

button5.grid(row=2, column=5)
button6 = Button(text="20",
                 fg="white",
                 bg="lightgrey",
                 width=2,
                 height=1,
                 command=lambda: (add20(), updateLabelText()))

button6.grid(row=2, column=6)
button7 = Button(text="100",
                 fg="white",
                 bg="lightgrey",
                 width=2,
                 height=1,
                 command=lambda: (add100(), updateLabelText()))

button7.grid(row=2, column=7)
#text1 = Entry(fg="white", bg="lightgrey", width=30)

#text1.place(x=65, y=50)
#text1.insert(0, "Please enter a number")

label2 = Label(window,
               text=chosenNumber,
               width=6,
               height=3,
               bg="white",
               fg="blue",
               font=("arial", 30))
label2.grid(row=6, column=4)
generateButton = Button(text="Generate!",
                        width=15,
                        height=2,
                        bg='white',
                        fg="blue",
                        command=lambda: (generate(), updateLabelText()))

generateButton.grid(row=7, column=4)
label3 = Label(text=randomNumber,
               width=6,
               height=3,
               bg="white",
               fg="blue",
               font=("arial", 30))
label3.grid(row=8, column=4)

#needs to be at end
window.mainloop()
