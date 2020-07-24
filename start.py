from tkinter import *
import shutil
from PIL import ImageTk,Image
import sqlite3
from tkinter import filedialog
import tkinter.messagebox as tmsg
from subprocess import call


def register():
    call(["python", "registerGUI.py"])
def VideoSurveillance():
    call(["python", "surveillance.py"])
def detectCriminal():
    call(["python", "detect.py"])


root = Tk()
root.geometry('800x500')
root.minsize(800,500)
root.maxsize(800,500)

root.title("CFIS- Criminal Face Identification System")
root.configure(bg="#069110151")



Fullname=StringVar()
father=StringVar()
var = IntVar()
c=StringVar()
d=StringVar()
var1= IntVar()
file1=""
image=Image.open("image.jpg")
photo=ImageTk.PhotoImage(image)
photo_label=Label(image=photo,width=800,height=0,bg='white').place(x=0,y=0)
photo_label

label_0 = Label(root, text="Criminal Face Identification System",width=50,font=("bold", 20),anchor=CENTER,bg="#386184",fg="white")
label_0.place(x=0,y=100)

Button(root, text='REGISTER CRIMINAL',width=35,height=3,bg='#096084050',fg='white',font=("bold", 11),command=register).place(x=250,y=180)
Button(root, text='PHOTO MATCH',width=35,height=3,bg='#096084050',fg='white',font=("bold", 11),command=detectCriminal).place(x=250,y=260)
Button(root, text='VIDEO SURVEILLANCE',width=35,height=3,bg='#096084050',fg='white',font=("bold", 11),command=VideoSurveillance).place(x=250,y=340)






'''   
def ask():
   tmsg.askquestion("CFIS WARNING !","First create dataset for better surveillance. \n Click on >>create dataset<< button before registering.\n If done, then proceed. \n\n Will you like to proceed ?")
def database():
   name1=Fullname.get()
   email=father.get()
   gender=var.get()
   if(gender==1):
      gen='Male'
   if(gender==2):
      gen='Female'
   country=c.get()
   prog=var1.get()
   conn = sqlite3.connect('Form.db')
   with conn:
      cursor=conn.cursor()
   cursor.execute('CREATE TABLE IF NOT EXISTS Student (Fullname TEXT,Email TEXT,Gender TEXT,country TEXT,Programming TEXT)')
   cursor.execute('INSERT INTO Student (FullName,Email,Gender,country,Programming) VALUES(?,?,?,?,?)',(name1,email,gender,country,prog,))
   conn.commit()

def mfileopen():
   file1=filedialog.askopenfilename()
   print(file1)
   newPath = shutil.copy(file1, 'temp/1.png')
   image=Image.open('temp/1.png')
   photo=ImageTk.PhotoImage(image)
   photo_label=Label(image=photo,width=500,height=500).place(x=640,y=140).pack()
   #label_ = Label(root, text=file1,width=70,font=("bold", 8))
   #label_.place(x=260,y=630)
   
label_10 = Label(root, text="Criminal Face Identification System",width=80,font=("bold", 20),anchor=CENTER,bg="grey",fg="white")
label_10.place(x=0,y=0)

             
label_0 = Label(root, text="Registration Form",width=90,font=("bold", 16),bg="yellow")
label_0.place(x=70,y=42)

##################  form begin  ######################

label_1 = Label(root, text="Name    *",width=20,font=("bold", 12))
label_1.place(x=70,y=130)

entry_1 = Entry(root,width=50,textvar=Fullname)
entry_1.place(x=260,y=130)

label_2 = Label(root, text="Father Name",width=20,font=("bold", 12))
label_2.place(x=70,y=180)

entry_2 = Entry(root,width=50,textvar=father)
entry_2.place(x=260,y=180)

label_3 = Label(root, text="Gender      *",width=20,font=("bold", 12))
label_3.place(x=70,y=280)

Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=260,y=280)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=315,y=280)

label_4 = Label(root, text="Mother Name",width=20,font=("bold", 12))
label_4.place(x=70,y=230)
entry_5 = Entry(root,width=50,textvar=Fullname)
entry_5.place(x=260,y=230)

##############

label_4 = Label(root, text="Religion",width=20,font=("bold", 12))
label_4.place(x=70,y=330)
list1 = ['Hindu','Muslim','Buddhist','Christian','Sikh','Jain','Others'];

droplist=OptionMenu(root,c, *list1)
droplist.config(width=30)
c.set('Select Religion') 
droplist.place(x=260,y=325)


##########

label_5 = Label(root, text="Blood Group",width=20,font=("bold", 12))
label_5.place(x=70,y=380)

list2 = ['A+','A-','B+','B-','AB+','AB-','O+','O-'];

droplist=OptionMenu(root,d, *list2)
droplist.config(width=30)
d.set('Select Blood Group') 
droplist.place(x=260,y=380)

label_6 = Label(root, text="Body Mark",width=20,font=("bold", 12))
label_6.place(x=70,y=430)

entry_6 = Entry(root,width=50,textvar=Fullname)
entry_6.place(x=260,y=430)

label_7 = Label(root, text="Nationality",width=20,font=("bold", 12))
label_7.place(x=70,y=480)

entry_7 = Entry(root,width=50,textvar=Fullname)
entry_7.place(x=260,y=480)

label_8= Label(root, text="Crime convicted        *",width=20,font=("bold", 12))
label_8.place(x=70,y=530)

entry_8 = Entry(root,width=50,textvar=Fullname)
entry_8.place(x=260,y=530)

label_9 = Label(root, text="DOB (dd/mm/yyyy)",width=20,font=("bold", 12))
label_9.place(x=70,y=580)

entry_9 = Entry(root,width=50,textvar=Fullname)
entry_9.place(x=260,y=580)

label_9 = Label(root, text="Face Image    *",width=20,font=("bold", 12))
label_9.place(x=70,y=620)

btn=Button(text="Select",width=20,command=mfileopen).place(x=260,y=620)
Button(root, text='Create dataset',width=15,bg='green',fg='white',command=ask).place(x=150,y=670)
Button(root, text='Register',width=10,bg='brown',fg='white',command=ask).place(x=300,y=670)

root.mainloop()
'''
