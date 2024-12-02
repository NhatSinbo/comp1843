# add_track.py

import tkinter as tk
from tkinter import messagebox, filedialog
from track_library import Track, TrackLibrary

def add_track_gui(library):
    add_window = tk.Toplevel()
    add_window.title("Add Track")
    add_window.geometry("400x350")

    tk.Label(add_window, text="ID").grid(row=0, column=0)
    id_entry = tk.Entry(add_window)
    id_entry.grid(row=0, column=1)

    tk.Label(add_window, text="Name").grid(row=1, column=0)
    name_entry = tk.Entry(add_window)
    name_entry.grid(row=1, column=1)

    tk.Label(add_window, text="Artist").grid(row=2, column=0)
    artist_entry = tk.Entry(add_window)
    artist_entry.grid(row=2, column=1)

    tk.Label(add_window, text="Genre").grid(row=3, column=0)
    genre_entry = tk.Entry(add_window)
    genre_entry.grid(row=3, column=1)

    tk.Label(add_window, text="File Path / YouTube Link").grid(row=4, column=0)
    file_entry = tk.Entry(add_window)
    file_entry.grid(row=4, column=1)

    def browse_file():
        # Chọn tệp từ hệ thống
        file_path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")])
        if file_path:
            file_entry.delete(0, tk.END)
            file_entry.insert(0, file_path)

    # Nút để chọn tệp
    tk.Button(add_window, text="Browse", command=browse_file).grid(row=4, column=2)

    def save_track():
        IdTrack = id_entry.get()
        nameTrack = name_entry.get()
        artist = artist_entry.get()
        genre = genre_entry.get()
        file_path = file_entry.get()  # Lấy đường dẫn tệp hoặc link YouTube

        if not IdTrack or not nameTrack or not artist or not genre or not file_path:
            messagebox.showerror("Input Error", "Please fill all fields correctly")
            return

        track = Track(IdTrack, nameTrack, artist, genre, file_path)
        library.add_track(track)
        library.save_to_file()  # Lưu danh sách bài hát vào tệp JSON
        messagebox.showinfo("Success", "Track added successfully")
        add_window.destroy()

    tk.Button(add_window, text="Save", command=save_track).grid(row=5, column=0, columnspan=2)
