from tkinter import *
import time
import ttkthemes
from tkinter import ttk , messagebox, filedialog
import pymysql
import pandas as pd


#funct part
def exit_button():
   result=messagebox.askyesno('Confirm','Do you want to exit?')
   if result:
      root.destroy()
   else:
      pass   



def export_student():
   url= filedialog.asksaveasfilename(defaultextension='.csv')
   indexing=studenttable.get_children()
   newlist=[]
   for index in indexing:
      content = studenttable.item(index)
      datalist=content['values'] 
      newlist.append(datalist)
   print(newlist)      

   table=pd.DataFrame(newlist,columns=['Id','Name','Mobile','Email','Address','Gender','DOB','Added Date','Added Time'])
   table.to_csv(url,index=False)
   messagebox.showinfo('Success','Data is Saved Successfullly')

def update_student():
 def update_data():
    query = 'update student set name=%s,mobile=%s,email=%s,Address=%s,gender=%s,DOB=%s,date=%s,time=%s where id = %s'
    mycursor.execute(query,(nameEntry.get(),phoneEntry.get(),emailEntry.get(),AddressEntry.get(),genderEntry.get(),DOBEntry.get(),date,currenttime,idEntry.get()))
    con.commit()
    messagebox.showinfo('Success',f'ID {idEntry.get()} is modified successfully',parent=update_window)
    update_window.destroy()
    show_student()
 
 
 update_window = Toplevel()
 update_window.title('Update Student')
 update_window.grab_set()
 update_window.resizable(False,False)
 
 idLabel = Label(update_window,text='Id',font=('times new roman',20,'bold'))
 idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
 idEntry = Entry(update_window,font=('roman',15,'bold'),width=24)
 idEntry.grid(row=0,column=1,pady=15,padx=10)
 
 nameLabel = Label(update_window,text='Name',font=('times new roman',20,'bold'))
 nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
 nameEntry = Entry(update_window,font=('roman',15,'bold'),width=24)
 nameEntry.grid(row=1,column=1,pady=15,padx=10)
 
 phoneLabel = Label(update_window,text='Phone',font=('times new roman',20,'bold'))
 phoneLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
 phoneEntry = Entry(update_window,font=('roman',15,'bold'),width=24)
 phoneEntry.grid(row=2,column=1,pady=15,padx=10)
 
 emailLabel = Label(update_window,text='Email',font=('times new roman',20,'bold')) 
 emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
 emailEntry = Entry(update_window,font=('roman',15,'bold'),width=24)
 emailEntry.grid(row=3,column=1,pady=15,padx=10)
 
 AddressLabel = Label(update_window,text='Address',font=('times new roman',20,'bold'))
 AddressLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
 AddressEntry = Entry(update_window,font=('roman',15,'bold'),width=24)
 AddressEntry.grid(row=4,column=1,pady=15,padx=10)

 genderLabel = Label(update_window,text='Gender',font=('times new roman',20,'bold'))
 genderLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
 genderEntry = Entry(update_window,font=('roman',15,'bold'),width=24)
 genderEntry.grid(row=5,column=1,pady=15,padx=10)
 
 DOBLabel = Label(update_window,text='D O B',font=('times new roman',20,'bold'))
 DOBLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
 DOBEntry = Entry(update_window,font=('roman',15,'bold'),width=24)
 DOBEntry.grid(row=6,column=1,pady=15,padx=10)
 
 update_student_button = ttk.Button(update_window,text='UPDATE STUDENT',command=update_data)
 update_student_button.grid(row=7,columnspan=2)
 
 indexing=studenttable.focus()
 print(indexing)
 content=studenttable.item(indexing)
 listdata=content['values']
 idEntry.insert(0,listdata[0])
 nameEntry.insert(0,listdata[1])
 phoneEntry.insert(0,listdata[2])
 emailEntry.insert(0,listdata[3])
 AddressEntry.insert(0,listdata[4])
 genderEntry.insert(0,listdata[5])
 DOBEntry.insert(0,listdata[6])


 


def show_student():
 query = 'select * from student'
 mycursor.execute(query)
 fetched_data=mycursor.fetchall()
 studenttable.delete(*studenttable.get_children())
 for data in fetched_data:
   studenttable.insert('',END,values=data)


def delete_student():
 indexing=studenttable.focus()
 print(indexing)
 content = studenttable.item(indexing)
 content_id = content['values'][0]
 query='delete from student where id=%s'
 mycursor.execute(query,content_id)
 con.commit()
 messagebox.showinfo('Deleted',f'ID {content_id} is deleted successfully')
 query = 'select * from student'
 mycursor.execute(query)
 fetched_data=mycursor.fetchall()
 studenttable.delete(*studenttable.get_children())
 for data in fetched_data:
   studenttable.insert('',END,values=data)





















