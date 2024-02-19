import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Gender finder")
root.geometry('300x300')

def mouse_click():
    list_box.delete(0, tk.END)

def button1_click():
    list_box.delete(0, tk.END)
    number = entry.get()
    entry.delete(0, tk.END)
    if len(number) == 10:
        if number.endswith("V") or number.endswith("X"):
            id_num = number
            first_num = int(id_num[2:5])
            if first_num > 500:
                list_box.insert(tk.END,"Female")
            else:
                list_box.insert(tk.END, "Male")
        else:
            list_box.insert(tk.END, "check ID")
    else:
        list_box.insert(tk.END, "Invalid ID")

def button2_click():
    number = entry.get()
    if len(number) == 12:
        id_num = number
        first_num = int(id_num[4:7])
        if first_num > 500:
            list_box.insert(tk.END,"Female")
        else:
            list_box.insert(tk.END,"Male")
    else:
            list_box.insert(tk.END,"Invalid ID")

frame1 = ttk.Frame(root, width=250, height=150)
frame1.pack()

entry = tk.Entry(frame1, font='arial 12', width=27, background= "#98F5FF")
entry.pack(pady=10)

button1 = ttk.Button(frame1, text="Old ID number", command=button1_click)
button1.pack()

button2 = ttk.Button(frame1, text="New ID number", command=button2_click)
button2.pack()

frame2 = ttk.Frame(root, width=250, height=150)
frame2.pack()

list_box = tk.Listbox(frame2, width=40, height=15, background="#FFD39B")
list_box.pack()

root.mainloop()