import tkinter as tk
from tkinter import messagebox
import database

class App(tk.Tk):
    def __init__(self):
         super().__init__()
         self.geometry("400x500")
         self.container=tk.Frame(self)
         self.title("Home Page")
         self.container.pack(fill="both",expand=True)

         self.frames={}

         for F in (Home,SignUp,LogIn,Profile):
             frame=F(parent=self.container,controller=self)
             frame.grid(row=0,column=0,sticky="nsew")
             self.frames[F]=frame
         self.show_frame(Home)

    def show_frame(self, page):
        self.frames[page].tkraise()

#Home Page
class Home(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller=controller
        tk.Label(self,text="Welcome to the Home Page!",font=("Times New Roman",20)).pack(pady=10)
        tk.Button(self,text="New User? SignUp",command=lambda: controller.show_frame(SignUp)).pack(pady=5)
        tk.Button(self,text="Already have an account? LogIn",command=lambda: controller.show_frame(LogIn)).pack(pady=5)

#SignUp Page
class SignUp(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller=controller
        #self.title("SignUp Page")
        tk.Label(self,text="SIGN UP!",font=("Times New Roman",20)).pack(pady=10)
        tk.Label(self,text="Username",font=("Times New Roman",12)).pack(pady=5)
        self.user=tk.Entry(self)
        self.user.pack(pady=5)
        tk.Label(self,text="Password",font=("Times New Roman",12)).pack(pady=5)
        self.pwd=tk.Entry(self,show="*")
        self.pwd.pack(pady=5)
        tk.Button(self,text="SignUp",command=self.register).pack(pady=5)
        tk.Button(self,text="LogIn",command=lambda: controller.show_frame(LogIn)).pack(pady=5)

    def clear(self):
        self.user.delete(0,tk.END)
        self.pwd.delete(0,tk.END)
        
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
        except database.mysql.connector.IntegrityError:
            messagebox.showerror("Error","Username already taken!")
        finally:
            self.clear()
            conn.close()
            
#LogIn Page
class LogIn(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller=controller
       # self.title("LogIn Page")
        tk.Label(self,text="LOG IN!",font=("Times New Roman",20)).pack(pady=10)
        self.user=tk.Entry(self)
        self.user.pack(pady=5)
        self.pwd=tk.Entry(self,show="*")
        self.pwd.pack(pady=5)
        tk.Button(self,text="LogIn",command=self.login).pack(pady=5)
        tk.Button(self,text="SignUp",command=lambda: controller.show_frame(SignUp)).pack(pady=5)

    def clear(self):
        self.user.delete(0,tk.END)
        self.pwd.delete(0,tk.END)
    def login(self):
        uname=self.user.get().strip()
        paswd=self.pwd.get().strip()
        if not uname or not paswd:
            messagebox.showerror("Error","Please fill out all the fields!")
        conn=database.get_db()
        cursor=conn.cursor()
        sql="SELECT id FROM data WHERE username=%s AND password=%s"
        val=(uname,paswd)
        cursor.execute(sql,val)
        row=cursor.fetchone()
        conn.close()
        if row:
            self.controller.user_id=row[0]
            self.controller.username=uname
            messagebox.showinfo("Success","You have logged in successfully!")
            self.controller.show_frame(Profile)
            self.clear()
        else:
            messagebox.showerror("Error","Invalid Username or Password!")

class Profile(tk.Frame):
    def __init__(self,parent,controller):
        super().__init__(parent)
        self.controller=controller
        #self.title("Profile Page")
        self.lbl=tk.Label(self,text="Welcome to Profile Page",font=("Times New Roman",20))
        self.lbl.pack(pady=10)
        tk.Button(self,text="Log Out",command=self.logout).pack()
        tk.Button(self,text="Update Username",command=self.update_user).pack()
    def logout(self):
        messagebox.showinfo("Logged out successfully","Have a good day!")
        self.controller.show_frame(Home)
    def update_user(self):
        win=tk.TopLevel(self)
        win.title("Update Username")
        win.geometry(300x150)
        tk.Label(win,text="New Username",font=("Times New Roman",12)).pack(pady=5)
        self.new_user=tk.Entry(win)
        self.new_user.pack(pady=5)
        if not new_user:
            messagebox.showerror("Error","Username cannot be empty.")
            return
        conn=database.get_db()
        cursor=conn.cursor()
        cursor.execute("UPDATE data SET username=%s WHERE id=%s",(new_user,id))
    def tkraise(self,*args,**kwargs):
        user=getattr(self.controller,"username","")
        self.lbl.config(text=f"Welcome {user}!")
        super().tkraise(*args,**kwargs)

if __name__=="__main__":
    app=App()
    app.mainloop()
