import tkinter as tk
def button_click(char):
    current=entry.get()
    if char=="C":
        entry.delete(0,tk.END)
    elif char=="=":
        try:
            result=eval(current)
            entry.delete(0,tk.END)
            entry.insert(0,result)
        except Exception:
            entry.delete(0,tk.END)
            entry.insert(0,result)
    elif char=="<-":
        entry.delete(len(current)-1,tk.END)
    else:
        entry.insert(tk.END,char)

root=tk.Tk()
root.title("Calculator")

entry=tk.Entry(root,width=20,font=("Arial",20))
entry.grid(row=0,column=0,columnspan=5)
buttons=[
    "7","8","9","+",
    "4","5","6","-",
    "1","2","3","*",
    "0",".","=","/"
    ]
row,col=1,0
for button in buttons:
    tk.Button(root,text=button,padx=20,pady=20,font=("Arial",16),
              command=lambda button=button: button_click(button)).grid(row=row,column=col)
    col+=1
    if col>3:
        col=0
        row+=1

tk.Button(root,text="<-",padx=20,pady=20,font=("Arial",16),
          command=lambda:button_click("<-")).grid(row=5,column=3)

tk.Button(root,text="C",padx=20,pady=20,font=("Arial",16),
          command=lambda:button_click("C")).grid(row=5,column=2)
root.mainloop()


def print_selected_items():
    selected_index=listbox.curselection() #Get selected item's index
    if selected_index:
        selected_item=listbox.get(selected_index[0])
        result_label.config(text=f"Selected item: {selected_item}")
    else:
        result_label.config(text="No item selected")

root=tk.Tk()
root.title("Listbox Example")

listbox=tk.Listbox(root)
listbox.pack(pady=10)

items=["Java Exercises","C++ Exercises","C# Exercises","C Exercises","Python Exercises"]
for item in items:
    listbox.insert(tk.END,item)

print_button=tk.Button(root,text="Print  Selected item",command=print_selected_items)
print_button.pack()

result_label=tk.Label(root,text="")
result_label.pack()

root.mainloop()
