from tkinter import *
from tkinter.tix import LabelEntry
from typing_extensions import Self
from PIL import Image, ImageTk
from tkinter import ttk

class employeeClass:
	def __init__(self,root):
		self.root=root
		self.root.geometry("1100x500+220+130")
		self.root.title("Inventory Management System || Hustler's Den")
		self.root.config(bg="white")
		self.root.focus_force()

		#============================
		# All Variables==============
		self.var_searchby=StringVar()
		self.var_searchtxt=StringVar()

		self.var_emp_id=StringVar()
		self.var_gender=StringVar()
		self.var_contact=StringVar()
		self.var_name=StringVar()
		self.var_dob=StringVar()
		self.var_doj=StringVar()
		self.var_email=StringVar()
		self.var_pass=StringVar()
		self.var_utype=StringVar()


    	#===searchFrame====
		SearchFrame=LabelFrame(self.root,text="Search Employee",font=("goudy old style",12,"bold"),bd=2,bg="white")
		SearchFrame.place(x=250,y=20,width=600,height=70)

		#===options====
		cmb_search=ttk.Combobox(SearchFrame,textvariable=self.var_searchby,values=("Select","Email","Name","Contact"),state='readonly',justify=CENTER,font=("goudy old style",15))
		cmb_search.place(x=10,y=10,width=180)
		cmb_search.current(0)

		txt_search=Entry(SearchFrame,textvariable=self.var_searchtxt,font=("goudy old style",15),bg="lightyellow").place(x=200,y=10 )
		btn_search=Button(SearchFrame,text="Search",font=("goudy old style",15),bg="#4caf50",cursor="hand2").place(x=410,y=9,width=150,height=30)

		#===title===
		title=Label(self.root,text="Employee Details",font=("goudy old style",15),bg="#0f4d7d",fg="white").place(x=50,y=100,width=1000)


		#====content==========
		lbl_empid=Label(self.root,text="Emp ID",font=("goudy old style",15),bg="white").place(x=50,y=150)
		lbl_gender=Label(self.root,text="Gender",font=("goudy old style",15),bg="white").place(x=350,y=150)
		lbl_contact=Label(self.root,text="Contact",font=("goudy old style",15),bg="white").place(x=750,y=150)

		txt_empid=Entry(self.root,textvariable=self.var_emp_id,font=("goudy old style",15),bg="white").place(x=150,y=150,width=180)
		#txt_gender=Entry(self.root,textvariable=self.var_gender,font=("goudy old style",15),bg="white").place(x=500,y=150,width=180)

		cmb_gender=ttk.Combobox(self.root,textvariable=self.var_gender,values=("Select","Male","Female","Others"),state='readonly',justify=CENTER,font=("goudy old style",15))
		cmb_gender.place(x=500,y=150,width=180)
		cmb_gender.current(0)
		
		txt_contact=Entry(self.root,textvariable=self.var_contact,font=("goudy old style",15),bg="white").place(x=850,y=150,width=180)
		

if __name__ == "__main__":
	root=Tk()
	obj=employeeClass(root)
	root.mainloop()