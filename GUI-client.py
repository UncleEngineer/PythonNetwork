from tkinter import *
from tkinter import ttk # theme of Tk
from tkinter import simpledialog 

GUI = Tk()
GUI.geometry('800x400')
GUI.title('โปรแกรมส่งข้อความไปหา Server')

v_username = StringVar()
v_username.set('--Username--')
Luser = Label(GUI, textvariable=v_username,font=(None,18))
Luser.place(x=650,y=10)

# ช่องกรอกข้อความ #Entry
v_message = StringVar()
E1 = ttk.Entry(GUI,textvariable=v_message ,width=30 ,font=(None,20))
E1.pack(pady=30)

# ถาม username
text = simpledialog.askstring('ชื่อผู้ใช้งาน','กรุณากรอกชื่อผู้ใช้งาน')
print(text)
v_username.set(text)

GUI.mainloop()