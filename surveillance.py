import cv2
from tkinter import *
from PIL import Image,ImageTk
import time
import imutils
#####################################################################################################

class App:
	def __init__(self,video_source=0):
		self.appname="Criminal Face Identification System"
		self.window=Tk()
		self.window.title(self.appname)
		self.window.geometry('1250x750')
		self.window.resizable(0,0)
		#self.window.wm_iconbitmap("cam.ico")
		self.window["bg"]='lightgrey'
		self.video_source=video_source
		self.vid=myvideocapture(self.video_source)
		self.label=Label(self.window,text=self.appname,font=("bold",20),bg='blue',fg='white').pack(side=TOP,fill=BOTH)
		self.canvas=Canvas(self.window,height=700,width=550,bg='lightgrey')
		self.canvas.pack(side=LEFT,fill=BOTH)

		self.btn_snap=Button(self.window,text="SnapSHOT",width=30,bg='goldenrod2',activebackground="red",command=self.snapshot)
		self.btn_snap.pack(anchor=CENTER,expand=True)
		self.update()
		self.window.mainloop()

	def snapshot(self):
		check,frame=self.vid.getframe()
		if check:
			image="IMG-"+time.strftime("%H-%M-%S-%d-%m")+".jpg"
			cv2.imwrite(image,cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))

			msg=Label(self.window,text='image saved'+image,bg='black',fg='green').place(x=430,y=510)

	def update(self):
		isTrue,frame=self.vid.getframe()
		if isTrue:
			self.photo=ImageTk.PhotoImage(image=Image.fromarray(frame))
			self.canvas.create_image(0,0,image=self.photo,anchor=NW)

		self.window.after(15,self.update)

#####################################################################################################
class myvideocapture:
	def __init__(self,video_source=0):
		self.vid=cv2.VideoCapture(video_source)
		if not self.vid.isOpened():
			raise ValueError("unable to open",video_source)

		self.width=self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
		self.height=self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

	def getframe(self):
		if self.vid.isOpened():
			isTrue,frame=self.vid.read()
			frame=imutils.resize(frame,height=700)
			if isTrue:
				return (isTrue,cv2.cvtColor(frame,cv2.COLOR_BGR2RGB))
			else:
				return (isTrue,None)
		else:
			return (isTrue,None)

	def __del__(self):
		if self.vid.isOpened():
			self.vid.release()

if __name__=="__main__":
	App()
