# find_track.py

import tkinter as tk
from tkinter import messagebox

def find_track_gui(library):
    find_window = tk.Toplevel()
    find_window.title("Find Track")
    find_window.geometry("300x200")

    tk.Label(find_window, text="Enter Track ID to Find").grid(row=0, column=0)
    id_entry = tk.Entry(find_window)
    id_entry.grid(row=0, column=1)

    def find_track():
        IdTrack = id_entry.get()
        track = library.find_track(IdTrack)
        if track:
            info = f"ID: {track.IdTrack}\nName: {track.nameTrack}\nArtist: {track.artist}\nGenre: {track.genre}"
            messagebox.showinfo("Track Found", info)
        else:
            messagebox.showerror("Error", "Track not found")
        find_window.destroy()

    tk.Button(find_window, text="Find", command=find_track).grid(row=1, column=0, columnspan=2)
