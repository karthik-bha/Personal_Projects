from tkinter import *
from tkinter import ttk,messagebox,filedialog
import sv_ttk
import time
import pymysql
import pandas as pd
#exit
def db_exit():
    res=messagebox.askyesno('Confirm?','Do you want to exit?')
    if res:
        root.destroy()
    else:
        pass

#export data
def export_data():
    url=filedialog.asksaveasfile(defaultextension='.csv')
    indexing=studtable.get_children()
    newlist=[]
    for index in indexing:
        content=studtable.item(index)
        datalist=content['values']
        newlist.append(datalist)

    table=pd.DataFrame(newlist,columns=['Id','Name','Ph.no','Email','Address','Gender','DOB','Added Date','Added Time'])
    table.to_csv(url,index=False)
    messagebox.showinfo('Successs','Data saved successfully')
#update student
def update_student():
    def update_data():
        currentdate=time.strftime('%d/%m/%y')
        currenttime=time.strftime('%H:%M')
        query='update student set name=%s, Ph_no=%s, Email=%s,Address=%s,Gender=%s,DOB=%s,Date=%s,Time=%s where id=%s'
        mycursor.execute(query,(nameentry.get(),Ph_noentry.get(),Emailentry.get(),Addressentry.get(),Genderentry.get(),DOBentry.get(),currenttime,currentdate,identry.get()))
        con.commit()
        messagebox.showinfo('Success',f'Record {identry.get()} updated',parent=update_win)
        update_win.destroy()
        show_student()

    update_win=Toplevel()
    update_win.grab_set()
    #For ID
    idlab=Label(update_win, text='Id',font=('Microsoft YaHei UI Light',12,'bold'),foreground='white')
    idlab.grid(row=0,column=0,sticky=W)
    identry=Entry(update_win,font=('Microsoft YaHei UI Light',12,'bold'),background='white',width=24,foreground='black')
    identry.grid(row=0,column=1,pady=15,padx=10,sticky=W)
    #For name
    namelab=Label(update_win, text='Name',font=('Microsoft YaHei UI Light',12,'bold'),foreground='white')
    namelab.grid(row=1,column=0,sticky=W)
    nameentry=Entry(update_win,font=('Microsoft YaHei UI Light',12,'bold'),background='white',width=24,foreground='black')
    nameentry.grid(row=1,column=1,pady=15,padx=10,sticky=W)
    #For Ph.no
    Ph_nolab=Label(update_win, text='Ph.no',font=('Microsoft YaHei UI Light',12,'bold'),foreground='white')
    Ph_nolab.grid(row=2,column=0,sticky=W)
    Ph_noentry=Entry(update_win,font=('Microsoft YaHei UI Light',12,'bold'),background='white',width=24,foreground='black')
    Ph_noentry.grid(row=2,column=1,pady=15,padx=10,sticky=W)
    #For email
    Emaillab=Label(update_win, text='Email',font=('Microsoft YaHei UI Light',12,'bold'),foreground='white')
    Emaillab.grid(row=3,column=0,sticky=W)
    Emailentry=Entry(update_win,font=('Microsoft YaHei UI Light',12,'bold'),background='white',width=24,foreground='black')
    Emailentry.grid(row=3,column=1,pady=15,padx=10,sticky=W)
    #For address
    Addresslab=Label(update_win, text='Address',font=('Microsoft YaHei UI Light',12,'bold'),foreground='white')
    Addresslab.grid(row=4,column=0,sticky=W)
    Addressentry=Entry(update_win,font=('Microsoft YaHei UI Light',12,'bold'),background='white',width=24,foreground='black')
    Addressentry.grid(row=4,column=1,pady=15,padx=10,sticky=W)
    #For gender
    Genderlab=Label(update_win, text='Gender',font=('Microsoft YaHei UI Light',12,'bold'),foreground='white')
    Genderlab.grid(row=5,column=0,sticky=W)
    Genderentry=Entry(update_win,font=('Microsoft YaHei UI Light',12,'bold'),background='white',width=24,foreground='black')
    Genderentry.grid(row=5,column=1,pady=15,padx=10,sticky=W)
    #For dob
    DOBlab=Label(update_win, text='DOB',font=('Microsoft YaHei UI Light',12,'bold'),foreground='white')
    DOBlab.grid(row=6,column=0,sticky=W)
    DOBentry=Entry(update_win,font=('Microsoft YaHei UI Light',12,'bold'),background='white',width=24,foreground='black')
    DOBentry.grid(row=6,column=1,pady=15,padx=10,sticky=W)
    #add student button
    usbutton=ttk.Button(update_win,text="Update Student",command=update_data)
    usbutton.grid(row=7,columnspan=2,pady=15)

    indexing=studtable.focus()
    content=studtable.item(indexing)
    ld=content['values']
    identry.insert(0,ld[0])
    nameentry.insert(0,ld[1])
    Ph_noentry.insert(0,ld[2])
    Emailentry.insert(0,ld[3])
    Addressentry.insert(0,ld[4])
    Genderentry.insert(0,ld[5])
    DOBentry.insert(0,ld[6])

