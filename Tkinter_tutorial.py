# learning tkinter module

'''from tkinter import Tk, Label, Message
#print(tkinter.TkVersion)

root = Tk()
#root.title("Fun with python")
#root.geometry("400*200+150+150")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
print("screen_width: ", screen_width)
print("screen_height: ", screen_height)

# Label
Label_1 = Label(root,text="Welcome to programming with tkinter", background='red')
Label_1.pack(padx=10, ipady=25)

#Message
msg = Message(root, text="Display this message...")
msg.config(font=('callibri', 24, 'italic bold underline'))
msg.pack()

Label_2 = (root, text="Hello how are you ?", background='red')
Label_3 = (root, text="Nice to meet you",  background='green')
Label_2.pack(fill=Y, padx=10, ipady=25, side=RIGHT)
Label_3.pack(fill=Y, padx=20, ipadx=35, side=left)

root.mainloop()


from tkinter import Tk, Menu
root = Tk()
root.title("Creat Menu-bar")
#  creating menu bar
menu_bar = Menu(root)

# Creating a sub-menu
filemenu_1= Menu(menu_bar, tearoff=0)
filemenu_2= Menu(menu_bar, tearoff=0)

# Add commands to sub-menu
filemenu_1.add_command(label='Stop', command=root.destroy)
filemenu_1.add_command(label='Exit', command=root.destroy)
filemenu_1.add_command(label='Kill', command=root.destroy)

filemenu_2.add_command(label='Shapes', command=root.destroy)
filemenu_2.add_command(label='styles', command=root.destroy)
filemenu_2.add_command(label='Images', command=root.destroy)
filemenu_2.add_command(label='Designs', command=root.destroy)

menu_bar.add_cascade(label='File', menu=filemenu_1)
menu_bar.add_cascade(label='Insert', menu=filemenu_2)
root.config(menu=menu_bar)
root.mainloop()

...........................................................................................................................................

from tkinter import Tk, Entry, Button, INSERT
root = Tk()

# Create an empty entry
entry = Entry(root)
entry.pack()

#Print the contents of entry box in console
def print_msg():
    print("Entry is: ",entry.get())

# Create a button when clicked will print the contents of entry box
button = Button(root, text="Print content", command=print_msg)
button.pack()
root.mainloop()
..............................................................................................................................................

#Prog to display text when label is clicked

from tkinter import Tk, Label
root = Tk()
label = Label(root, text='Message printing label...')
label.pack()
def my_call():
    print('Welcome to the world od programming')
# Bind left mouse button click on label
label.bind("<Button-1>", lambda e:my_call())
root.mainloop()

..............................................................................................................................................

# Prog to display an image

import sys
from tkinter import Tk, Label, PhotoImage
root = Tk()
img = PhotoImage(file="")
IMG = Label(root, image=img)
IMG.pack()
root.mainloop()

..............................................................................................................................................

# Prog to display a pop up message box

from tkinter import messagebox
title = "Costumer feedback"
text = "Did you like our costumer service ? "
reply = messagebox.askquestion(title, text)
if reply =="yes":
    print("Thank you very much...")
else:
    print("We regret the inconvinience. Please give us another chance...")

..............................................................................................................................................

# Program to create a top level window which will be closed when button is clicked

from tkinter import Tk, Toplevel, Button
root = Tk()
# Create new top level window
top_level_window = Toplevel()
top_level_window.title("Top level window")
#Destroy the top level window
def tlw_destroy():
    top_level_window.destroy()
closeButton = Button(root, text="Close Top Level Window", command=tlw_destroy)
closeButton.pack()
root.mainloop()

..............................................................................................................................................

# Program to put focus on the top leve window 
from tkinter import Tk, Toplevel
root = Tk()
top_level_window = Toplevel()
top_level_window.title("TLW")
# Focus on Top level window
top_level_window.focus_force()
root.mainloop()

..............................................................................................................................................'''

# Prog to draw colored shapes on canvas
from tkinter import Tk, Canvas 
root = Tk()
canvas = Canvas(root, width=250, height=200)
canvas.pack()
# Draw orange dashed line
canvas.create_line(0,0,250,200, fill='orange', dash=(5, 15))
# Draw yellow rectange at (100,150) to (150,60)
canvas.create_rectangle(100, 150, 150, 60, fill='yellow')
# Draw green oval from (30, 30) to (50,50)
canvas.create_oval(30, 30, 50, 50, fill='green')
root.mainloop()












































































