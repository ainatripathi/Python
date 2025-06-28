import tkinter as tk
from tkinter import messagebox
import mysql.connector

def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="user"
        )

def insert():
    conn=connect_db()
    cursor=conn.cursor()
    sql="INSERT INTO store(name,pwd) VALUES(%s,%s)"
    val=(name_entry.get(),pwd_entry.get())
    try:
        cursor.execute(sql,val)
        conn.commit()
        messagebox.showinfo("Success","Data stored successfully!")
        clear()
        fetch()
    except Exception as e:
        messagebox.showerror("Error",str(e))
    conn.close()

def update():
    conn=connect_db()
    cursor=conn.cursor()
    sql="UPDATE store SET name=%s,pwd=%s WHERE sno=%s"
    val=(name_entry.get(),pwd_entry.get(),sno_entry.get())
    try:
        cursor.execute(sql,val)
        conn.commit()
        messagebox.showinfo("Success","Data supdated successfully!")
        clear()
        fetch()
    except Exception as e:
        messagebox.showerror("Error",str(e))
    conn.close()

def delete():
    conn=connect_db()
    cursor=conn.cursor()
    sql="DELETE FROM store WHERE sno=%s"
    val=(sno_entry.get(),)
    try:
        cursor.execute(sql,val)
        conn.commit()
        messagebox.showinfo("Success","Data deleted successfully!")
        clear()
        fetch()
    except Exception as e:
        messagebox.showerror("Error",str(e))
    conn.close()

def fetch():
    conn=connect_db()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM store")
    rows=cursor.fetchall()
    listbox.delete(0,tk.END)
    for row in rows:
        listbox.insert(tk.END,row)
    conn.close()

def select_record(event):
    selected=listbox.get(listbox.curselection())
    sno_entry.delete(0,tk.END)
    name_entry.delete(0,tk.END)
    pwd_entry.delete(0,tk.END)
    sno_entry.insert(0,selected[0])
    name_entry.insert(0,selected[1])
    pwd_entry.insert(0,selected[2])

def clear():
    sno_entry.delete(0,tk.END)
    name_entry.delete(0,tk.END)
    pwd_entry.delete(0,tk.END)

root=tk.Tk()
root.title("User Data Storage")
root.geometry("400x500")

tk.Label(root,text="S. No.").pack()
sno_entry=tk.Entry(root)
sno_entry.pack()

tk.Label(root,text="Username").pack()
name_entry=tk.Entry(root)
name_entry.pack()

tk.Label(root,text="Password").pack()
pwd_entry=tk.Entry(root,show="*")
pwd_entry.pack()

tk.Button(root,text="Enter",width=15,command=insert).pack(pady=5)
tk.Button(root,text="Update",width=15,command=update).pack(pady=5)
tk.Button(root,text="Delete",width=15,command=delete).pack(pady=5)
tk.Button(root,text="Clear",width=15,command=clear).pack(pady=5)

listbox=tk.Listbox(root,width=50)
listbox.pack(pady=10)
listbox.bind("<<ListBoxSelect>>",select_record)

fetch()

root.mainloop()
