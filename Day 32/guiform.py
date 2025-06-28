import tkinter as tk
from tkinter import messagebox
import mysql.connector

#MySQL Databse connector function
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="guiform"
        )

#Insert student
def insert():
    conn=connect_db()
    cursor=conn.cursor()
    sql="INSERT INTO students (name,marks) VALUES (%s,%s)"
    values=(name_entry.get(),marks_entry.get())
    try:
        cursor.execute(sql,values)
        conn.commit()
        messagebox.showinfo("Success","Record inserted!")
        clear()
        fetch()
    except Exception as e:
        messagebox.showerror("Error",str(e))
    conn.close()

#Fetch all students
def fetch():
    conn=connect_db()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM students")
    rows=cursor.fetchall()
    listbox.delete(0,tk.END)
    for row in rows:
        listbox.insert(tk.END,row)
    conn.close()

#Select a record
def select_record(event):
    selected=listbox.get(listbox.curselection())
    id_entry.delete(0,tk.END)
    name_entry.delete(0,tk.END)
    marks_entry.delete(0,tk.END)
    id_entry.insert(0,selected[0])
    name_entry.insert(0,selected[1])
    marks_entry.insert(0,selected[2])

#Update a student
def update():
    conn=connect_db()
    cursor=conn.cursor()
    sql="UPDATE students SET name=%s,marks=%s WHERE id=%s"
    values=(name_entry.get(),marks_entry.get(),id_entry.get())
    try:
        cursor.execute(sql,values)
        conn.commit()
        messagebox.showinfo("Sucess","Record updated!")
        clear()
        fetch()
    except Exception as e:
        messagebox.showerror("Error",str(e))
    conn.close()

#Delete student
def delete():
    conn=connect_db()
    cursor=conn.cursor()
    sql="DELETE FROM students WHERE id=%s"
    val=(id_entry.get(),)
    try:
        cursor.execute(sql,val)
        conn.commit()
        messagebox.showinfo("Success","Record deleted!")
        clear()
        fetch()
    except Exception as e:
        messagebox.showerror("Error",str(e))
    conn.close()

#Clear fields
def clear():
    id_entry.delete(0,tk.END)
    name_entry.delete(0,tk.END)
    marks_entry.delete(0,tk.END)

#--------------------------------Tkinter GUI---------------------------#
root=tk.Tk()
root.title("Student Management System")
root.geometry("400x500")

#Labels and Entries
tk.Label(root,text="ID").pack()
id_entry=tk.Entry(root)
id_entry.pack()

tk.Label(root,text="Name").pack()
name_entry=tk.Entry(root)
name_entry.pack()

tk.Label(root,text="Marks").pack()
marks_entry=tk.Entry(root)
marks_entry.pack()


#Buttons
tk.Button(root,text="Insert",width=15,command=insert).pack(pady=5)
tk.Button(root,text="Update",width=15,command=update).pack(pady=5)
tk.Button(root,text="Delete",width=15,command=delete).pack(pady=5)
tk.Button(root,text="Clear",width=15,command=clear).pack(pady=5)

#Listbox to display data
listbox=tk.Listbox(root,width=50)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>",select_record)

#Fetch records when app starts
fetch()

root.mainloop()