#show student
def show_student():
    query='select * from student'
    mycursor.execute(query)
    f_d=mycursor.fetchall()
    studtable.delete(*studtable.get_children())
    for data in f_d:
        studtable.insert('',END, values=data)

#delte student
def delete_student():
    indexing=studtable.focus() #Higlights on selected record
    print(indexing)
    content=studtable.item(indexing) 
    content_id=content['values'][0]  #extracts ID from record
    query='delete from student where id=%s'
    mycursor.execute(query,content_id)
    con.commit()
    messagebox.showinfo('Deleted',f'ID {content_id} has been deleted successfully')
    query='select * from student'
    mycursor.execute(query)
    f_d=mycursor.fetchall()
    studtable.delete(*studtable.get_children())
    for data in f_d:
        studtable.insert('',END, values=data)

#search student
def search_student():
    def search_data():
        query='select * from student where id=%s'
        mycursor.execute(query,(identry.get()))
        studtable.delete(*studtable.get_children())
        f_d=mycursor.fetchall()
        for data in f_d:
            studtable.insert('',END,values=data)

    add_win=Toplevel()
    add_win.grab_set()
    idlab=Label(add_win, text='Id',font=('Microsoft YaHei UI Light',12,'bold'),foreground='white')
    idlab.grid(row=0,column=0)
    identry=Entry(add_win,font=('Microsoft YaHei UI Light',12,'bold'),background='white',width=24,foreground='black')
    identry.grid(row=0,column=1,pady=15,padx=10,sticky=W)
    asbutton=ttk.Button(add_win,text="Search student",command=search_data)
    asbutton.grid(row=7,columnspan=2,pady=15)