def search_student():
 def search_data():
    query  = 'select * from student where id =%s or name=%s or email=%s or mobile =%s or Address = %s or gender=%s or DOB=%s'
    mycursor.execute(query,(idEntry.get(),nameEntry.get(),emailEntry.get(),phoneEntry.get(),AddressEntry.get(),genderEntry.get(),DOBEntry.get()))
    studenttable.delete(*studenttable.get_children())
    fetched_data=mycursor.fetchall()
    for data in fetched_data:
      studenttable.insert('',END,values=data)






 search_window = Toplevel()
 search_window.title('Search Student')
 search_window.grab_set()
 search_window.resizable(False,False)
 
 idLabel = Label(search_window,text='Id',font=('times new roman',20,'bold'))
 idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
 idEntry = Entry(search_window,font=('roman',15,'bold'),width=24)
 idEntry.grid(row=0,column=1,pady=15,padx=10)
 
 nameLabel = Label(search_window,text='Name',font=('times new roman',20,'bold'))
 nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
 nameEntry = Entry(search_window,font=('roman',15,'bold'),width=24)
 nameEntry.grid(row=1,column=1,pady=15,padx=10)
 
 phoneLabel = Label(search_window,text='Phone',font=('times new roman',20,'bold'))
 phoneLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
 phoneEntry = Entry(search_window,font=('roman',15,'bold'),width=24)
 phoneEntry.grid(row=2,column=1,pady=15,padx=10)
 
 emailLabel = Label(search_window,text='Email',font=('times new roman',20,'bold')) 
 emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
 emailEntry = Entry(search_window,font=('roman',15,'bold'),width=24)
 emailEntry.grid(row=3,column=1,pady=15,padx=10)
 
 AddressLabel = Label(search_window,text='Address',font=('times new roman',20,'bold'))
 AddressLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
 AddressEntry = Entry(search_window,font=('roman',15,'bold'),width=24)
 AddressEntry.grid(row=4,column=1,pady=15,padx=10)

 genderLabel = Label(search_window,text='Gender',font=('times new roman',20,'bold'))
 genderLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
 genderEntry = Entry(search_window,font=('roman',15,'bold'),width=24)
 genderEntry.grid(row=5,column=1,pady=15,padx=10)
 
 DOBLabel = Label(search_window,text='D O B',font=('times new roman',20,'bold'))
 DOBLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
 DOBEntry = Entry(search_window,font=('roman',15,'bold'),width=24)
 DOBEntry.grid(row=6,column=1,pady=15,padx=10)
 
 search_student_button = ttk.Button(search_window,text='SEARCH STUDENT',command=search_data)
 search_student_button.grid(row=7,columnspan=2)










