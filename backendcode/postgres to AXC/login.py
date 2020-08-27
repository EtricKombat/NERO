from tkinter import* 
from tkinter import messagebox
from PIL import ImageTk
import constants as c

class login_System():
	def __init__ (self):
		self.root = Tk()
		self.root.title("Welcome to Allripe XC") 
		self.root.iconbitmap("imagenes/favicon.ico")
		self.root.geometry("800x439+0+0")
		self.root.resizable(0,0)

		#all images
		self.bgIcon=ImageTk.PhotoImage(file="imagenes/background.jpg")
		self.userIcon=ImageTk.PhotoImage(file= "imagenes/user3.png")
		self.PasswordIcon=ImageTk.PhotoImage(file="imagenes/password.png") 
		self.Logo=ImageTk.PhotoImage(file="imagenes/Logo.png") 
		#variables
		self.userName = StringVar()
		self.passwordUser = StringVar()

		background = Label(self.root, image=self.bgIcon).pack()

		labelTitle=Label(self.root, text="Login System", font=("Calibri",25,"bold"),bg="white")
		labelTitle.place(x=0,y=0,relwidth=1)

		Login_Frame = Frame(self.root,bg="white")
		Login_Frame.place(x=215,y=120)
		#Login_Frame.wm_attributes("-alpha",0)
		
		labelLogo = Label(Login_Frame, image=self.Logo,bg="white")
		labelLogo.grid(row=0,columnspan=2, pady = 10)

		labelIconUser = Label(Login_Frame, text= " UserName", image=self.userIcon, compound = LEFT,font=("Calibri",15,"bold"),bg="white")
		labelIconUser.grid(row=1,column=0, sticky="e",padx=20)

		TxtUser=Entry(Login_Frame, text="User Name",bd=5, textvariable = self.userName ,relief=GROOVE,font=("",10))
		TxtUser.grid(row=1,column=1,padx=20) 

		labelPass=Label(Login_Frame, text= " Password", image=self.PasswordIcon, compound = LEFT,font=("Calibri",15,"bold"),bg="white")
		labelPass.grid(row=2,column=0, sticky="e",padx=20)

		TxtPass=Entry(Login_Frame, text="password", bd=5, textvariable = self.passwordUser , relief=GROOVE, font=("",10))
		TxtPass.grid(row=2,column=1,padx=20)
		TxtPass.config(show="*")

		loginButton = Button(Login_Frame, command=self.RegisterUser, text = "New User",width = 15, font=("Calibri",12,"bold"),bg="white")
		loginButton.grid(row=3,column=0, sticky="e",padx=20,pady = 5)

		loginButton = Button(Login_Frame, command=self.login, text = "Login",width = 15, font=("Calibri",12,"bold"),bg="white")
		loginButton.grid(row=3,column=1, sticky="e",padx=20,pady = 5)
		
		self.root.mainloop()

	def login(self):
		if self.userName.get()!="" and self.passwordUser.get() != "":
			try:
				if c.UserDict[self.userName.get()][1] == self.passwordUser.get():
					messagebox.showinfo ("Wellcome","Welcome "+c.UserDict[self.userName.get()][0])
					c.access = True
					c.usuario = self.userName.get()
					self.root.destroy()
			except:
				messagebox.showwarning("Warning","The user or password are incorrect ")
		else:
			messagebox.showerror("Error","All fields are required!!")

	def RegisterUser(self):
		
		self.root.destroy()


	
 