import tkinter as tk
from tkinter import messagebox
import database

class App(tk.Tk):
    def __init__(self):
         super().__init__()
         self.geometry("400x500")
         self.container=tk.Frame(self)
         self.container.pack(fill="both",expand=True)

         self.frames={}

         for F in (Home,SignUp,LogIn,Profile):
             frame=F(parent=container,controller=self)
             frame.grid(row=0,column=0,sticky="nsew")
             self.frames[F]=frame
        self.show_frame(Home)

    def show_frame(self, page):
        self.frames[page].tkraise()

#Home Page
class Home(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.title("Home Page")
        self.controller=controller
        tk.Label(self,text="Welcome to the Home Page",font=("Times New Roman",20)).pack(pady=10)
        tk.Button(self,text="New User? SignUp",command=lambda: controller.show_frame(SignUp)).pack(pady=5)
        tk.Button(self,text="Already have an account? LogIn",command=lambda: controller.show_frame(LogIn)).pack(pady=5)

#SignUp Page
class SignUp(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller=controller
        self.title("SignUp Page")
        tk.Label(self,text="SIGN UP!",font=("Times New Roman",20)).pack(pady=10)
        self.user=tk.Entry(self)
        self.user.pack(pady=5)
        self.user.insert(0,"Username")
        self.pwd=tk.Entry(self,show="*")
        self.pwd.pack(pady=5)
        self.pwd.insert(0,"Password")
        tk.Button(self,text="SignUp",command=self.register).pack(pady=5)
        tk.Button(self,text="LogIn",command=lambda: controller.show_frame(LogIn)).pack(pady=5)
        
    def register(self):
        uname=self.user.get().strip()
        paswd=self.pwd.get().strip()

        if not uname or not paswd:
            messagebox.showerror("Error","Please fill out all the fields!")

        conn=database.get_db()
        cursor=conn.cursor()
        try:
            sql="INSERT INTO data (username,password) VALUES(%s,%s)"
            val=(uname,paswd)
            cursor.execute(sql,val)
            conn.commit()
            messagebox.showinfo("Success","You have signed up successfully!")
            self.controller.show_frame(LogIn)
        except mysql.connector.IntegrityError:
            messagebox.showerror("Error","Username already taken!")
        finally:
            conn.close()
            
#LogIn Page
class LogIn(tk.Frame):
    def __init__(self,parent,controller):
        super().__init_(parent)
        self.controller=controller
        self.title("LogIn Page")
        tk.Label(self,text="LOG IN!",font=("Times New Roman",20)).pack(pady=10)
        self.user=tk.Entry(self)
        self.user.pack(pady=5)
        self.user.insert(0,"Username")
        self.pwd=tk.Entry(self,show="*")
        self.pwd.pack(pady=5)
        self.pwd.insert(0,"Password")
        tk.Button(self,text="LogIn",command=self.login).pack(pady=5)
        tk.Button(self,text="SignUp",command=lambda: controller.show_frame(SignUp)).pack(pady=5)

    def login(self):
        uname=self.user.get().strip()
        paswd=self.user.get().strip()

         if not uname or not paswd:
            messagebox.showerror("Error","Please fill out all the fields!")
        sql="SELECT id FROM data WHERE username=%s AND password=%s"
        val=(uname,paswd)
        cursor.execute(sql,val)
        conn.commit()
        row=cursor.fetchone()
        conn.close()
        if row:
            self.controller.user_id=row[0]
            self.controller.username=uname
            messagebox.showinfo("Success","You have logged in successfully!")
            self.controller.show_frame(Profile)
        else:
            messagebox.showerror("Error","Invalid Username or Password!")

class Profile(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller(controller)
        self.title("Profile Page")
        tk.Label(self,text="Welcome to Profile Page",font=("Times New Roman",20)).pack(pady=10)
        
