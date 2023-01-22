from tkinter import *
root = Tk()
root.title("MUSIC PLAYER")
root.geometry('352x255')
root.configure(bg="white")
root.resizable(width=FALSE, height=FALSE)

#frames
left_frame = Frame(root, width=150, height=150, bg="white")
left_frame.grid(row=0, column=0, padx=1, pady=1)

right_frame = Frame(root, width=220, height=150, bg="black")
right_frame.grid(row=0, column=1, padx=0)

down_frame= Frame(root, width=400,height=100, bg="brown")
down_frame.grid(row=1, column=0, columnspan=3, padx=1, pady=1)
