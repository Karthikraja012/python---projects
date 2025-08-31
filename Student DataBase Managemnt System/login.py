from tkinter import *
from tkinter import messagebox
from  PIL import ImageTk


def login():
    if usernameEntry.get()=='' or passwordEntry.get()=='':
       messagebox.showerror('Error','Fields cannot be empty')
    elif usernameEntry.get()=='student' and passwordEntry.get()=='12345':
        messagebox.showinfo('Success','Welcome..!')
        window.destroy()
        import sms
    else:
        messagebox.showerror('Error','Please enter correct correct credentials')


window = Tk()

window.geometry("1280x700+0+0")
window.title('Login System Of Student Management System')
window.resizable(False,False)

backgroundImage = ImageTk.PhotoImage(file='bg.jpg')

bgLabel= Label(window,image=backgroundImage)
bgLabel.place(x=0,y=0)

loginFrame = Frame(window,bg='white')

loginFrame.place(x=400,y=150)

logoImage = PhotoImage(file="graduated.png")

logolabel = Label(loginFrame,image=logoImage)
logolabel.grid(row=0,column=0,columnspan=2,pady=10)


usernameLabel = Label(loginFrame,text='Username',compound='left',font=('times new roman',20,'bold'),bg='white')
usernameLabel.grid(row=1,column=0,pady=10,padx=20)

usernameEntry = Entry(loginFrame,font=('times new roman',20,'bold'),bd=5)
usernameEntry.grid(row=1,column=1,pady=10,padx=20)

#password
logolabel = Label(loginFrame,image=logoImage)
logolabel.grid(row=0,column=0,columnspan=2,pady=10)


passwordLabel = Label(loginFrame,text='Password',compound='left',font=('times new roman',20,'bold'),bg='white')
passwordLabel.grid(row=2,column=0,pady=10,padx=20)

passwordEntry = Entry(loginFrame,font=('times new roman',20,'bold'),bd=5)
passwordEntry.grid(row=2,column=1,pady=10,padx=20)

loginButton = Button(loginFrame, text='Login',font=('times new roman',14,'bold'),width=8,fg='white',bg='cornflowerblue',cursor='hand2',command=login)
loginButton.grid(row=3,column=1)







window.mainloop()