def add_student():
  def add_data():
     if idEntry.get()=='' or nameEntry.get()=='' or phoneEntry.get()=='' or emailEntry.get()=='' or AddressEntry.get()=='' or genderEntry.get()=='' or DOBEntry.get()=='':
        messagebox.showerror('Error','all Fields required',parent = addd_window)

     else:
         try: 
             query = 'insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
             mycursor.execute(query,(idEntry.get(),nameEntry.get(),phoneEntry.get(),emailEntry.get(),AddressEntry.get(),genderEntry.get(),DOBEntry.get(),date,currenttime))
             con.commit()
             result = messagebox.askyesno('Confirm','Data added successfully. Do you want to clean the form?', parent = addd_window)
             if result:
                idEntry.delete(0,END)
                nameEntry.delete(0,END)
                phoneEntry.delete(0,END)
                emailEntry.delete(0,END)  
                AddressEntry.delete(0,END)
                genderEntry.delete(0,END)
                DOBEntry.delete(0,END)
             else:
                pass
                return
         except:
             messagebox.showerror('Error','Id cannot be repeated ', parent = addd_window)

             query = 'select * from student'
             mycursor.execute(query)
             fetched_data=mycursor.fetchall()
             studenttable.delete(*studenttable.get_children())
             for data in fetched_data:
               studenttable.insert('',END,values=data)





  addd_window = Toplevel()
  addd_window.grab_set()
  addd_window.resizable(False,False)
  idLabel = Label(addd_window,text='Id',font=('times new roman',20,'bold'))
  idLabel.grid(row=0,column=0,padx=30,pady=15,sticky=W)
  idEntry = Entry(addd_window,font=('roman',15,'bold'),width=24)
  idEntry.grid(row=0,column=1,pady=15,padx=10)

  nameLabel = Label(addd_window,text='Name',font=('times new roman',20,'bold'))
  nameLabel.grid(row=1,column=0,padx=30,pady=15,sticky=W)
  nameEntry = Entry(addd_window,font=('roman',15,'bold'),width=24)
  nameEntry.grid(row=1,column=1,pady=15,padx=10)

  phoneLabel = Label(addd_window,text='Phone',font=('times new roman',20,'bold'))
  phoneLabel.grid(row=2,column=0,padx=30,pady=15,sticky=W)
  phoneEntry = Entry(addd_window,font=('roman',15,'bold'),width=24)
  phoneEntry.grid(row=2,column=1,pady=15,padx=10)

  emailLabel = Label(addd_window,text='Email',font=('times new roman',20,'bold'))
  emailLabel.grid(row=3,column=0,padx=30,pady=15,sticky=W)
  emailEntry = Entry(addd_window,font=('roman',15,'bold'),width=24)
  emailEntry.grid(row=3,column=1,pady=15,padx=10)

  AddressLabel = Label(addd_window,text='Address',font=('times new roman',20,'bold'))
  AddressLabel.grid(row=4,column=0,padx=30,pady=15,sticky=W)
  AddressEntry = Entry(addd_window,font=('roman',15,'bold'),width=24)
  AddressEntry.grid(row=4,column=1,pady=15,padx=10)

  genderLabel = Label(addd_window,text='Gender',font=('times new roman',20,'bold'))
  genderLabel.grid(row=5,column=0,padx=30,pady=15,sticky=W)
  genderEntry = Entry(addd_window,font=('roman',15,'bold'),width=24)
  genderEntry.grid(row=5,column=1,pady=15,padx=10)

  DOBLabel = Label(addd_window,text='D O B',font=('times new roman',20,'bold'))
  DOBLabel.grid(row=6,column=0,padx=30,pady=15,sticky=W)
  DOBEntry = Entry(addd_window,font=('roman',15,'bold'),width=24)
  DOBEntry.grid(row=6,column=1,pady=15,padx=10)

  add_student_button = ttk.Button(addd_window,text='ADD STUDENT',command=add_data)
  add_student_button.grid(row=7,columnspan=2)




























def connect_database():
   def connect():
      global mycursor , con
      try: 
          con  = pymysql.connect(host=hostEntry.get(),user=UserEntry.get(),passwd=passwordEntry.get())
          """con  = pymysql.connect(host=hostEntry.get(),user=UserEntry.get(),passwd=passwordEntry.get())"""
          mycursor = con.cursor()
      except:
         messagebox.showerror('Error','Invalid Details',parent = connectWindow)
         return
      try:     
          query='create database studentmanagementsystem'
          mycursor.execute(query)
          query = 'use studentmanagementsystem'
          mycursor.execute(query)
          query = 'create table  student (' \
        'id int not null primary key, ' \
        'name varchar(30), ' \
        'mobile varchar(10), ' \
        'email varchar(30), ' \
        'address varchar(100), ' \
        'gender varchar(20), ' \
        'dob varchar(20), ' \
        'date varchar(50), ' \
        'time varchar(50))'

        
        
        
        
        
          """query = 'create table student(id not null primary key, name varchar(300),mobile varchar(100),email varchar(30),address varchar(100),gender varchar(20),dob varchar(20),date varchar(50),time varchar(50))'"""
          mycursor.execute(query)
      except:
            query = 'use studentmanagementsystem'
            mycursor.execute(query)
      messagebox.showinfo('Success','DataBase Connected Successfully',parent = connectWindow)
      connectWindow.destroy()
      addstudentButton.config(state=NORMAL)
      searchstudentButton.config(state=NORMAL)
      updatestudentButton.config(state=NORMAL)
      showstudentButton.config(state=NORMAL)
      exportButton.config(state=NORMAL)
      deletestudentButton.config(state=NORMAL)



   connectWindow = Toplevel()
   connectWindow.geometry('470x280+730+230')
   connectWindow.title('DATABASE CONNECTION')
   connectWindow.resizable(0,0,)

   hostnameLabel= Label(connectWindow,text='Host name',font=('arial',20,'bold')) 
   hostnameLabel.grid(row=0,column=0,padx=20)

   hostEntry = Entry(connectWindow,font=('roman',15,'bold'),bd=2)
   hostEntry.grid(row=0,column=1,padx=30,pady=30)
   
   UsernameLabel= Label(connectWindow,text='User name',font=('arial',20,'bold')) 
   UsernameLabel.grid(row=1,column=0,padx=20)
   
   UserEntry = Entry(connectWindow,font=('roman',15,'bold'),bd=2)
   UserEntry.grid(row=1,column=1,padx=30,pady=20)
   

   PasswordLabel= Label(connectWindow,text='Password',font=('arial',20,'bold')) 
   PasswordLabel.grid(row=2,column=0,padx=20)
   
   passwordEntry = Entry(connectWindow,font=('roman',15,'bold'),bd=2)
   passwordEntry.grid(row=2,column=1,padx=30,pady=20)
   
   connectButton1 = ttk.Button(connectWindow,text='CONNECT',command=connect)
   connectButton1.grid(row=3,columnspan=2)



