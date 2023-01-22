from tkinter import *
from PIL import ImageTk, Image
import os
from pygame import mixer

window = Tk()
window.title("MUSIC PLAYER")
window.geometry('352x255')
window.configure(bg="white")
window.resizable(width=0, height=0)


left_frame = Frame(window, width=150, height=150, bg="white")
left_frame.grid(row=0, column=0, padx=1, pady=1)

right_frame = Frame(window, width=220, height=150, bg="black")
right_frame.grid(row=0, column=1, padx=0)

down_frame = Frame(window, width=400, height=100, bg="blue")
down_frame.grid(row=1, column=0, columnspan=3, padx=0, pady=1)

Listbox = Listbox(right_frame, selectmode=SINGLE, font=(
    "Arial 9 bold"), width=22, bg="black", fg="white")
Listbox.grid(row=0, column=0)

w = Scrollbar(right_frame)
w.grid(row=0, column=1)

Listbox.config(yscrollcommand=w.set)
w.config(command=Listbox.yview)


img_1 = Image.open('Icons/1.png.jpg')
img_1 = img_1.resize((130, 130))
img_1 = ImageTk.PhotoImage(img_1)
app_image = Label(left_frame, height=130, image=img_1, padx=10, bg="white")
app_image.place(x=20, y=15)


def prev_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = index - 1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    Listbox.delete(0, END)

    show()
    Listbox.select_set(new_index)
    running_song['text'] = playing


img_2 = Image.open('Icons/4.png')
img_2 = img_2.resize((30, 30))
img_2 = ImageTk.PhotoImage(img_2)
prev_button = Button(down_frame, width=35, height=35, image=img_2,
                     padx=10, bg="white", font=("Ivy 10"), command=prev_music)
prev_button.place(x=10+28, y=30)


def play_music():
    running = Listbox.get(ACTIVE)
    running_song['text'] = running
    mixer.music.load(running)
    mixer.music.play()


img_3 = Image.open('Icons/1.png')
img_3 = img_3.resize((30, 30))
img_3 = ImageTk.PhotoImage(img_3)
play_button = Button(down_frame, width=35, height=35, image=img_3,
                     padx=10, bg="white", font=("Ivy 10"), command=play_music)
play_button.place(x=50+28, y=30)


def pause_music():
    mixer.music.pause()


img_4 = Image.open('Icons/3.png')
img_4 = img_4.resize((30, 30))
img_4 = ImageTk.PhotoImage(img_4)
pause_button = Button(down_frame, width=35, height=35, image=img_4,
                      padx=10, bg="white", font=("Ivy 10"), command=pause_music)
pause_button.place(x=90+28, y=30)


def resume_music():
    mixer.music.unpause()


img_5 = Image.open('Icons/6.png')
img_5 = img_5.resize((30, 30))
img_5 = ImageTk.PhotoImage(img_5)
resume_button = Button(down_frame, width=35, height=35, image=img_5,
                       padx=10, bg="white", font=("Ivy 10"), command=resume_music)
resume_button.place(x=130+28, y=30)


def Next_music():
    playing = running_song['text']
    index = songs.index(playing)
    new_index = index + 1
    playing = songs[new_index]
    mixer.music.load(playing)
    mixer.music.play()

    Listbox.delete(0, END)

    show()
    Listbox.select_set(new_index)
    running_song['text'] = playing


img_6 = Image.open('Icons/2.png')
img_6 = img_6.resize((30, 30))
img_6 = ImageTk.PhotoImage(img_6)
Next_button = Button(down_frame, width=35, height=35, image=img_6,
                     padx=10, bg="white", font=("Ivy 10"), command=Next_music)
Next_button.place(x=170+28, y=30)

Line = Label(left_frame, width=200, height=1, image=img_1, padx=10, bg="black")
Line.place(x=0, y=1)

Line = Label(left_frame, width=200, height=1, image=img_1, padx=10, bg="white")
Line.place(x=0, y=3)

running_song = Label(down_frame, text="Select a Song", font=(
    "Ivy 10"), width=44, height=1, padx=10, bg="white", fg="black", anchor=NW)
running_song.place(x=0, y=1)


os.chdir(r'C:\music player  app\Music')
songs = os.listdir()


def show():
    for i in songs:
        Listbox.insert(END, i)


show()

mixer.init()
music_state = StringVar()
music_state.set("choose one!")

window.mainloop()
