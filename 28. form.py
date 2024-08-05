from tkinter import *
from tkinter import messagebox

def submit():
    nm = text1.get()
    email = text2.get()
    num = text3.get()

    a = "Welcome..." + nm.upper()
    
    messagebox.showinfo("UserInfo", a)
    lblName = Label(frameBottom, text=a, font=(14))
    lblName.grid(row=4, column=0)

    lblEmail = Label(frameBottom, text=f"Your email is {email}")
    lblEmail.grid(row=5, column=0)

    lblNum = Label(frameBottom, text=f"Your number is {num}")
    lblNum.grid(row=6, column=0)

root = Tk()
root.geometry("350x400")
root.title("DEMO FORM")

frameBottom = Frame(root)
frameBottom.pack(side="bottom", pady=80)

frameTop = Frame(root)
frameTop.pack(side="top", pady=30)

label1 = Label(frameTop, text="Name -")
label1.grid(row=0, column=0, padx=30, pady=10)

text1 = Entry(frameTop)
text1.grid(row=0, column=1)

label2 = Label(frameTop, text="Email id -")
label2.grid(row=1, column=0, padx=30, pady=10)

text2 = Entry(frameTop)
text2.grid(row=1, column=1)

label3 = Label(frameTop, text="Contact no-")
label3.grid(row=2, column=0, padx=30, pady=10)

text3 = Entry(frameTop)
text3.grid(row=2, column=1)

calcel = Button(frameTop, text="Cancel", command=root.destroy)
calcel.grid(row=3, column=0)

sub = Button(frameTop, text="Submit", command=submit)
sub.grid(row=3, column=1, padx=50, pady=20)

root.mainloop()
