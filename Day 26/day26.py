import tkinter as tk
win=tk.Tk()
win.title("Hello World!")
win.mainloop()

root=tk.Tk()
root.title("Tkinter World!")
label=tk.Label(root,text="Hello World!")
label.pack()
entry=tk.Entry(root)
entry.pack()
button=tk.Button(root,text="Click me!")
button.pack()
root.mainloop()

profile=tk.Tk()
profile.title("Tkinter World!")
label1=tk.Label(profile,text="Username")
label1.pack()
entry1=tk.Entry(profile)
entry1.pack()
label2=tk.Label(profile,text="Password")
label2.pack()
entry2=tk.Entry(profile)
entry2.pack()
button1=tk.Button(profile,text="Login")
button1.pack()
button2=tk.Button(profile,text="SignUp")
button2.pack()
profile.mainloop()

win=tk.Tk()
frame1=tk.Frame(master=win,width=200,height=200,bg="navyblue")
frame1.pack()
frame2=tk.Frame(master=win,width=100,height=100,bg="blue")
frame2.pack()
frame3=tk.Frame(master=win,width=50,height=50,bg="cyan")
frame3.pack()
win.mainloop()

win=tk.Tk()
frame1=tk.Frame(master=win,width=200,height=200,bg="navyblue")
frame1.pack(fill=tk.X)
frame2=tk.Frame(master=win,width=100,height=100,bg="blue")
frame2.pack(fill=tk.X)
frame3=tk.Frame(master=win,width=50,height=50,bg="cyan")
frame3.pack(fill=tk.X)
win.mainloop()

win=tk.Tk()
frame1=tk.Frame(master=win,width=200,height=200,bg="navyblue")
frame1.pack(fill=tk.Y)
frame2=tk.Frame(master=win,width=100,height=100,bg="blue")
frame2.pack(fill=tk.Y)
frame3=tk.Frame(master=win,width=50,height=50,bg="cyan")
frame3.pack(fill=tk.Y)
win.mainloop()

win=tk.Tk()
frame1=tk.Frame(master=win,width=200,height=200,bg="navyblue")
frame1.pack(fill=tk.BOTH)
frame2=tk.Frame(master=win,width=100,height=100,bg="blue")
frame2.pack(fill=tk.BOTH)
frame3=tk.Frame(master=win,width=50,height=50,bg="cyan")
frame3.pack(fill=tk.BOTH)
win.mainloop()

win=tk.Tk()
frame1=tk.Frame(master=win,width=200,height=200,bg="navyblue")
frame1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frame2=tk.Frame(master=win,width=100,height=100,bg="blue")
frame2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frame3=tk.Frame(master=win,width=50,height=50,bg="cyan")
frame3.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
win.mainloop()

