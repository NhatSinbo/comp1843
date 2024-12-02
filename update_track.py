# update_track.py

import tkinter as tk
from tkinter import messagebox

def update_track_gui(library):
    update_window = tk.Toplevel()
    update_window.title("Update Track")
    update_window.geometry("400x350")

    tk.Label(update_window, text="Track ID").grid(row=0, column=0)
    id_entry = tk.Entry(update_window)
    id_entry.grid(row=0, column=1)

    tk.Label(update_window, text="New Name").grid(row=1, column=0)
    name_entry = tk.Entry(update_window)
    name_entry.grid(row=1, column=1)

    tk.Label(update_window, text="New Artist").grid(row=2, column=0)
    artist_entry = tk.Entry(update_window)
    artist_entry.grid(row=2, column=1)

    tk.Label(update_window, text="New Genre").grid(row=3, column=0)
    genre_entry = tk.Entry(update_window)
    genre_entry.grid(row=3, column=1)

    tk.Label(update_window, text="New File Path / YouTube Link").grid(row=4, column=0)
    file_entry = tk.Entry(update_window)
    file_entry.grid(row=4, column=1)

    def update_track():
        IdTrack = id_entry.get()
        new_name = name_entry.get()
        new_artist = artist_entry.get()
        new_genre = genre_entry.get()
        new_file_path = file_entry.get()

        track = library.find_track(IdTrack)
        if track:
            # Cập nhật thông tin bài hát
            track.update_info(nameTrack=new_name, artist=new_artist, genre=new_genre, file_path=new_file_path)
            library.save_to_file()  # Lưu danh sách bài hát vào tệp JSON sau khi cập nhật
            messagebox.showinfo("Success", "Track updated successfully")
        else:
            messagebox.showerror("Error", "Track not found")
        update_window.destroy()

    tk.Button(update_window, text="Update", command=update_track).grid(row=5, column=0, columnspan=2)
