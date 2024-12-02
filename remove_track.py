# remove_track.py

import tkinter as tk
from tkinter import messagebox

def remove_track_gui(library):
    remove_window = tk.Toplevel()
    remove_window.title("Remove Track")
    remove_window.geometry("300x200")

    tk.Label(remove_window, text="Enter Track ID to Remove").grid(row=0, column=0)
    id_entry = tk.Entry(remove_window)
    id_entry.grid(row=0, column=1)

    def delete_track():
        IdTrack = id_entry.get()
        track = library.find_track(IdTrack)
        if track:
            library.remove_track(IdTrack)
            messagebox.showinfo("Success", "Track removed successfully")
        else:
            messagebox.showerror("Error", "Track not found")
        remove_window.destroy()

    tk.Button(remove_window, text="Delete", command=delete_track).grid(row=1, column=0, columnspan=2)
