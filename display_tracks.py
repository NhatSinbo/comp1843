
from tkinter import Tk, Label, Listbox, Button, Scrollbar, Frame, END, VERTICAL

def display_tracks_gui(library):
    root = Tk()
    root.title("Track Viewer")
    root.geometry("700x500")
    root.resizable(False, False)

    # Tạo khung cho danh sách bài hát
    list_frame = Frame(root, bd=2, relief="groove")
    list_frame.place(x=10, y=10, width=450, height=300)

    Label(list_frame, text="Track List", font=("Arial", 14, "bold")).pack(anchor="n", pady=5)
    scrollbar_y = Scrollbar(list_frame, orient=VERTICAL)
    scrollbar_y.pack(side="right", fill="y")
    tracks_list = Listbox(list_frame, yscrollcommand=scrollbar_y.set, font=("Arial", 12), width=40, height=15)
    tracks_list.pack(fill="both", expand=True)
    scrollbar_y.config(command=tracks_list.yview)

    # Hàm hiển thị tất cả các bài hát
    def list_all_tracks():
        tracks_list.delete(0, END)
        for track in library.list_all_tracks():
            tracks_list.insert(END, f"{track.IdTrack} - {track.nameTrack} by {track.artist}")

    Button(root, text="List All Tracks", font=("Arial", 12), width=15, command=list_all_tracks).place(x=480, y=150)

    root.mainloop()