count=0
text=''
def slider():
   global text,count
   if count==len(s):
     count=0
     text=''
   text = text + s[count]
   sliderLabel.config(text=text)
   count = count + 1
   sliderLabel.after(300,slider)




def clock():
  global date,currenttime 
  date = time.strftime('%d/%m/%Y')
  currenttime = time.strftime('%H:%M:%S')
  datetimeLabel.config(text=f'  Date: {date}\nTime : {currenttime}')
  datetimeLabel.after(1000,clock)

#GUI part
root = ttkthemes.ThemedTk()

root.get_themes()

root.set_theme('radiance')

root.geometry('1174x680+0+0')
root.title("Student Management System")
root.resizable(0,0)

datetimeLabel=Label(root,text='hello',font=('times new roman',18,'bold'))
datetimeLabel.place(x=5,y=5)
clock()
s='Student Management System'
sliderLabel = Label(root,font=('arila',28,'italic bold'),width=30)
sliderLabel.place(x=200,y=0)
slider()

connectButton = ttk.Button(root,text="connect to Database",command=connect_database)
connectButton.place(x=980,y=0)

#Frames
leftFrame = Frame(root,)
leftFrame.place(x=50,y=80,width=300,height=600)

#logo image
logo_image = PhotoImage(file='folder (1).png')
logo_label = Label(leftFrame,image=logo_image)
logo_label.grid(row=0,column=0)

addstudentButton =ttk.Button(leftFrame,text='Add Student Details',width=25,state=DISABLED,command=add_student)
addstudentButton.grid(row=1,column=0,pady=15)

searchstudentButton =ttk.Button(leftFrame,text='Search Student Details',width=25,state=DISABLED,command=search_student)
searchstudentButton.grid(row=2,column=0,pady=15)


deletestudentButton =ttk.Button(leftFrame,text='Delete Student Details',width=25,state=DISABLED,command=delete_student)
deletestudentButton.grid(row=3,column=0,pady=15)


updatestudentButton =ttk.Button(leftFrame,text='Update Student Details',width=25,state=DISABLED,command=update_student)
updatestudentButton.grid(row=4,column=0,pady=15)


showstudentButton =ttk.Button(leftFrame,text='Show Student Details',width=25,state=DISABLED,command=show_student)
showstudentButton.grid(row=5,column=0,pady=15)


exportButton =ttk.Button(leftFrame,text='Export data',width=25,state=DISABLED,command=export_student)
exportButton.grid(row=6,column=0,pady=20)


exitButton = ttk.Button(leftFrame,text='Exit',width=25,command=exit_button)
exitButton.grid(row=7,column=0,pady=20)


#rigth frame
rightFrame = Frame(root)
rightFrame.place(x=350,y=80,width=820,height=600)

scorllBarX= Scrollbar(rightFrame,orient=HORIZONTAL)
scorllBarY= Scrollbar(rightFrame,orient=VERTICAL)

scorllBarX.pack(side=BOTTOM,fill=X)
scorllBarY.pack(side=RIGHT,fill=Y)

studenttable = ttk.Treeview(rightFrame,columns=('Id','Name','Mobile_no','Email','Address','Gender',
                                 'D.O.B','Added Date','Added Time'),
                                 xscrollcommand=scorllBarX.set,yscrollcommand=scorllBarY.set)

scorllBarX.config(command=studenttable.xview)
scorllBarY.config(command=studenttable.yview)
studenttable.pack(fill='both',expand=1)

studenttable.heading('Id',text='ID')
studenttable.heading('Name',text='NAME')
studenttable.heading('Mobile_no',text='MOBILE NO')
studenttable.heading('Email',text='EMAIL')
studenttable.heading('Address',text='ADDRESS')
studenttable.heading('Gender',text='GENDER')
studenttable.heading('D.O.B',text='D.O.B')
studenttable.heading('Added Date',text='ADDED DATE')
studenttable.heading('Added Time',text='ADDED TIME')

style=ttk.Style()

style.configure('Treeview',rowheight=40,font=('arial',12,'bold'),foreground='gray27',background='gray99',fieldbackground='lightgrey')
style.configure('Treeview.Heading',font=('arial',14,'bold'),foreground='black')





studenttable.config(show='headings')



root.mainloop()

