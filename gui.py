
import tkinter as tk
from add_track import add_track_gui
from remove_track import remove_track_gui
from play_track import play_track_gui
from find_track import find_track_gui
from update_track import update_track_gui
from display_tracks import display_tracks_gui
from track_library import TrackLibrary

def main_gui():
    library = TrackLibrary()
    library.load_from_file()  # Tải dữ liệu từ tệp JSON

    root = tk.Tk()
    root.title("JukeBox")
    root.geometry("500x300")
    root.resizable(False, False)

    # Khung tiêu đề
    title_frame = tk.Frame(root, bd=2, relief="ridge", bg="lightgray")
    title_frame.pack(side="top", fill="x", pady=10)
    tk.Label(title_frame, text="Select an option by clicking one of the buttons below",
             font=("Arial", 12, "bold"), bg="lightgray").pack(pady=5)

    # Khung nút
    button_frame = tk.Frame(root)
    button_frame.pack(pady=20)

    tk.Button(button_frame, text="View Tracks", width=20, height=2,
              command=lambda: display_tracks_gui(library)).grid(row=0, column=0, padx=10, pady=10)
    tk.Button(button_frame, text="Add Track", width=20, height=2,
              command=lambda: add_track_gui(library)).grid(row=0, column=1, padx=10, pady=10)
    tk.Button(button_frame, text="Find Track", width=20, height=2,
              command=lambda: find_track_gui(library)).grid(row=1, column=0, padx=10, pady=10)
    tk.Button(button_frame, text="Remove Track", width=20, height=2,
              command=lambda: remove_track_gui(library)).grid(row=1, column=1, padx=10, pady=10)
    tk.Button(button_frame, text="Play Track", width=20, height=2,
              command=lambda: play_track_gui(library)).grid(row=2, column=0, padx=10, pady=10)
    tk.Button(button_frame, text="Update Track", width=20, height=2,
              command=lambda: update_track_gui(library)).grid(row=2, column=1, padx=10, pady=10)

    root.mainloop()

if __name__ == "__main__":
    main_gui()
