from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image,ImageTk
import pymysql
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Registration Window")
        self.root.geometry("1550x800+0+0")
        self.root.config(bg="white")
 #=======IMAGES===========
        self.bg=ImageTk.PhotoImage(file="image/b2.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)


 #====LEft Image======
        self.left=ImageTk.PhotoImage(file="image/side.png")
        left=Label(self.root,image=self.left).place(x=80,y=140,width=392,height=500)       

#========Register Frame===============
        frame1=Frame(self.root,bg="white")
        frame1.place(x=470,y=140,width=900,height=500)


        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="navy blue").place(x=50,y=30)
#---------------------------------ROW 1-----------------------------------------
        
        f_name=Label(frame1,text="First Name",font=("times new roman",15,"bold"),bg="white",fg="#9370db").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="#eeedf1")
        self.txt_fname.place(x=50,y=130,width=250)

        l_name=Label(frame1,text="Last Name",font=("times new roman",15,"bold"),bg="white",fg="#9370db").place(x=570,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="#eeedf1")
        self.txt_lname.place(x=570,y=130,width=250)
           
#---------------------------------ROW 2-----------------------------------

        contact=Label(frame1,text="Contact No.",font=("times new roman",15,"bold"),bg="white",fg="#9370db").place(x=50,y=170)
        self.txt_contact=Entry(frame1,font=("times new roman",15),bg="#eeedf1")
        self.txt_contact.place(x=50,y=200,width=250)

        email=Label(frame1,text="Email",font=("times new roman",15,"bold"),bg="white",fg="#9370db").place(x=570,y=170)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="#eeedf1")
        self.txt_email.place(x=570,y=200,width=250)

#-----------------------ROW 3-------------------------------    
        question=Label(frame1,text="Security Question",font=("times new roman",15,"bold"),bg="white",fg="#9370db").place(x=50,y=240)
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify=CENTER)
        self.cmb_quest['values']=("Select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50,y=270,width=250)
        self.cmb_quest.current(0)

        answer=Label(frame1,text="Answer",font=("times new roman",15,"bold"),bg="white",fg="#9370db").place(x=570,y=240)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="#eeedf1")
        self.txt_answer.place(x=570,y=270,width=250)

#-----------------------ROW 4-------------------------
        password=Label(frame1,text="Password",font=("times new roman",15,"bold"),bg="white",fg="#9370db").place(x=50,y=310)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="#eeedf1")
        self.txt_password.place(x=50,y=340,width=250)

        cpasword=Label(frame1,text="Confirm Password",font=("times new roman",15,"bold"),bg="white",fg="#9370db").place(x=570,y=310)
        self.txt_cpassword=Entry(frame1,font=("times new roman",15),bg="#eeedf1")
        self.txt_cpassword.place(x=570,y=340,width=250)

#------------------TERMS AND CONDITIONS-----------------------
        self.var_chk=IntVar()

        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,bg="white",font=("times new roman",12),onvalue=1,offvalue=0).place(x=50,y=380)
        
        self.btn_img=ImageTk.PhotoImage(file="image/Hnet.com-image (1).png")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor="hand2",command=self.register_data).place(x=50,y=420)
        btn_login=Button(self.root,text="Sign In",font=("times new roman",20),bd=0,bg="#d9d7f9",cursor="hand2",command=self.login_window).place(x=180,y=610,width=180)
    
#==========================================================================================================================
    def clear(self):
            self.txt_fname.delete(0,END)
            self.txt_lname.delete(0,END)
            self.txt_contact.delete(0,END)
            self.txt_email.delete(0,END)
            self.txt_answer.delete(0,END)
            self.txt_password.delete(0,END)
            self.txt_cpassword.delete(0,END)
            self.cmb_quest.current(0)
            
#===================SignIn function=============================

    def login_window(self):
            self.root.destroy()
            import login 




    def register_data(self):
            if(self.txt_fname.get()=="" or self.txt_email.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_cpassword.get()=="" or self.txt_contact.get()==""):
                messagebox.showerror("Error","All fields are Required",parent=self.root)
            elif self.txt_cpassword.get()!=self.txt_password.get():
                    messagebox.showerror("Error","Password & Confirm Password should be same",parent=self.root)
            elif self.var_chk.get()==0:
                    messagebox.showerror("Error","Please Agree our terms & Conditions",parent=self.root)        
            else:
                try:
                        con=pymysql.connect(host="localhost",user="root",password="",database="rhythm")
                        cur=con.cursor()
                        cur.execute("Select * from registered where email=%s",self.txt_email.get())
                        row=cur.fetchone()
                        if row!=None:
                                messagebox.showerror("Error","User Already exit ,Please try with another email",parent=self.root)
                        else:        
                         cur.execute("insert into registered (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                                     (self.txt_fname.get(),
                                     self.txt_lname.get(),
                                     self.txt_contact.get(),
                                     self.txt_email.get(),
                                     self.cmb_quest.get(),
                                     self.txt_answer.get(),
                                     self.txt_password.get()
                                     ))
                         con.commit()
                         con.close() 
                         messagebox.showinfo("Success","Register Successful")
                         self.clear()

                except Exception as es:
                        messagebox.showerror("Error",f"Error due to: {str(es)}",parent=self.root)        
            







root=Tk()
obj=Register(root)
root.mainloop()