#add student
def add_student():
    def add_data():
        if identry.get()=='' or nameentry.get()=='' or Ph_noentry.get()=='' or Emailentry.get()=='' or Addressentry.get()=='' or Genderentry.get()=='' or DOBentry.get()=='':
            messagebox.showerror('Error','All fields required!',parent=add_win)
        else:
            currentdate=time.strftime('%d/%m/%y')
            currenttime=time.strftime('%H:%M')
            try:
                query='insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s) ' #takes inputs
                mycursor.execute(query,(identry.get(),nameentry.get(),Ph_noentry.get(),Emailentry.get(),Addressentry.get(),Genderentry.get(),DOBentry.get(),currenttime,currentdate))
                con.commit() #makes changes in db
                res=messagebox.askyesno('Confirm?','Data added successfully. Do you want to clean the form?',parent=add_win) #its a boolean function
                if res:
                    identry.delete(0,END)
                    nameentry.delete(0,END)
                    Ph_noentry.delete(0,END)
                    Emailentry.delete(0,END)
                    Addressentry.delete(0,END)
                    Genderentry.delete(0,END)
                    DOBentry.delete(0,END)
                else:
                    pass
            except:
                messagebox.showerror('Error','Id must be unique',parent=add_win)
                return

            query='select * from student'
            mycursor.execute(query)
            f_d=mycursor.fetchall() #mycursor can also retrieve data
            studtable.delete(*studtable.get_children())
            for data in f_d:
                dl=list(data)
                studtable.insert('',END,values=dl)

    add_win=Toplevel()
    add_win.grab_set()
    #For ID
    idlab=Label(add_win, text='Id',font=('Microsoft YaHei UI Light',12,'bold'),foreground='white')
    idlab.grid(row=0,column=0)
    identry=Entry(add_win,font=('Microsoft YaHei UI Light',12,'bold'),background='white',width=24,foreground='black')
    identry.grid(row=0,column=1,pady=15,padx=10,sticky=W)
    #For name
    namelab=Label(add_win, text='Name',font=('Microsoft YaHei UI Light',12,'bold'),foreground='white')
    namelab.grid(row=1,column=0)
    nameentry=Entry(add_win,font=('Microsoft YaHei UI Light',12,'bold'),background='white',width=24,foreground='black')
    nameentry.grid(row=1,column=1,pady=15,padx=10,sticky=W)
    #For Ph.no
    Ph_nolab=Label(add_win, text='Ph.no',font=('Microsoft YaHei UI Light',12,'bold'),foreground='white')
    Ph_nolab.grid(row=2,column=0)
    Ph_noentry=Entry(add_win,font=('Microsoft YaHei UI Light',12,'bold'),background='white',width=24,foreground='black')
    Ph_noentry.grid(row=2,column=1,pady=15,padx=10,sticky=W)
    #For email
    Emaillab=Label(add_win, text='Email',font=('Microsoft YaHei UI Light',12,'bold'),foreground='white')
    Emaillab.grid(row=3,column=0)
    Emailentry=Entry(add_win,font=('Microsoft YaHei UI Light',12,'bold'),background='white',width=24,foreground='black')
    Emailentry.grid(row=3,column=1,pady=15,padx=10,sticky=W)
    #For address
    Addresslab=Label(add_win, text='Address',font=('Microsoft YaHei UI Light',12,'bold'),foreground='white')
    Addresslab.grid(row=4,column=0)
    Addressentry=Entry(add_win,font=('Microsoft YaHei UI Light',12,'bold'),background='white',width=24,foreground='black')
    Addressentry.grid(row=4,column=1,pady=15,padx=10,sticky=W)
    #For gender
    Genderlab=Label(add_win, text='Gender',font=('Microsoft YaHei UI Light',12,'bold'),foreground='white')
    Genderlab.grid(row=5,column=0)
    Genderentry=Entry(add_win,font=('Microsoft YaHei UI Light',12,'bold'),background='white',width=24,foreground='black')
    Genderentry.grid(row=5,column=1,pady=15,padx=10,sticky=W)
    #For dob
    DOBlab=Label(add_win, text='DOB',font=('Microsoft YaHei UI Light',12,'bold'),foreground='white')
    DOBlab.grid(row=6,column=0)
    DOBentry=Entry(add_win,font=('Microsoft YaHei UI Light',12,'bold'),background='white',width=24,foreground='black')
    DOBentry.grid(row=6,column=1,pady=15,padx=10,sticky=W)
    #add student button
    asbutton=ttk.Button(add_win,text="Add Student",command=add_data)
    asbutton.grid(row=7,columnspan=2,pady=15)

#func for clock()
def clock():
    date=time.strftime('%d/%m/%y')
    c_time=time.strftime('%H:%M')
    dtlabel.config(text=f'      Date:{date}\nTime:{c_time}') #config() used for updation
    dtlabel.place(x=0,y=25)
def c_db():
    def connectt():
        global mycursor,con
        try:
            con=pymysql.connect(host=host_entry.get(),user=user_entry.get(),password=passw_entry.get()) #connects to MySQL
            mycursor=con.cursor() #helps in executing cmds
            messagebox.showinfo('Success','Connected to Database',parent=con_win)
        except:
            messagebox.showerror("Error","Invalid credentials",parent=con_win)
            return
        try:
            query='create database sdm'
            mycursor.execute(query)
            query='use sdm'
            mycursor.execute(query)
            query='create table student(id int not null primary key,name varchar(30),Ph_no varchar(10),email varchar(30),Address varchar(100),Gender varchar(20),DOB varchar(20),date varchar(50),time varchar(50))'
            mycursor.execute(query)
        except:
            query='use sdm'
            mycursor.execute(query)
        messagebox.showinfo('Success','Successful connection')
        con_win.destroy()
        b1.config(state=NORMAL)
        b2.config(state=NORMAL)
        b3.config(state=NORMAL)
        b4.config(state=NORMAL)
        b5.config(state=NORMAL)
        b6.config(state=NORMAL)


        
    con_win=Toplevel() #creates GUI window over main window
    con_win.grab_set()
    con_win.geometry('470x250+730+230')
    con_win.title('Databse connect')
    con_win.resizable(0,0)
    #host label and entry
    host_n=Label(con_win,text='Hostname',font=('Microsoft YaHei UI Light',12,'bold'))
    host_n.place(x=20,y=30)
    host_entry=Entry(con_win,font=('Microsoft YaHei UI Light',12,'bold'),bd=2,background='white',foreground='black')
    host_entry.place(x=150,y=30)
     #username label and entry
    user_n=Label(con_win,text='Username',font=('Microsoft YaHei UI Light',12,'bold'))
    user_n.place(x=20,y=90)
    user_entry=Entry(con_win,font=('Microsoft YaHei UI Light',12,'bold'),bd=2,background='white',foreground='black')
    user_entry.place(x=150,y=90)
     #host label and entry
    passw_n=Label(con_win,text='Password',font=('Microsoft YaHei UI Light',12,'bold'))
    passw_n.place(x=20,y=150)
    passw_entry=Entry(con_win,font=('Microsoft YaHei UI Light',12,'bold'),bd=2,background='white',foreground='black')
    passw_entry.place(x=150,y=150)
    #connect button
    connect=ttk.Button(con_win,text='Connect',command=connectt)
    connect.place(x=175,y=200)
