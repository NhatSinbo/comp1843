# play_track.py

import tkinter as tk
from tkinter import messagebox
import webbrowser  # Để mở link YouTube
import pygame  # Để phát nhạc
import time
import threading  # Để chạy bộ đếm thời gian đồng thời

pygame.mixer.init()  # Khởi tạo pygame mixer

def play_track_gui(library):
    # Tạo cửa sổ phát nhạc
    play_window = tk.Toplevel()
    play_window.title("Play Track")
    play_window.geometry("400x300")

    # Nhập ID của bài hát
    tk.Label(play_window, text="Enter Track ID to Play").grid(row=0, column=0)
    id_entry = tk.Entry(play_window)
    id_entry.grid(row=0, column=1)

    # Nhãn để hiển thị thời gian phát hiện tại của bài hát
    time_label = tk.Label(play_window, text="Current time: 0s")
    time_label.grid(row=2, column=0, columnspan=2)

    # Biến để lưu trạng thái phát nhạc và thời gian hiện tại
    is_playing = False
    current_time = 0

    # Hàm để cập nhật thời gian
    def update_time():
        nonlocal current_time, is_playing
        while is_playing:
            time.sleep(1)
            current_time += 1
            time_label.config(text=f"Current time: {current_time}s")

    # Hàm để phát hoặc tạm dừng bài hát
    def toggle_play():
        nonlocal is_playing, current_time
        IdTrack = id_entry.get()
        track = library.find_track(IdTrack)

        if track:
            if track.file_path.startswith("http"):  # Kiểm tra nếu là link YouTube
                webbrowser.open(track.file_path)  # Mở link YouTube trong trình duyệt
                messagebox.showinfo("Now Playing", f"Playing {track.nameTrack} on YouTube")
                # Ẩn nút Play/Pause và Stop khi phát từ YouTube
                play_button.grid_remove()
                stop_button.grid_remove()
                time_label.config(text="")  # Không hiển thị bộ đếm thời gian
            else:
                if not is_playing:
                    # Phát nhạc từ file nội bộ
                    try:
                        pygame.mixer.music.load(track.file_path)
                        pygame.mixer.music.play()
                        is_playing = True
                        current_time = 0  # Đặt lại thời gian về 0
                        threading.Thread(target=update_time, daemon=True).start()  # Chạy bộ đếm thời gian
                        play_button.config(text="Pause")  # Chuyển nút thành "Pause"
                    except Exception as e:
                        messagebox.showerror("Error", f"Could not play the track: {e}")
                else:
                    # Tạm dừng nhạc
                    pygame.mixer.music.pause()
                    is_playing = False
                    play_button.config(text="Play")  # Chuyển nút thành "Play"
        else:
            messagebox.showerror("Error", "Track not found")

    # Hàm để dừng hoàn toàn bài hát
    def stop_track():
        nonlocal is_playing, current_time
        pygame.mixer.music.stop()
        is_playing = False
        current_time = 0
        time_label.config(text="Current time: 0s")
        play_button.config(text="Play")

    # Nút phát/tạm dừng và nút dừng
    play_button = tk.Button(play_window, text="Play", command=toggle_play)
    play_button.grid(row=1, column=0)
    stop_button = tk.Button(play_window, text="Stop", command=stop_track)
    stop_button.grid(row=1, column=1)

    play_window.mainloop()
