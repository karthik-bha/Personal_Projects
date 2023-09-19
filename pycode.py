from tkinter import *
from tkinter import messagebox
from PIL import ImageTk #helps us import images
def login():        #command for sign in button
    if user.get()=='' or passw.get=='':
        messagebox.showerror('Error','Incomplete fields!')
    elif user.get()=='admin' and passw.get()=='123':
        messagebox.showinfo('Success',"Welcome")
        window.destroy()
        import pycode2
        
    else:
        messagebox.showerror('Error','Incorrect credentials')

#Tkinter object
window=Tk()  #making object of Tk() which is a widow class
window.geometry('925x500+300+200') #sets res of window
window.title('Student Database Management System')
window.configure(bg='#fff')
window.resizable(False,False)       #cant minimize if set to false
bgimage=PhotoImage(file='vitap.png')        #background image parameters

Label(window,image=bgimage,bg='white').place(x=100,y=100) 
#frame section
frame=Frame(window, width=350, height=350,bg="white")

#creates the frame for login layout
frame.place(x=480,y=70)
heading=Label(frame, text="Sign in", fg='#57a1f8',bg='white',
              font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)

#username section
user=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
Frame(frame,width=295,height=2, bg='black').place(x=25,y=107)

#password section
passw=Entry(frame,width=25,fg='black',border=0,bg="white",font=('Microsoft YaHei UI Light',11))
passw.place(x=30,y=150)
passw.insert(0,'Password')
Frame(frame,width=295,height=2, bg='black').place(x=25,y=177)

#button section
Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',border=0,command=login).place(x=35,y=204)
#end

label=Label(frame,text="Unable to login? Contact SDC at AB-1, 204",fg='black',bg='white',font=('Microsoft YaHei UI Light',9))
label.place(x=50,y=270)

label1=Label(window,text="Made by Karthik (21BCE7737) and Chetan (21BCE7252)",fg='#79B0FF',bg='white',font=('Microsoft YaHei UI Light',9))
label1.place(x=620,y=480)
window.mainloop() #keeps window open 