root=Tk()
root.geometry('1176x680+0+0')
root.title('Student Database Management System')
root.resizable(0,0)
#creating a time and date section
dtlabel=Label(root,font=('Microsoft YaHei UI Light',11,'bold'))
dtlabel.place(x=5,y=5)
clock()
s='Student Database Management System'
sl=Label(root,text=s,font=('Microsoft YaHei UI Light',30,'bold'),fg='#57a1f8')
sl.place(x=200,y=10)
#connect button
cb=ttk.Button(root,width=20,text='Connect to Database',command=c_db) #applies sunvalley ttk
cb.pack()
cb.place(x=980,y=30)
sv_ttk.set_theme('dark')
#left frame
lf=Frame(root,bg='#1C1B1C')
lf.place(x=50,y=100,width=300,height=550)
#left frame img

li=PhotoImage(file='db.png')
ll=Label(lf,image=li)
ll.place(x=90,y=20)

#button1
b1=ttk.Button(root,width=20,text='Add record',state=DISABLED,command=add_student)
b1.place(x=80,y=250)
#button2
b2=ttk.Button(root,width=20,text='Search record',state=DISABLED,command=search_student)
b2.place(x=80,y=300)
#button3
b3=ttk.Button(root,width=20,text='Update record',state=DISABLED,command=update_student)
b3.place(x=80,y=350)
#button4
b4=ttk.Button(root,width=20,text='Delete record',state=DISABLED,command=delete_student)
b4.place(x=80,y=400)
#button5
b5=ttk.Button(root,width=20,text='Show records',state=DISABLED,command=show_student)
b5.place(x=80,y=450)
#button6
b6=ttk.Button(root,width=20,text='Export records',state=DISABLED,command=export_data)
b6.place(x=80,y=500)
#button7
b7=ttk.Button(root,width=20,text='Exit',command=db_exit)
b7.place(x=80,y=550)

#creating right frame
rf=Frame(root,bg='white')
rf.place(x=350,y=100,width=800,height=550)
#Making scrollbars to check columns 
sbx=Scrollbar(rf, orient=HORIZONTAL)
sby=Scrollbar(rf, orient=VERTICAL)

#making columns for preview
studtable=ttk.Treeview(rf, columns=('Id', 'Name','Ph.no','Email','Address','Gender','DOB','Added Date','Added Time'),xscrollcommand=sbx.set,yscrollcommand=sby.set)
sbx.config(command=studtable.xview)  #integrates scrollbarx with the preview table
sby.config(command=studtable.yview)
sbx.pack(side=BOTTOM,fill=X)              
sby.pack(side=RIGHT,fill=Y)
studtable.pack(fill=BOTH,expand=1) #fills entire frame with table frame 

#Add headers to columns 
studtable.heading('Id',text='Id')
studtable.heading('Name',text='Name')
studtable.heading('Ph.no',text='Ph.no')
studtable.heading('Email',text='Email')
studtable.heading('Address',text='Address')
studtable.heading('Gender',text='Gender')
studtable.heading('DOB',text='DOB')
studtable.heading('Added Date',text='Added Date')
studtable.heading('Added Time',text='Added Time')


studtable.config(show='headings')   #shows only headers in the column name
root.mainloop()

