from tkinter import Tk, Menu
root = Tk()
#  creating menu bar
menu_bar = Menu(root)
# Creating a sub-menu
filemenu= Menu(menu_bar, tearoff=0)
# Add commands to sub-menu
filemenu.add_command(label='Stop', command=root.destroy)
filemenu.add_command(label='Exit', command=root.destroy)
filemenu.add_command(label='Kill', command=root.destroy)

menu_bar.add_cascade(label='File', menu=filemenu)
root.config(menu=menu_bar)









root.mainloop()
