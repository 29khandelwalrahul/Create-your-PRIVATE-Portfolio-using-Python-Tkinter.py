from tkinter import *

rahul =Tk()
rahul.geometry("250x150")
rahul.title("LOGIN HERE !")

rahul.minsize(250,150)
# rahul.maxsize(250,150)

def login():
    if(Passval.get() == "rahul@123" and Userval.get() == "rahul khandelwal"):
        rahul.title("About you ")
        rahul.geometry("390x630")

        photo = PhotoImage(file="7.png")

        a = Label(image=photo)
        a.grid()

        lablel =Label(text="Hello , Rahul this side ! ",fg="red",font="Times_new_roman 20 bold")
        lablel.grid()
        rahul.mainloop()

    else:
        rahul.geometry("450x200")
        f = open("Login responses","a")
        f.write(f"Username is : {Userval.get()}\n")
        f.write(f"Password is : {Passval.get()}\n\n")
        f.close()
        label=Label(text="Your response has been submitted ",fg="black",font="Times_new_roman 15 bold").grid(column=4)
        rahul.mainloop()

def end_here():
    # if(but == 1):

    rahul.destroy()


img=Label(rahul,fg="black",text= "LOGIN HERE !! ",font="Times_new_roman 14 bold").grid(column=4)
# User=Label(rahul,fg="black",text= "Username",font="CASTELLAR 10 bold")
# Password=Label(rahul,fg="black",text="Password",font="CASTELLAR 10 bold")

User=Label(rahul,fg="black",text="Username ").grid(column=3)
Pass=Label(rahul,fg="black",text="Password  ").grid(column=3)

Userval = StringVar()
Passval = StringVar()

frame3=Frame(rahul,borderwidth=2,bg="grey",relief=SUNKEN)
frame3.grid(row=1,column=4)
Userentry = Entry(frame3,text=Userval).grid(row=1,column=4)

frame4=Frame(rahul,borderwidth=2,bg="grey",relief=SUNKEN)
frame4.grid(row=2,column=4)
Passentry = Entry(frame4,text=Passval,show="*").grid(row=2,column=4)


frame = Frame(rahul,borderwidth=4,bg="grey",relief=SUNKEN)
frame.grid(column=4)
but = Button(frame,text="SUBMIT",command=login).grid(column=4)


frame1 = Frame(rahul,borderwidth=4,bg="grey",relief=SUNKEN)
frame1.grid(column=4)
but1=Button(frame1,text="END",command=end_here).grid(column=4)

rahul.mainloop()