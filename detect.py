from tkinter import * 
from tkinter import ttk
import shutil
from PIL import ImageTk,Image
import sqlite3
from tkinter import filedialog
import tkinter.messagebox as tmsg
import cv2,os


if __name__ == "__main__":
   root = Tk()
   root.geometry('1300x750')
   root.minsize(1300,750)
   root.title("CFIS")
image=Image.open("images.jpg")
photo=ImageTk.PhotoImage(image)
photo_label=Label(image=photo,width=400,height=400).place(x=90,y=110)
photo_label

label_1 = Label(root, text="Select Photo to detect faces",width=50,font=("bold", 15))
label_1.place(x=30,y=60)
label_177 = Label(root, text="Double click on record to see details",width=50,font=("bold", 15))
label_177.place(x=650,y=48)

label_0 = Label(root, text="Criminal Face Identification System",width=80,font=("bold", 20),anchor=CENTER,bg="grey",fg="white")
label_0.place(x=0,y=0)
'''
def View():
    conn = sqlite3.connect("TRIAL.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM profile")
    rows = cur.fetchall()
    for row in rows:
        print(row) # it print all records in the database
        tree.insert("", tkinter.END, values=row)
    conn.close()
'''
####################################################################
###############  Get data ##########################################
cascadePath = "haarcascade_frontalface_default.xml"
faceDetect = cv2.CascadeClassifier(cascadePath)
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("recognizer\\training_data.yml")

#################################################################3##
def viewdetail(a):
   conn = sqlite3.connect("criminal.db")
   cur = conn.cursor()
   cur.execute("SELECT * FROM people where Id="+str(a))
   rows = cur.fetchall()
   print(rows)
   for row in rows:
      label_n = Label(root, text=row[1],width=20,font=("bold", 12))
      label_n.place(x=1000,y=400)
      label_f = Label(root, text=row[3],width=20,font=("bold", 12))
      label_f.place(x=1000,y=430)
      label_m = Label(root, text=row[4],width=20,font=("bold", 12))
      label_m.place(x=1000,y=460)
      label_g = Label(root, text=row[2],width=20,font=("bold", 12))
      label_g.place(x=1000,y=490)
      label_r = Label(root, text=row[5],width=20,font=("bold", 12))
      label_r.place(x=1000,y=520)
      label_bl = Label(root, text=row[6],width=20,font=("bold", 12))
      label_bl.place(x=1000,y=550)
      label_b = Label(root, text=row[7],width=20,font=("bold", 12))
      label_b.place(x=1000,y=580)
      label_n = Label(root, text=row[8],width=20,font=("bold", 12))
      label_n.place(x=1000,y=610)
      label_c = Label(root, text=row[9],width=30,font=("bold", 15),fg="red")
      label_c.place(x=930,y=640)
      #label_d = Label(root, text=row[10],width=20,font=("bold", 12))
      #label_d.place(x=1000,y=670)
      # it print all records in the database
   conn.close()
   ################################################################################
   label_name = Label(root, text="Name",width=20,font=("bold", 12))
   label_name.place(x=830,y=400)
   label_father = Label(root, text="FatherName",width=20,font=("bold", 12))
   label_father.place(x=830,y=430)
   label_mother = Label(root, text="MotherName",width=20,font=("bold", 12))
   label_mother.place(x=830,y=460)
   label_gender = Label(root, text="Gender",width=20,font=("bold", 12))
   label_gender.place(x=830,y=490)
   label_religion = Label(root, text="Religion",width=20,font=("bold", 12))
   label_religion.place(x=830,y=520)
   label_bloodgroup = Label(root, text="Blood Group",width=20,font=("bold", 12))
   label_bloodgroup.place(x=830,y=550)
   label_body = Label(root, text="BodyMark",width=20,font=("bold", 12))
   label_body.place(x=830,y=580)
   label_nat = Label(root, text="Nationality",width=20,font=("bold", 12))
   label_nat.place(x=830,y=610)
   label_crime = Label(root, text="Crime",width=23,font=("bold", 15),fg="red")
   label_crime.place(x=780,y=640)
   #############################################################################
   

   #############################################################################
   x='user.'+str(a)+".png"
   image=Image.open('images/'+x)
   photo=ImageTk.PhotoImage(image)
   photo_l=Label(image=photo,width=250,height=250).place(x=590,y=400).pack()


def mfileopen():
   cleartree()
   file1=filedialog.askopenfilename()
   print(file1)
   newPath = shutil.copy(file1, 'temp/1.png')
   image=Image.open('temp/1.png')
   photo=ImageTk.PhotoImage(image)
   photolbl=Label(image=photo,width=400,height=400).place(x=90,y=110).pack()

def cleartree():
   records=tree.get_children()
   for el in records:
      tree.delete(el)
      
def doubleclick(event):
   item=tree.selection()
   itemid=tree.item(item,"values")
   ide=itemid[0]
   ide=(int(ide))
   viewdetail(ide)
      
def View():
    cleartree()
    im =cv2.imread("temp/1.png")
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceDetect.detectMultiScale(gray, 1.2,5)
    Id, conf = recognizer.predict(gray)
    print(Id)
    conn = sqlite3.connect("criminal.db")
    cur = conn.cursor()
    cur.execute("SELECT ID,name,crime FROM people where ID="+str(Id))
    rows = cur.fetchall()
    print(conf)

    x=""
    if(conf>100):
       x="  No match!"
    elif(conf>80):
       x="  Low match!"
    elif(conf>50):
       x=" Good"
    else:
       x="  Best"
    for row in rows:
        print(row)
        # it print all records in the database
    conf=(100-float(conf))
    a="Matching "+str(conf)+"%" +x
    tree.insert("", 'end', values=row)
    tree.bind("<Double-1>",doubleclick)
    label_Match = Label(root, text=a,width=35,font=("bold", 20))
    label_Match.place(x=20,y=690)
   
    conn.close()
    
Fullname=StringVar()
father=StringVar()
var = IntVar()
c=StringVar()
d=StringVar()
var1= IntVar()
file1=""

btn=Button(text="Select photo",width=25,command=mfileopen).place(x=180,y=550)

#== showing treeview
tree= ttk.Treeview(root, column=("column1", "column2", "column3"), show='headings')
tree.heading("#1", text="Criminal-ID")
tree.heading("#2", text="NAME")
tree.heading("#3", text="CRIME")

tree.place(x=630,y=90)




b2=Button(text="View Matching Records",width=30,command=View).place(x=165,y=620)


root.mainloop()

'''def ask():
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
'''
