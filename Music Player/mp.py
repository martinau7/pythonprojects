from tkinter import *
from tkinter import filedialog

import pygame

root = Tk()
root.title("Martin's Music Player")
root.geometry("500x300")

pygame.mixer.init()


def add_song():
    songs = filedialog.askopenfilenames(title="Choose a song",
                                       filetypes=(("mp3 files", "*.mp3"),))
    for song in songs:
        song_box.insert(END, song)


def play():
    song = song_box.get(ACTIVE)

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)


def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)


global paused
paused = False


def pause(is_paused):
    global paused
    paused = is_paused

    if paused:
        pygame.mixer.music.unpause()
        paused = False
    else:
        pygame.mixer.music.pause()
        paused = True


def next_song():
    next_one = song_box.curselection()
    next_one = next_one[0] + 1
    song = song_box.get(next_one)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_box.selection_clear(0, END)
    song_box.activate(next_one)
    song_box.selection_set(next_one, last=None)


def prev_song():
    prev_one = song_box.curselection()
    prev_one = prev_one[0] - 1
    song = song_box.get(prev_one)
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_box.selection_clear(0, END)
    song_box.activate(prev_one)
    song_box.selection_set(prev_one, last=None)


song_box = Listbox(root, bg="black", fg="green", width=60, selectbackground="grey", selectforeground="black")
song_box.pack(pady=20)

prev_bi = PhotoImage(file="prev.png")
next_bi = PhotoImage(file="next.png")
play_bi = PhotoImage(file="play.png")
pause_bi = PhotoImage(file="pause.png")
stop_bi = PhotoImage(file="stop.png")

controls = Frame(root)
controls.pack()

prev_b = Button(controls, image=prev_bi, borderwidth=0, command=prev_song)
next_b = Button(controls, image=next_bi, borderwidth=0, command=next_song)
play_b = Button(controls, image=play_bi, borderwidth=0, command=play)
pause_b = Button(controls, image=pause_bi, borderwidth=0, command=lambda: pause(paused))
stop_b = Button(controls, image=stop_bi, borderwidth=0, command=stop)

prev_b.grid(row=0, column=0, padx=10)
next_b.grid(row=0, column=4, padx=10)
play_b.grid(row=0, column=2, padx=10)
pause_b.grid(row=0, column=3, padx=10)
stop_b.grid(row=0, column=1, padx=10)

menu = Menu(root)
root.config(menu=menu)

add_song_menu = Menu(menu)
menu.add_cascade(label="Add Songs", menu=add_song_menu, underline=0)
add_song_menu.add_command(label="Add songs to playlist", command=add_song)

root.mainloop()
